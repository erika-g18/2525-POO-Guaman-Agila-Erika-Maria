import tkinter as tk
from tkinter import messagebox
import json
import os


class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Lista")  # Título de la ventana cambiado a "Mi Lista"
        self.root.configure(bg='#f0f0f0')  # Fondo general de la ventana en gris claro
        self.tasks = []  # Lista de tuplas: (texto, completado)
        self.tasks_file = "tasks.json"  # Archivo JSON para persistencia
        self.load_tasks()  # Cargar tareas al iniciar
        self.setup_ui()
        self.bind_keys()
        # Configurar cierre de ventana para guardar
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def setup_ui(self):
        # Título principal como Label
        title_label = tk.Label(self.root, text="Mi Lista", font=('Arial', 18, 'bold'),
                               bg='#f0f0f0', fg='#333333')
        title_label.pack(pady=(10, 5))

        # Explicación de atajos de teclado
        shortcuts_label = tk.Label(self.root,
                                   text="Atajos: Enter (añadir) | C (completar tarea seleccionada) | D/Delete (eliminar tarea seleccionada) | Esc (salir)",
                                   font=('Arial', 9, 'italic'), bg='#f0f0f0', fg='#666666', wraplength=500)
        shortcuts_label.pack(pady=(0, 10))

        # Campo de entrada para nuevas tareas con color de fondo
        self.entry = tk.Entry(self.root, font=('Arial', 12), width=50, bg='#e6f3ff', relief=tk.SOLID, bd=1)
        self.entry.pack(pady=10)
        self.entry.bind('<Return>', lambda e: self.add_task())

        # Frame para botones con fondo
        btn_frame = tk.Frame(self.root, bg='#f0f0f0')
        btn_frame.pack(pady=5)

        # Botón para añadir tarea con colores verde
        self.add_btn = tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task,
                                 font=('Arial', 10, 'bold'), bg='#4CAF50', fg='white',
                                 relief=tk.RAISED, bd=2, padx=10)
        self.add_btn.pack(side=tk.LEFT, padx=5)

        # Botón para marcar como completada con colores azul
        self.complete_btn = tk.Button(btn_frame, text="Completar", command=self.complete_task,
                                      font=('Arial', 10, 'bold'), bg='#2196F3', fg='white',
                                      relief=tk.RAISED, bd=2, padx=10)
        self.complete_btn.pack(side=tk.LEFT, padx=5)

        # Botón para eliminar con colores rojo
        self.delete_btn = tk.Button(btn_frame, text="Eliminar", command=self.delete_task,
                                    font=('Arial', 10, 'bold'), bg='#f44336', fg='white',
                                    relief=tk.RAISED, bd=2, padx=10)
        self.delete_btn.pack(side=tk.LEFT, padx=5)

        # Frame para la lista con scroll
        list_frame = tk.Frame(self.root, bg='#f0f0f0')
        list_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Listbox para mostrar tareas con colores de fondo y texto
        self.listbox = tk.Listbox(list_frame, font=('Arial', 11), height=10,
                                  bg='#ffffff', fg='#333333', selectbackground='#b3d9ff',
                                  relief=tk.SOLID, bd=1)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar para la listbox
        scrollbar = tk.Scrollbar(list_frame, bg='#cccccc')
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        # Actualizar la lista al cargar
        self.update_listbox()

    def bind_keys(self):
        # Atajo para cerrar la aplicación (ahora guarda antes de salir)
        self.root.bind('<Escape>', lambda e: self.on_closing())

        # Atajo para completar tarea (tecla "c" o "C")
        self.root.bind('<c>', lambda e: self.complete_task())
        self.root.bind('<C>', lambda e: self.complete_task())

        # Atajo para eliminar tarea (tecla Delete o "d" o "D")
        self.root.bind('<Delete>', lambda e: self.delete_task())
        self.root.bind('<d>', lambda e: self.delete_task())
        self.root.bind('<D>', lambda e: self.delete_task())

    def save_tasks(self):
        """Guardar tareas en archivo JSON"""
        tasks_data = [{'text': text, 'completed': completed} for text, completed in self.tasks]
        try:
            with open(self.tasks_file, 'w', encoding='utf-8') as f:
                json.dump(tasks_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar las tareas: {e}")

    def load_tasks(self):
        """Cargar tareas desde archivo JSON"""
        if os.path.exists(self.tasks_file):
            try:
                with open(self.tasks_file, 'r', encoding='utf-8') as f:
                    tasks_data = json.load(f)
                    self.tasks = [(task['text'], task['completed']) for task in tasks_data]
            except Exception as e:
                messagebox.showerror("Error", f"No se pudieron cargar las tareas: {e}")
                self.tasks = []

    def on_closing(self):
        """Función para cerrar la app guardando las tareas"""
        self.save_tasks()
        self.root.destroy()

    def add_task(self):
        text = self.entry.get().strip()
        if text:
            self.tasks.append((text, False))
            self.update_listbox()
            self.entry.delete(0, tk.END)
            self.save_tasks()  # Guardar después de añadir
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese el texto de la tarea.")

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task_text, completed in self.tasks:
            # Prefijo visual para diferenciar
            prefix = "✓ " if completed else "○ "
            if completed:
                display_text = f"{prefix}{task_text} (Completada)"
            else:
                display_text = f"{prefix}{task_text} (Pendiente)"
            self.listbox.insert(tk.END, display_text)

        # Opcional: Cambiar color de selección para resaltar mejor
        if self.tasks:
            self.listbox.selection_set(0)  # Selecciona la primera por defecto si hay tareas

    def get_selected_index(self):
        selection = self.listbox.curselection()
        if selection:
            return selection[0]
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea de la lista.")
            return None

    def complete_task(self):
        index = self.get_selected_index()
        if index is not None:
            # Marcar como completada (setear a True)
            self.tasks[index] = (self.tasks[index][0], True)
            self.update_listbox()
            self.save_tasks()  # Guardar después de completar

    def delete_task(self):
        index = self.get_selected_index()
        if index is not None:
            confirm = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de que desea eliminar esta tarea?")
            if confirm:
                del self.tasks[index]
                self.update_listbox()
                self.save_tasks()  # Guardar después de eliminar


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
