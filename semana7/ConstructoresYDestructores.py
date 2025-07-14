#constructor
# Clase para gestionar la creación y eliminación de usuarios
class CrearUsuario:
    def __init__(self,usuario):
        self.usuario = usuario
        self.activa=True
        print(f"usuario correctamente creado, hola {self.usuario}")

    def EliminarUsuario(self):
        self.activa=False
        print(f"usuario {self.usuario} eliminado")

#destructor
    def __del__(self):
        if self.activa:
            print(f"El usuario {self.usuario} se ha eliminado correctamente")

#
usuario=CrearUsuario("ERIKA")
usuario.EliminarUsuario() # Esto eliminará al usuario

