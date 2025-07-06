# Clase base: Helado
class Helado:
    def __init__(self, sabor, precio):
        # Atributos encapsulados (privados)
        self.__sabor = sabor
        self.__precio = precio

    # Métodos para acceder a los atributos privados
    def obtener_sabor(self):
        return self.__sabor

    def obtener_precio(self):
        return self.__precio

    # Método para mostrar el helado
    def __str__(self):
        return f"Helado de sabor {self.__sabor}, precio: ${self.__precio:.2f}"


# Clase derivada: HeladoConFrutas
class HeladoConFrutas(Helado):
    def __init__(self, sabor, precio, frutas):
        super().__init__(sabor, precio)
        self.__frutas = frutas  # Encapsulado

    def obtener_frutas(self):
        return self.__frutas

    def __str__(self):
        return f"{super().__str__()} con frutas: {', '.join(self.__frutas)}"


# Clase derivada: HeladoConQueso
class HeladoConQueso(Helado):
    def __init__(self, sabor, precio, queso):
        super().__init__(sabor, precio)
        self.__queso = queso  # Encapsulado

    def obtener_queso(self):
        return self.__queso

    def __str__(self):
        return f"{super().__str__()} con queso: {self.__queso}"


# --- Uso del programa ---

helado1 = Helado(sabor='Banana', precio=1.00)
helado2 = HeladoConFrutas(sabor="Chocolate", precio=1.50, frutas=["fresa", "manzana", "papaya"])
helado3 = HeladoConQueso(sabor="Vainilla", precio=2.00, queso="queso crema")

print("=======HELADERIA DULCE MARIA=======")
print("Usted compró un:", helado1)
print("Usted compró un:", helado2)
print("Usted compró un:", helado3)
