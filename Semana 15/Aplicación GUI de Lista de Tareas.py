import tkinter as tk
from tkinter import messagebox
import json
import os
from datetime import datetime


class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi lista de tareas")

        # Archivo donde se guardarán las tareas
        self.filename = "tasks.json"
        self.tasks = {}

        # ===== Interfaz gráfica =====
        # Título
        title = tk.Label(root, text="📋 Mi lista de tareas", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Entrada de nueva tarea
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.entry_var, font=("Arial", 12))
        self.entry.pack(pady=5, padx=10, fill="x")

        # Botones
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Añadir Tarea", command=self.add_task).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Marcar como Completada", command=self.complete_task).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Eliminar Tarea", command=self.delete_task).grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.listbox = tk.Listbox(root, width=70, height=12, font=("Arial", 11))
        self.listbox.pack(padx=10, pady=10)

        # Eventos
        self.entry.bind("<Return>", lambda event: self.add_task())
        self.listbox.bind("<Double-Button-1>", lambda event: self.complete_task())

        # Cargar tareas existentes
        self.load_tasks()
        self.refresh_tasks()

    # ===== Lógica de tareas =====
    def add_task(self):
        text = self.entry_var.get().strip()
        if not text:
            messagebox.showwarning("Entrada vacía", "Escribe una tarea antes de añadirla.")
            return

        # Generar nuevo ID único
        new_id = max(self.tasks.keys(), default=0) + 1

        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.tasks[new_id] = {"text": text, "completed": False, "datetime": fecha_hora}

        self.entry_var.set("")
        self.save_tasks()
        self.refresh_tasks()

    def complete_task(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showinfo("Seleccionar tarea", "Selecciona una tarea para marcar como completada.")
            return

        index = selection[0]
        task_id = list(self.tasks.keys())[index]
        self.tasks[task_id]["completed"] = not self.tasks[task_id]["completed"]

        self.save_tasks()
        self.refresh_tasks()

    def delete_task(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showinfo("Seleccionar tarea", "Selecciona una tarea para eliminar.")
            return

        index = selection[0]
        task_id = list(self.tasks.keys())[index]
        del self.tasks[task_id]

        self.save_tasks()
        self.refresh_tasks()

    def refresh_tasks(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks.values():
            estado = "✔️" if task["completed"] else "❌"
            self.listbox.insert(
                tk.END,
                f"{estado} {task['text']}  ({task['datetime']})"
            )

    # ===== Manejo de JSON =====
    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                self.tasks = json.load(f)
            # Convertir claves a enteros (JSON guarda como string)
            self.tasks = {int(k): v for k, v in self.tasks.items()}


# ===== Ejecutar aplicación =====
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()
