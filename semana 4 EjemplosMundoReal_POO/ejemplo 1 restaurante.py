"""ejemplo de poo en un restaurante para realizar reservas en linea"""


# Clase que representa el menú del restaurante
class Menu:
    def __init__(self, comida_1, comida_2):
        self.comida_1 = comida_1
        self.comida_2 = comida_2

    def mostrar_menu(self):
        print(f"Menú: {self.comida_1}, {self.comida_2}")


# Clase que representa una mesa y su capacidad
class Mesa:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.ocupada = False

    def mostrar_informacion(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        print(f"Mesa para {self.capacidad} personas - Estado: {estado}")


# Clase para representar al cliente que va a realizar la reservación
class Cliente:
    def __init__(self, nombre, numero_ID):
        self.nombre = nombre
        self.numero_ID = numero_ID

    def mostrar_informacion(self):
        print(f"Cliente: {self.nombre} | Cédula: {self.numero_ID}")


# Clase que representa la reservación
class Reservacion:
    def __init__(self, mesa, menu, hora, precio):
        self.mesa = mesa
        self.menu = menu
        self.hora = hora
        self.precio = precio
        self.ocupada = True  # La reservación ocupa la mesa

    def mostrar_informacion(self):
        print(f"Reservación: Mesa para {self.mesa.capacidad} personas")
        print(f"Menú: {self.menu.comida_1}, {self.menu.comida_2}")
        print(f"Hora: {self.hora} | Precio: {self.precio} | Estado: {'Ocupada' if self.ocupada else 'Disponible'}")


# Clase que representa el restaurante, mesas que dispone y reservaciones
class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mesas = []
        self.reservaciones = []

    def agregar_mesa(self, mesa):
        self.mesas.append(mesa)

    def realizar_reservacion(self, cliente, mesa, menu, hora, precio):
        if not mesa.ocupada:
            reservacion = Reservacion(mesa, menu, hora, precio)
            self.reservaciones.append(reservacion)
            mesa.ocupada = True  # Marcar la mesa como ocupada
            print(f"Reservación realizada para {cliente.nombre} en la mesa para {mesa.capacidad} personas.")
        else:
            print("La mesa ya está ocupada. Por favor, elige otra mesa.")

    def mostrar_informacion(self):
        print(f"Restaurante: {self.nombre}")
        print("Mesas disponibles:")
        for mesa in self.mesas:
            mesa.mostrar_informacion()
        print("Reservaciones:")
        for reservacion in self.reservaciones:
            reservacion.mostrar_informacion()


# Ejemplo de uso
if __name__ == "__main__":
    restaurante = Restaurante("El Buen Sabor")

    # Agregar mesas
    restaurante.agregar_mesa(Mesa(2))
    restaurante.agregar_mesa(Mesa(4))
    restaurante.agregar_mesa(Mesa(10))

    # Crear un menú
    menu = Menu("Hornado", "pollo al jugo")

    # Crear un cliente
    cliente = Cliente("Erika Guaman", "12345678")

    # Realizar una reservación
    restaurante.realizar_reservacion(cliente, restaurante.mesas[0], menu, "19:00", 20.0)

    # Mostrar información del restaurante
    restaurante.mostrar_informacion()
