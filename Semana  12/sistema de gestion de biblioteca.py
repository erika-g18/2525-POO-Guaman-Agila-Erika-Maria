#******Sistema de Gestión de Biblioteca Digital******
import json
import os

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.datos = (titulo, autor)  # Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.datos[0]} por {self.datos[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"

    def to_dict(self):
        return {
            "titulo": self.datos[0],
            "autor": self.datos[1],
            "categoria": self.categoria,
            "isbn": self.isbn
        }

    @staticmethod
    def from_dict(data):
        return Libro(data["titulo"], data["autor"], data["categoria"], data["isbn"])


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {len(self.libros_prestados)}"

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "id_usuario": self.id_usuario,
            "libros_prestados": [libro.to_dict() for libro in self.libros_prestados]
        }

    @staticmethod
    def from_dict(data):
        usuario = Usuario(data["nombre"], data["id_usuario"])
        usuario.libros_prestados = [Libro.from_dict(l) for l in data["libros_prestados"]]
        return usuario


class Biblioteca:
    def __init__(self, archivo="biblioteca.json"):
        self.libros = {}       # ISBN -> Libro
        self.usuarios = {}     # ID -> Usuario
        self.ids_usuarios = set()
        self.archivo = archivo
        self.cargar_datos()

    # ==========================
    # Manejo de persistencia
    # ==========================
    def guardar_datos(self):
        data = {
            "libros": {isbn: libro.to_dict() for isbn, libro in self.libros.items()},
            "usuarios": {uid: usuario.to_dict() for uid, usuario in self.usuarios.items()}
        }
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def cargar_datos(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.libros = {isbn: Libro.from_dict(ld) for isbn, ld in data.get("libros", {}).items()}
                self.usuarios = {uid: Usuario.from_dict(ud) for uid, ud in data.get("usuarios", {}).items()}
                self.ids_usuarios = set(self.usuarios.keys())

    # ==========================
    # Gestión de libros
    # ==========================
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print("⚠️ Ese ISBN ya existe en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            self.guardar_datos()
            print(f"✅ Libro agregado: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            self.guardar_datos()
            print(f"🗑️ Libro eliminado: {eliminado}")
        else:
            print("⚠️ No se encontró un libro con ese ISBN.")

    def listar_todos_libros(self):
        if self.libros:
            print("\n📚 Catálogo de libros disponibles:")
            for libro in self.libros.values():
                print(f" - {libro}")
        else:
            print("⚠️ No hay libros disponibles en la biblioteca.")

    # ==========================
    # Gestión de usuarios
    # ==========================
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("⚠️ Ese ID de usuario ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            self.guardar_datos()
            print(f"✅ Usuario registrado: {usuario}")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            eliminado = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            self.guardar_datos()
            print(f"🗑️ Usuario dado de baja: {eliminado.nombre}")
        else:
            print("⚠️ No se encontró un usuario con ese ID.")

    # ==========================
    # Préstamos
    # ==========================
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("⚠️ Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("⚠️ Libro no disponible en la biblioteca.")
            return

        usuario = self.usuarios[id_usuario]
        libro = self.libros.pop(isbn)
        usuario.libros_prestados.append(libro)
        self.guardar_datos()
        print(f"📚 Libro prestado: {libro} a {usuario.nombre}")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("⚠️ Usuario no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros[isbn] = libro
                self.guardar_datos()
                print(f"✅ Libro devuelto: {libro}")
                return
        print("⚠️ Ese usuario no tiene prestado este libro.")

    # ==========================
    # Búsquedas
    # ==========================
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.datos[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.datos[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)

        if resultados:
            print("\n🔎 Resultados de la búsqueda:")
            for l in resultados:
                print(f" - {l}")
        else:
            print("⚠️ No se encontraron libros con ese criterio.")

    # ==========================
    # Listado de préstamos
    # ==========================
    def listar_prestamos_usuario(self, id_usuario):
        if id_usuario not in self.usuarios:
            print("⚠️ Usuario no registrado.")
            return

        usuario = self.usuarios[id_usuario]
        if usuario.libros_prestados:
            print(f"\n📖 Libros prestados a {usuario.nombre}:")
            for l in usuario.libros_prestados:
                print(f" - {l}")
        else:
            print(f"{usuario.nombre} no tiene libros prestados.")


# ==========================
# MENÚ INTERACTIVO
# ==========================
def menu():
    biblioteca = Biblioteca()

    while True:
        print("\n===== 📚 MENÚ BIBLIOTECA DIGITAL =====")
        print("1. Agregar libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libros")
        print("8. Listar préstamos de usuario")
        print("9. Salir")
        print("10. Listar todos los libros disponibles")
        opcion = input("👉 Selecciona una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)

        elif opcion == "2":
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID único del usuario: ")
            usuario = Usuario(nombre, id_usuario)
            biblioteca.registrar_usuario(usuario)

        elif opcion == "4":
            id_usuario = input("ID del usuario a dar de baja: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")
            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":
            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":
            print("\nBuscar por: titulo / autor / categoria")
            criterio = input("Criterio: ").lower()
            valor = input("Valor: ")
            biblioteca.buscar_libros(criterio, valor)

        elif opcion == "8":
            id_usuario = input("ID del usuario: ")
            biblioteca.listar_prestamos_usuario(id_usuario)

        elif opcion == "9":
            print("👋 Saliendo del sistema de biblioteca...")
            break

        elif opcion == "10":
            biblioteca.listar_todos_libros()

        else:
            print("⚠️ Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    menu()
