#sistema de gestión de inventarios simple para una tienda

class Producto:
    #constructor clase producto
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f" {self.id_producto} ,{self.nombre},Cantidad: {self.cantidad},Precio: ${self.precio}"

class Inventario:
    #constructor clase inventario
    def __init__(self):
        self.productos ={}
    def AgregarProducto(self,producto):
        if producto.id_producto in self.productos:
            print("Error: El producto ya existe.")
        else:
            self.productos[producto.id_producto] = producto
    def EliminarProducto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Error: Producto no encontrado.")

    def ActualizarProducto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                 self.productos[id_producto].precio = precio
        else:
            print("Error: Producto no encontrado.")

    def BuscarProducto(self, nombre):
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)

    def MostrarInventario(self):
        for producto in self.productos.values():
            print(producto)
def menu():
    #menu principal
        inventario = Inventario()
        while True:
            print("\n Bienvenidos al Sistema de Gestión de Inventarios")
            print("\n1. Agregar producto\n2. Eliminar producto\n3. Actualizar producto\n4. Buscar producto\n5. Mostrar Inventario\n6. Salir")
            opcion = input("seleccione una opcion")
            if opcion=="6":
                break
            elif opcion == "1":
                id_producto=input("ingrese el id de producto")
                nombre=input("ingrese el nombre de producto")
                cantidad=int(input("ingrese la cantidad de producto"))
                precio=float(input("ingrese la precio de producto"))
                producto= Producto(id_producto, nombre, cantidad, precio)
                inventario.AgregarProducto(producto)
            elif opcion == "2":
                id_producto=input("ingrese el id de producto para eliminar")
                inventario.EliminarProducto(id_producto)
            elif opcion == "3":
                id_producto=input("ingrese el id de producto para actualizar")
                cantidad=int(input("ingrese la cantidad de producto"))
                precio=float(input("ingrese la precio de producto"))
                cantidad=int(cantidad) if cantidad else None
                precio=float (precio) if precio else None
                inventario.ActualizarProducto(id_producto, cantidad, precio)
            elif opcion == "4":
                nombre =input("ingrese el nombre de producto a buscar")
                inventario.BuscarProducto(nombre)
            elif opcion == "5":
                inventario.MostrarInventario()

if __name__=="__main__":
        menu()