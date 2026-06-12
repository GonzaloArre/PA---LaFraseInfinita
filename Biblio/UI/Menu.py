from Biblio.UI.presentacion import PresentacionBiblioteca
from Biblio.Exceptions import Exceptions

class Menu:

    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        self.ui = PresentacionBiblioteca()

    def mostrar_menu_principal(self):
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestión de Libros")
        print("2. Gestión de Usuarios")
        print("3. Gestión de Préstamos")
        print("4. Iniciar Sesión")
        print("5. Cerrar Sesión")
        print("0. Salir")

        return input("Seleccione una opción: ")

    def menu_libros(self):
        while True:
            print("\n=== GESTIÓN DE LIBROS ===")
            print("1. Listar ejemplares")
            print("2. Agregar ejemplar")
            print("3. Eliminar ejemplar")
            print("0. Volver")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                try:
                    self.biblioteca.listar_ejemplares()
                except Exception as e:
                    print(e)

            elif opcion == "2":
                print("Funcionalidad pendiente")

            elif opcion == "3":
                codigo = input("Código de barras: ")

                try:
                    self.biblioteca.eliminar_ejemplar(codigo)
                except Exception as e:
                    print(e)

            elif opcion == "0":
                break

    def menu_usuarios(self):
        while True:
            print("\n=== GESTIÓN DE USUARIOS ===")
            print("1. Registrar usuario")
            print("0. Volver")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print("Funcionalidad pendiente")

            elif opcion == "0":
                break

    def menu_prestamos(self):
        while True:
            print("\n=== GESTIÓN DE PRÉSTAMOS ===")
            print("1. Listar préstamos activos")
            print("0. Volver")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                try:
                    self.biblioteca.listar_prestamos_activos()
                except Exception as e:
                    print(e)

            elif opcion == "0":
                break

    def ejecutar(self):

        while True:

            opcion = self.mostrar_menu_principal()

            if opcion == "1":
                self.menu_libros()

            elif opcion == "2":
                self.menu_usuarios()

            elif opcion == "3":
                self.menu_prestamos()

            elif opcion == "4":

                try:
                    self.biblioteca.iniciar_sesion()
                except Exception as e:
                    print(e)

            elif opcion == "5":
                self.biblioteca.cerrar_sesion()

            elif opcion == "0":
                break

            else:
                print("Opción inválida.")
