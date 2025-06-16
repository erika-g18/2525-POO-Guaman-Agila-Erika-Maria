# Programación Tradicional
# Ejemplo:

#Practicar la definición y uso de funciones en Python para calcular temperaturas promedio
#

def temperatura_promedio(ciudades_temperaturas): #funcion para calcular la temperatura
    temperaturas_promedio = {}

    for ciudad, semanas in ciudades_temperaturas.items():
        todas_las_temperaturas = []

        for semana in semanas:
            for dia in semana:
                todas_las_temperaturas.append(dia["temperatura"])  # Extraemos la temperatura

        promedio = sum(todas_las_temperaturas) / len(todas_las_temperaturas)
        temperaturas_promedio[ciudad] = promedio

    return temperaturas_promedio


# Diccionario de ciudades y temperaturas
ciudades_temperaturas = {
    "paltas": [
        [  # semana 1
            {"day": "lunes", "temperatura": 15},
            {"day": "martes", "temperatura": 20},
            {"day": "miercoles", "temperatura": 21},
            {"day": "jueves", "temperatura": 21},
            {"day": "viernes", "temperatura": 20},
            {"day": "sabado", "temperatura": 19},
            {"day": "domingo", "temperatura": 19},
        ],
        [  # semana 2
            {"day": "lunes", "temperatura": 19},
            {"day": "martes", "temperatura": 21},
            {"day": "miercoles", "temperatura": 21},
            {"day": "jueves", "temperatura": 19},
            {"day": "viernes", "temperatura": 19},
            {"day": "sabado", "temperatura": 20},
            {"day": "domingo", "temperatura": 21},
        ],
        [  # semana 3
            {"day": "lunes", "temperatura": 19},
            {"day": "martes", "temperatura": 15},
            {"day": "miercoles", "temperatura": 20},
            {"day": "jueves", "temperatura": 25},
            {"day": "viernes", "temperatura": 23},
            {"day": "sabado", "temperatura": 19},
            {"day": "domingo", "temperatura": 22},
        ],
        [  # semana 4
            {"day": "lunes", "temperatura": 20},
            {"day": "martes", "temperatura": 18},
            {"day": "miercoles", "temperatura": 20},
            {"day": "jueves", "temperatura": 25},
            {"day": "viernes", "temperatura": 21},
            {"day": "sabado", "temperatura": 27},
            {"day": "domingo", "temperatura": 26},
        ]
    ],
    "loja": [
        [  # semana 1
            {"day": "lunes", "temperatura": 13},
            {"day": "martes", "temperatura": 20},
            {"day": "miercoles", "temperatura": 21},
            {"day": "jueves", "temperatura": 21},
            {"day": "viernes", "temperatura": 20},
            {"day": "sabado", "temperatura": 20},
            {"day": "domingo", "temperatura": 19},
        ],
        [  # semana 2
            {"day": "lunes", "temperatura": 19},
            {"day": "martes", "temperatura": 22},
            {"day": "miercoles", "temperatura": 21},
            {"day": "jueves", "temperatura": 20},
            {"day": "viernes", "temperatura": 20},
            {"day": "sabado", "temperatura": 19},
            {"day": "domingo", "temperatura": 21},
        ],
        [  # semana 3
            {"day": "lunes", "temperatura": 19},
            {"day": "martes", "temperatura": 17},
            {"day": "miercoles", "temperatura": 18},
            {"day": "jueves", "temperatura": 20},
            {"day": "viernes", "temperatura": 22},
            {"day": "sabado", "temperatura": 19},
            {"day": "domingo", "temperatura": 24},
        ],
        [  # semana 4
            {"day": "lunes", "temperatura": 20},
            {"day": "martes", "temperatura": 18},
            {"day": "miercoles", "temperatura": 19},
            {"day": "jueves", "temperatura": 21},
            {"day": "viernes", "temperatura": 23},
            {"day": "sabado", "temperatura": 20},
            {"day": "domingo", "temperatura": 18},
        ]
    ],
    "catamayo": [
        [  # semana 1
            {"day": "lunes", "temperatura": 18},
            {"day": "martes", "temperatura": 28},
            {"day": "miercoles", "temperatura": 28},
            {"day": "jueves", "temperatura": 28},
            {"day": "viernes", "temperatura": 28},
            {"day": "sabado", "temperatura": 29},
            {"day": "domingo", "temperatura": 29},
        ],
        [  # semana 2
            {"day": "lunes", "temperatura": 29},
            {"day": "martes", "temperatura": 30},
            {"day": "miercoles", "temperatura": 29},
            {"day": "jueves", "temperatura": 29},
            {"day": "viernes", "temperatura": 29},
            {"day": "sabado", "temperatura": 29},
            {"day": "domingo", "temperatura": 29},
        ],
        [  # semana 3
            {"day": "lunes", "temperatura": 19},
            {"day": "martes", "temperatura": 20},
            {"day": "miercoles", "temperatura": 29},
            {"day": "jueves", "temperatura": 25},
            {"day": "viernes", "temperatura": 27},
            {"day": "sabado", "temperatura": 29},
            {"day": "domingo", "temperatura": 26},
        ],
        [  # semana 4
            {"day": "lunes", "temperatura": 19},
            {"day": "martes", "temperatura": 18},
            {"day": "miercoles", "temperatura": 20},
            {"day": "jueves", "temperatura": 25},
            {"day": "viernes", "temperatura": 23},
            {"day": "sabado", "temperatura": 27},
            {"day": "domingo", "temperatura": 28},
        ]
    ]

}

# Llamamos a la función para calcular las temperaturas promedio
temperaturas_promedio = temperatura_promedio(ciudades_temperaturas)

# Mostramos los resultados
print("=====programacion tradicional=====")
print("Temperaturas Promedio de las 4 semanas por Ciudad:")
for ciudad, promedio in temperaturas_promedio.items():

    print(f"{ciudad}: {promedio:.2f}°C")

#ejemplo de programacion orientada#

class DiaClima:
    """
    Representa la información del clima para un día específico.
    Encapsula el nombre del día y su temperatura.
    """

    def __init__(self, nombre_dia, temperatura):
        if not isinstance(nombre_dia, str) or not nombre_dia:
            raise ValueError("El nombre del día debe ser una cadena no vacía.")
        if not isinstance(temperatura, (int, float)):
            raise ValueError("La temperatura debe ser un número.")

        self.__nombre_dia = nombre_dia  # Encapsulamiento
        self.__temperatura = temperatura  # Encapsulamiento

    def get_nombre_dia(self):
        """Retorna el nombre del día."""
        return self.__nombre_dia

    def get_temperatura(self):
        """Retorna la temperatura del día."""
        return self.__temperatura

    def __str__(self):
        """Representación en cadena del objeto DiaClima."""
        return f"{self.__nombre_dia}: {self.__temperatura}°C"


class SemanaClima:
    """
    Representa una semana de información climática, compuesta por 7 objetos DiaClima.
    """

    def __init__(self, dias_temperaturas_lista):
        if not isinstance(dias_temperaturas_lista, list) or len(dias_temperaturas_lista) != 7:
            raise ValueError("Una semana debe tener exactamente 7 días en formato de lista.")

        self.dias = []
        for dia_data in dias_temperaturas_lista:
            # Composición: Cada SemanaClima "tiene" objetos DiaClima
            self.dias.append(DiaClima(dia_data["day"], dia_data["temperatura"]))

    def get_temperaturas_semana(self):
        """Retorna una lista con las temperaturas de todos los días de la semana."""
        return [dia.get_temperatura() for dia in self.dias]

    def __str__(self):
        """Representación en cadena de la SemanaClima."""
        return ", ".join([str(dia) for dia in self.dias])


class CiudadClima:
    """
    Representa el registro de temperaturas para una ciudad a lo largo de varias semanas.
    """

    def __init__(self, nombre_ciudad, semanas_data):
        if not isinstance(nombre_ciudad, str) or not nombre_ciudad:
            raise ValueError("El nombre de la ciudad debe ser una cadena no vacía.")
        if not isinstance(semanas_data, list) or not all(isinstance(s, list) for s in semanas_data):
            raise ValueError("Las semanas de datos deben ser una lista de listas.")

        self.__nombre_ciudad = nombre_ciudad  # Encapsulamiento
        self.semanas = []
        for semana_data in semanas_data:
            # Composición: Cada CiudadClima "tiene" objetos SemanaClima
            self.semanas.append(SemanaClima(semana_data))

    def get_nombre_ciudad(self):
        """Retorna el nombre de la ciudad."""
        return self.__nombre_ciudad

    def get_todas_las_temperaturas(self):
        """
        Recopila todas las temperaturas registradas para esta ciudad
        a lo largo de todas las semanas.
        """
        todas_las_temperaturas = []
        for semana in self.semanas:
            todas_las_temperaturas.extend(semana.get_temperaturas_semana())
        return todas_las_temperaturas

    def calcular_promedio_general(self):
        """
        Calcula el promedio de todas las temperaturas registradas para la ciudad.
        """
        todas_las_temperaturas = self.get_todas_las_temperaturas()
        if not todas_las_temperaturas:
            return 0
        return sum(todas_las_temperaturas) / len(todas_las_temperaturas)

    def __str__(self):
        """Representación en cadena de la CiudadClima."""
        return f"Ciudad: {self.__nombre_ciudad}, Semanas registradas: {len(self.semanas)}"


class PronosticoClima:
    """
    Clase principal que gestiona la colección de ciudades y sus datos climáticos,
    y puede calcular los promedios generales.
    """

    def __init__(self):
        self.ciudades = {}  # Diccionario para almacenar objetos CiudadClima

    def agregar_ciudad_temperaturas(self, nombre_ciudad, semanas_data):
        """
        Crea un objeto CiudadClima y lo añade a la colección.
        """
        if nombre_ciudad in self.ciudades:
            print(f"Advertencia: La ciudad '{nombre_ciudad}' ya existe y será sobrescrita.")
        try:
            self.ciudades[nombre_ciudad] = CiudadClima(nombre_ciudad, semanas_data)
            print(f"Datos de temperatura agregados para {nombre_ciudad}.")
        except ValueError as e:
            print(f"Error al agregar datos para {nombre_ciudad}: {e}")

    def calcular_promedios_ciudades(self):
        """
        Calcula el promedio de temperatura para cada ciudad registrada.
        Retorna un diccionario con los promedios.
        """
        temperaturas_promedio_ciudades = {}
        for nombre_ciudad, ciudad_obj in self.ciudades.items():
            promedio = ciudad_obj.calcular_promedio_general()
            temperaturas_promedio_ciudades[nombre_ciudad] = promedio
        return temperaturas_promedio_ciudades

    def mostrar_informe_promedios(self):
        """
        Muestra los promedios de temperatura por ciudad.
        """
        promedios = self.calcular_promedios_ciudades()
        print("\n--- Temperaturas Promedio de las 4 semanas por Ciudad (POO) ---")
        if not promedios:
            print("No hay datos de ciudades para mostrar.")
            return

        for ciudad, promedio in promedios.items():
            print(f"{ciudad}: {promedio:.2f}°C")


# --- Datos de entrada  ---
ciudades_temperaturas_data = {
    "paltas": [
        [  # semana 1
            {"day": "lunes", "temperatura": 15}, {"day": "martes", "temperatura": 20},
            {"day": "miercoles", "temperatura": 21}, {"day": "jueves", "temperatura": 21},
            {"day": "viernes", "temperatura": 20}, {"day": "sabado", "temperatura": 19},
            {"day": "domingo", "temperatura": 19},
        ],
        [  # semana 2
            {"day": "lunes", "temperatura": 19}, {"day": "martes", "temperatura": 21},
            {"day": "miercoles", "temperatura": 21}, {"day": "jueves", "temperatura": 19},
            {"day": "viernes", "temperatura": 19}, {"day": "sabado", "temperatura": 20},
            {"day": "domingo", "temperatura": 21},
        ],
        [  # semana 3
            {"day": "lunes", "temperatura": 19}, {"day": "martes", "temperatura": 15},
            {"day": "miercoles", "temperatura": 20}, {"day": "jueves", "temperatura": 25},
            {"day": "viernes", "temperatura": 23}, {"day": "sabado", "temperatura": 19},
            {"day": "domingo", "temperatura": 22},
        ],
        [  # semana 4
            {"day": "lunes", "temperatura": 20}, {"day": "martes", "temperatura": 18},
            {"day": "miercoles", "temperatura": 20}, {"day": "jueves", "temperatura": 25},
            {"day": "viernes", "temperatura": 21}, {"day": "sabado", "temperatura": 27},
            {"day": "domingo", "temperatura": 26},
        ]
    ],
    "loja": [
        [  # semana 1
            {"day": "lunes", "temperatura": 13}, {"day": "martes", "temperatura": 20},
            {"day": "miercoles", "temperatura": 21}, {"day": "jueves", "temperatura": 21},
            {"day": "viernes", "temperatura": 20}, {"day": "sabado", "temperatura": 20},
            {"day": "domingo", "temperatura": 19},
        ],
        [  # semana 2
            {"day": "lunes", "temperatura": 19}, {"day": "martes", "temperatura": 22},
            {"day": "miercoles", "temperatura": 21}, {"day": "jueves", "temperatura": 20},
            {"day": "viernes", "temperatura": 20}, {"day": "sabado", "temperatura": 19},
            {"day": "domingo", "temperatura": 21},
        ],
        [  # semana 3
            {"day": "lunes", "temperatura": 19}, {"day": "martes", "temperatura": 17},
            {"day": "miercoles", "temperatura": 18}, {"day": "jueves", "temperatura": 20},
            {"day": "viernes", "temperatura": 22}, {"day": "sabado", "temperatura": 19},
            {"day": "domingo", "temperatura": 24},
        ],
        [  # semana 4
            {"day": "lunes", "temperatura": 20}, {"day": "martes", "temperatura": 18},
            {"day": "miercoles", "temperatura": 19}, {"day": "jueves", "temperatura": 21},
            {"day": "viernes", "temperatura": 23}, {"day": "sabado", "temperatura": 20},
            {"day": "domingo", "temperatura": 18},
        ]
    ],
    "catamayo": [
        [  # semana 1
            {"day": "lunes", "temperatura": 18}, {"day": "martes", "temperatura": 28},
            {"day": "miercoles", "temperatura": 28}, {"day": "jueves", "temperatura": 28},
            {"day": "viernes", "temperatura": 28}, {"day": "sabado", "temperatura": 29},
            {"day": "domingo", "temperatura": 29},
        ],
        [  # semana 2
            {"day": "lunes", "temperatura": 29}, {"day": "martes", "temperatura": 30},
            {"day": "miercoles", "temperatura": 29}, {"day": "jueves", "temperatura": 29},
            {"day": "viernes", "temperatura": 29}, {"day": "sabado", "temperatura": 29},
            {"day": "domingo", "temperatura": 29},
        ],
        [  # semana 3
            {"day": "lunes", "temperatura": 19}, {"day": "martes", "temperatura": 20},
            {"day": "miercoles", "temperatura": 29}, {"day": "jueves", "temperatura": 25},
            {"day": "viernes", "temperatura": 27}, {"day": "sabado", "temperatura": 29},
            {"day": "domingo", "temperatura": 26},
        ],
        [  # semana 4
            {"day": "lunes", "temperatura": 19}, {"day": "martes", "temperatura": 18},
            {"day": "miercoles", "temperatura": 20}, {"day": "jueves", "temperatura": 25},
            {"day": "viernes", "temperatura": 23}, {"day": "sabado", "temperatura": 27},
            {"day": "domingo", "temperatura": 28},
        ]
    ]
}

# --- Programa Principal (Usando el diseño POO) ---
if __name__ == "__main__":
    pronostico = PronosticoClima()

    # Agregar los datos de cada ciudad al objeto PronosticoClima
    for ciudad_nombre, semanas_datos in ciudades_temperaturas_data.items():
        pronostico.agregar_ciudad_temperaturas(ciudad_nombre, semanas_datos)

    # Mostrar los promedios calculados por la clase PronosticoClima
    pronostico.mostrar_informe_promedios()