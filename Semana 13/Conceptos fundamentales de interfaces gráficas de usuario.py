import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada.get()
    if dato.strip() != "":
        lista.insert(tk.END, dato)
        entrada.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío.")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica - Lista de Datos")
ventana.geometry("400x300")

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:", font=("Arial", 12))
etiqueta.pack(pady=5)

# Campo de texto
entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

# Botón para agregar
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato, bg="lightgreen", font=("Arial", 11))
boton_agregar.pack(pady=5)

# Botón para limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista, bg="lightcoral", font=("Arial", 11))
boton_limpiar.pack(pady=5)

# Lista para mostrar los datos
lista = tk.Listbox(ventana, font=("Arial", 12), width=40, height=10)
lista.pack(pady=10)

# Ejecutar aplicación
ventana.mainloop()
