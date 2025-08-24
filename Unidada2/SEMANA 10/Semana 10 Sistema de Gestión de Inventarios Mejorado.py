#----Sistema de Gestión de Inventarios Mejorado----

import os
import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto.strip()
        self.nombre = nombre.strip()
        self.cantidad = cantidad
        self.precio = precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(
            data["id_producto"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )

    def __str__(self):
        return "{:<10} {:<20} {:<10} {:<10.2f}".format(
            self.id_producto, self.nombre, self.cantidad, self.precio
        )


class Inventario:
    def __init__(self, archivo="Inventario.txt"):
        self.archivo = archivo
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        """Carga los productos desde el archivo"""
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.productos = [Producto.from_dict(p) for p in data]
            else:
                self.productos = []
        except (FileNotFoundError, json.JSONDecodeError):
            print("⚠️ El archivo estaba vacío o dañado. Se creará uno nuevo.")
            self.productos = []
        except PermissionError:
            print("❌ No tienes permisos para leer el archivo de inventario.")

    def guardar_inventario(self):
        """Guarda los productos en el archivo"""
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump([p.to_dict() for p in self.productos], f, indent=4, ensure_ascii=False)
        except PermissionError:
            print("❌ No tienes permisos para escribir en el archivo de inventario.")

    def agregar_producto(self, producto):
        if producto.cantidad < 0 or producto.precio < 0:
            print("⚠️ No se permiten cantidades o precios negativos.")
            return
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print(f"⚠️ Ya existe un producto con ID '{producto.id_producto}'.")
            return
        self.productos.append(producto)
        self.guardar_inventario()
        print(f"✅ Producto '{producto.nombre}' agregado correctamente.")

    def eliminar_producto(self, id_producto):
        producto = next((p for p in self.productos if p.id_producto == id_producto), None)
        if producto:
            self.productos.remove(producto)
            self.guardar_inventario()
            print(f"✅ Producto '{producto.nombre}' eliminado correctamente.")
        else:
            print("⚠️ No se encontró un producto con ese ID.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = next((p for p in self.productos if p.id_producto == id_producto), None)
        if producto:
            if cantidad is not None:
                if cantidad < 0:
                    print("⚠️ La cantidad no puede ser negativa.")
                    return
                producto.cantidad = cantidad
            if precio is not None:
                if precio < 0:
                    print("⚠️ El precio no puede ser negativo.")
                    return
                producto.precio = precio
            self.guardar_inventario()
            print(f"✅ Producto '{producto.nombre}' actualizado correctamente.")
        else:
            print("⚠️ No se encontró un producto con ese ID.")

    def mostrar_inventario(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("\n📋 Inventario Actual:")
            print("{:<10} {:<20} {:<10} {:<10}".format("ID", "Nombre", "Cantidad", "Precio"))
            print("-" * 55)
            for p in self.productos:
                print(p)

    def buscar_producto(self, nombre):
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        if encontrados:
            print("\n🔎 Resultados de búsqueda:")
            print("{:<10} {:<20} {:<10} {:<10}".format("ID", "Nombre", "Cantidad", "Precio"))
            print("-" * 55)
            for p in encontrados:
                print(p)
        else:
            print(f"⚠️ No se encontraron productos con el nombre '{nombre}'.")


# ---------------------------
# Interfaz de consola
# ---------------------------
if __name__ == "__main__":
    inventario = Inventario()

    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Mostrar inventario")
        print("2. Agregar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            inventario.mostrar_inventario()
        elif opcion == "2":
            try:
                id_p = input("ID: ").strip()
                nombre = input("Nombre: ").strip()
                cantidad = int(input("Cantidad: ").strip())
                precio = float(input("Precio: ").strip())
                producto = Producto(id_p, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except ValueError:
                print("⚠️ Error: cantidad y precio deben ser numéricos.")
        elif opcion == "3":
            id_p = input("ID del producto a actualizar: ").strip()
            try:
                cantidad_input = input("Nueva cantidad (Enter para no cambiar): ").strip()
                precio_input = input("Nuevo precio (Enter para no cambiar): ").strip()

                cantidad = int(cantidad_input) if cantidad_input else None
                precio = float(precio_input) if precio_input else None

                inventario.actualizar_producto(id_p, cantidad, precio)
            except ValueError:
                print("⚠️ Error: cantidad y precio deben ser numéricos.")
        elif opcion == "4":
            id_p = input("ID del producto a eliminar: ").strip()
            inventario.eliminar_producto(id_p)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del producto a buscar: ").strip()
            inventario.buscar_producto(nombre)
        elif opcion == "6":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("⚠️ Opción no válida.")

