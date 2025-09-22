"""
Agenda Personal - Tkinter GUI
Archivo: agenda_tkinter.py
Descripción: Aplicación de agenda personal que permite agregar, ver y eliminar eventos.

guarda los eventos en 'events.json' en el mismo directorio para persistencia.
"""

import json
import os
import uuid
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

# Intentar importar tkcalendar.DateEntry. Si no está disponible, la app seguirá funcionado
# usando una entrada de texto para la fecha (formato YYYY-MM-DD).
try:
    from tkcalendar import DateEntry
    TKCALENDAR_AVAILABLE = True
except Exception:
    DateEntry = None
    TKCALENDAR_AVAILABLE = False

EVENTS_FILE = "events.json"


class AgendaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Agenda Personal")
        self.geometry("700x450")
        self.resizable(False, False)

        # Estructura principal con frames
        self.frame_list = ttk.Frame(self, padding=10)
        self.frame_form = ttk.Frame(self, padding=10)
        self.frame_actions = ttk.Frame(self, padding=10)

        self.frame_list.grid(row=0, column=0, sticky="nsew")
        self.frame_form.grid(row=1, column=0, sticky="ew")
        self.frame_actions.grid(row=2, column=0, sticky="ew")

        # Inicializar componente Treeview para mostrar eventos
        self._create_treeview()

        # Crear formulario de entrada (fecha, hora, descripción)
        self._create_form()

        # Crear botones de acción
        self._create_action_buttons()

        # Cargar eventos desde archivo si existe
        self.events = {}
        self._load_events()

    def _create_treeview(self):
        """Crea y configura el Treeview para listar los eventos."""
        columns = ("date", "time", "desc")
        self.tree = ttk.Treeview(self.frame_list, columns=columns, show="headings", height=10)
        self.tree.heading("date", text="Fecha")
        self.tree.heading("time", text="Hora")
        self.tree.heading("desc", text="Descripción")
        self.tree.column("date", width=120, anchor="center")
        self.tree.column("time", width=80, anchor="center")
        self.tree.column("desc", width=440, anchor="w")
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Scrollbar vertical
        vsb = ttk.Scrollbar(self.frame_list, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=vsb.set)
        vsb.grid(row=0, column=1, sticky="ns")

    def _create_form(self):
        """Crea las entradas para fecha, hora y descripción."""
        # Etiquetas
        lbl_date = ttk.Label(self.frame_form, text="Fecha:")
        lbl_time = ttk.Label(self.frame_form, text="Hora (HH:MM):")
        lbl_desc = ttk.Label(self.frame_form, text="Descripción:")

        lbl_date.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        lbl_time.grid(row=0, column=2, padx=5, pady=5, sticky="e")
        lbl_desc.grid(row=1, column=0, padx=5, pady=5, sticky="ne")

        # Fecha: DateEntry si tkcalendar está disponible, sino Entry simple
        if TKCALENDAR_AVAILABLE:
            self.entry_date = DateEntry(self.frame_form, date_pattern="yyyy-mm-dd")
        else:
            self.entry_date = ttk.Entry(self.frame_form)
            self.entry_date.insert(0, "YYYY-MM-DD")

        self.entry_time = ttk.Entry(self.frame_form)
        self.entry_time.insert(0, "12:00")

        self.text_desc = tk.Text(self.frame_form, height=3, width=60)

        self.entry_date.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.entry_time.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        self.text_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky="w")

    def _create_action_buttons(self):
        """Crea botones: Agregar Evento, Eliminar Evento Seleccionado, Salir."""
        btn_add = ttk.Button(self.frame_actions, text="Agregar Evento", command=self.add_event)
        btn_delete = ttk.Button(self.frame_actions, text="Eliminar Evento Seleccionado", command=self.delete_selected_event)
        btn_exit = ttk.Button(self.frame_actions, text="Salir", command=self.quit)

        btn_add.grid(row=0, column=0, padx=10, pady=10)
        btn_delete.grid(row=0, column=1, padx=10, pady=10)
        btn_exit.grid(row=0, column=2, padx=10, pady=10)

    def add_event(self):
        """Valida y agrega un evento tanto a la estructura en memoria como al Treeview y archivo."""
        date_str = self.entry_date.get().strip()
        time_str = self.entry_time.get().strip()
        desc = self.text_desc.get("1.0", "end").strip()

        # Validaciones básicas
        if not date_str or not time_str or not desc:
            messagebox.showwarning("Campos incompletos", "Por favor complete fecha, hora y descripción.")
            return

        # Validar fecha (YYYY-MM-DD)
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Fecha inválida", "Formato de fecha inválido. Use YYYY-MM-DD.")
            return

        # Validar hora (HH:MM)
        try:
            datetime.strptime(time_str, "%H:%M")
        except ValueError:
            messagebox.showerror("Hora inválida", "Formato de hora inválido. Use HH:MM en 24 horas.")
            return

        # Crear un id único para el evento
        event_id = str(uuid.uuid4())
        event = {"id": event_id, "date": date_str, "time": time_str, "desc": desc}

        # Guardar en memoria y actualizar UI
        self.events[event_id] = event
        self._insert_tree_item(event)
        self._save_events()

        # Limpiar formulario
        if not TKCALENDAR_AVAILABLE:
            self.entry_date.delete(0, tk.END)
            self.entry_date.insert(0, "YYYY-MM-DD")
        else:
            # DateEntry ya provee su selector
            pass
        self.entry_time.delete(0, tk.END)
        self.entry_time.insert(0, "12:00")
        self.text_desc.delete("1.0", tk.END)

        messagebox.showinfo("Evento agregado", "El evento fue agregado correctamente.")

    def _insert_tree_item(self, event):
        """Inserta un evento en el Treeview. Usamos el id como iid para poder identificarlo luego."""
        self.tree.insert("", "end", iid=event["id"], values=(event["date"], event["time"], event["desc"]))

    def delete_selected_event(self):
        """Elimina el evento seleccionado del Treeview y del almacenamiento con confirmación opcional."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Seleccionar evento", "Por favor seleccione un evento para eliminar.")
            return

        # Confirmación
        confirm = messagebox.askyesno("Confirmar eliminación", "¿Seguro que desea eliminar el/los evento(s) seleccionado(s)?")
        if not confirm:
            return

        for iid in selected:
            # Remover del diccionario y del tree
            if iid in self.events:
                del self.events[iid]
            try:
                self.tree.delete(iid)
            except Exception:
                pass

        self._save_events()
        messagebox.showinfo("Eliminado", "Evento(s) eliminado(s) correctamente.")

    def _load_events(self):
        """Carga eventos desde el archivo JSON si existe y los muestra en el Treeview."""
        if not os.path.exists(EVENTS_FILE):
            return
        try:
            with open(EVENTS_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                # data debe ser un dict id -> event
                if isinstance(data, dict):
                    self.events = data
                    for event in self.events.values():
                        self._insert_tree_item(event)
        except Exception as e:
            messagebox.showerror("Error al cargar eventos", f"No se pudieron cargar eventos: {e}")

    def _save_events(self):
        """Guarda los eventos en un archivo JSON para persistencia simple."""
        try:
            with open(EVENTS_FILE, "w", encoding="utf-8") as f:
                json.dump(self.events, f, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("Error al guardar", f"No se pudieron guardar los eventos: {e}")


if __name__ == "__main__":
    # Mensaje informativo si tkcalendar no está instalado
    if not TKCALENDAR_AVAILABLE:
        print("Aviso: tkcalendar no está disponible. La selección de fecha será manual (formato YYYY-MM-DD).\nInstale con: pip install tkcalendar")

    app = AgendaApp()
    app.mainloop()
