from Biblio.UI.Presentacion import PresentacionBiblioteca
from Biblio.Exceptions import Exceptions
from Biblio.Books.ejemplar import Ejemplar
from Biblio.Books.Libro import Libro
from Biblio.People.Socio import Socio


class Menu:

    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        self.ui = PresentacionBiblioteca()

    # ==========================
    # MENÚ PRINCIPAL
    # ==========================
    def mostrar_menu_principal(self):

        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestión de Libros")
        print("2. Gestión de Usuarios")
        print("3. Gestión de Préstamos")
        print("4. Iniciar Sesión")
        print("5. Cerrar Sesión")
        print("0. Salir")

        return input("Seleccione una opción: ")

    # ==========================
    # MENÚ LIBROS
    # ==========================
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

                titulo = input("Título del libro: ")
                isbn = input("ISBN: ")
                anio = input("Año de publicación: ")
                paginas = input("Páginas: ")
                codigo = input("Código de barras: ")

                libro = Libro(titulo, isbn, anio, paginas)
                ejemplar = Ejemplar(codigo, libro)

                self.biblioteca.agregar_ejemplar(ejemplar)

            elif opcion == "3":

                codigo = input("Código de barras: ")

                try:
                    self.biblioteca.eliminar_ejemplar(codigo)
                except Exception as e:
                    print(e)

            elif opcion == "0":
                break

    # ==========================
    # MENÚ USUARIOS
    # ==========================
    def menu_usuarios(self):

        while True:

            print("\n=== GESTIÓN DE USUARIOS ===")
            print("1. Registrar usuario del sistema")
            print("2. Registrar socio")
            print("3. Listar socios")
            print("0. Volver")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":

                print("Funcionalidad de usuario del sistema ya manejada por Login.")

            elif opcion == "2":

                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                fec_nac = input("Fecha nacimiento: ")
                tel = input("Teléfono: ")
                mail = input("Mail: ")
                dni = input("DNI: ")
                direccion = input("Dirección: ")

                socio = Socio(nombre, apellido, fec_nac, tel, mail, dni, direccion)

                self.biblioteca.registrar_socio(socio)

            elif opcion == "3":

                self.biblioteca.listar_socios()

            elif opcion == "0":
                break

    # ==========================
    # MENÚ PRÉSTAMOS
    # ==========================
    def menu_prestamos(self):

        while True:

            print("\n=== GESTIÓN DE PRÉSTAMOS ===")
            print("1. Listar préstamos activos")
            print("2. Registrar préstamo")
            print("3. Registrar devolución")
            print("0. Volver")

            opcion = input("Seleccione una opción: ")

            # --------------------------
            # LISTAR PRÉSTAMOS
            # --------------------------
            if opcion == "1":

                try:
                    self.biblioteca.listar_prestamos_activos()
                except Exception as e:
                    print(e)

            # --------------------------
            # REGISTRAR PRÉSTAMO
            # --------------------------
            elif opcion == "2":

                codigo = input("Código de ejemplar: ")
                dni = input("DNI del socio: ")

                try:
                    ejemplar = self.biblioteca.buscar_ejemplar(codigo)
                    socio = self.biblioteca.buscar_socio(dni)

                    self.biblioteca.registrar_prestamo(ejemplar, socio)

                except Exception as e:
                    print(e)

            # --------------------------
            # DEVOLUCIÓN
            # --------------------------
            elif opcion == "3":

                codigo = input("Código del ejemplar: ")

                prestamo = self.biblioteca.buscar_prestamo_por_codigo(codigo)

                if prestamo is None:
                    print("No se encontró un préstamo activo con ese código.")
                else:
                    self.biblioteca.registrar_devolucion(prestamo)

            elif opcion == "0":
                break

    # ==========================
    # EJECUCIÓN PRINCIPAL
    # ==========================
    def ejecutar(self):

        while True:

            opcion = self.mostrar_menu_principal()

            # LIBROS
            if opcion == "1":
                self.menu_libros()

            # USUARIOS / SOCIOS
            elif opcion == "2":
                self.menu_usuarios()

            # PRÉSTAMOS
            elif opcion == "3":
                self.menu_prestamos()

            # LOGIN
            elif opcion == "4":

                try:
                    self.biblioteca.iniciar_sesion()
                except Exception as e:
                    print(e)

            # LOGOUT
            elif opcion == "5":
                self.biblioteca.cerrar_sesion()

            # SALIR
            elif opcion == "0":
                break

            else:
                print("Opción inválida.")
            elif opcion == "0":
                break

            else:
                print("Opción inválida.")
