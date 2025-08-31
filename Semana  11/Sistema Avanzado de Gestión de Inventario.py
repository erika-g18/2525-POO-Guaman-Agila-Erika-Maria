import json
import os

# Clase Producto


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos Getters y Setters
    def get_id(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio

    #Método para convertir a diccionario (para guardar en JSON)

    def to_dict(self):
        return {
            "id": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    def __str__(self):
        return f"[ID: {self.id_producto}] | {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"

# Clase Inventario
class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}  # Usamos diccionario {id: Producto}
        self.cargar_inventario()

    # Añadir producto
    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("❌ Error: El ID ya existe en el inventario.")
        else:
            self.productos[producto.get_id()] = producto
            print("✅ Producto añadido con éxito.")
            self.guardar_inventario()

    # Eliminar producto por ID
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("🗑️ Producto eliminado con éxito.")
            self.guardar_inventario()
        else:
            print("❌ Error: El producto no existe.")

    # Actualizar cantidad o precio
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print("♻️ Producto actualizado con éxito.")
            self.guardar_inventario()
        else:
            print("❌ Error: El producto no existe.")

    # Buscar productos por nombre
    def buscar_producto(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(p)
        else:
            print("❌ No se encontraron productos con ese nombre.")

    # Mostrar todos los productos
    def mostrar_productos(self):
        if not self.productos:
            print("📦 El inventario está vacío.")
        else:
            print("\n📋 Inventario actual:")
            for producto in self.productos.values():
                print(producto)

    # Guardar inventario en archivo JSON
    def guardar_inventario(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump({id: p.to_dict() for id, p in self.productos.items()}, f, indent=4, ensure_ascii=False)

    # Cargar inventario desde archivo JSON
    def cargar_inventario(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                for id, info in data.items():
                    self.productos[id] = Producto(info["id"], info["nombre"], info["cantidad"], info["precio"])


# ============================
# Menú interactivo
# ============================
def menu():
    inventario = Inventario()

    while True:
        print("\n====== MENÚ GESTION DE INVENTARIO ======")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre: ")
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (ENTER para no cambiar): ")
            precio = input("Nuevo precio (ENTER para no cambiar): ")
            inventario.actualizar_producto(
                id_producto,
                cantidad=int(cantidad) if cantidad else None,
                precio=float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("👋 Saliendo del sistema. Inventario guardado.")
            break

        else:
            print("❌ Opción inválida. Intente de nuevo.")



# ============================
# Ejecutar programa
# ============================
if __name__ == "__main__":
    menu()
