import os
from .Presentacion import PresentacionBiblioteca
from ..Exceptions import Exceptions
from ..Books.ejemplar import Ejemplar
from ..Books.Libro import Libro
from ..People.Socio import Socio


class Menu:

    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        self.ui = PresentacionBiblioteca()

    def limpiar(self):
        os.system("cls" if os.name == "nt" else "clear")

    # ==========================
    # MENÚ PRINCIPAL
    # ==========================
    def mostrar_menu_principal(self):

        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Gestión de Libros")
        print("2. Gestión de Socios")
        print("3. Gestión de Préstamos")
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
                self.limpiar()
                try:
                    self.biblioteca.listar_ejemplares()
                except Exception as e:
                    print(e)

            elif opcion == "2":
                self.limpiar()
                titulo = input("Título del libro: ")
                isbn = input("ISBN: ")
                anio = input("Año de publicación: ")
                paginas = input("Páginas: ")
                codigo = input("Código de barras: ")
                autor = input("Autor/es (separados por comas): ").split(",")
                self.limpiar()

                libro = Libro(titulo, isbn, anio, paginas)
                for a in autor:
                    libro.agregar_autor(a.strip())
                ejemplar = Ejemplar(codigo, libro)

                self.biblioteca.agregar_ejemplar(ejemplar)

            elif opcion == "3":
                self.limpiar()

                codigo = input("Código de barras: ")

                try:
                    self.biblioteca.eliminar_ejemplar(codigo)
                except Exception as e:
                    print(e)

            elif opcion == "0":
                self.limpiar()
                break

    # ==========================
    # MENÚ SOCIOS
    # ==========================
    def menu_socios(self):

        while True:

            print("\n=== GESTIÓN DE SOCIOS ===")
            print("1. Registrar socio")
            print("2. Eliminar socio")
            print("3. Listar socios")
            print("4. Modificar socio")
            print("0. Volver")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.limpiar()
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                fec_nac = input("Fecha nacimiento: ")
                tel = input("Teléfono: ")
                mail = input("Mail: ")
                dni = input("DNI: ")
                direccion = input("Dirección: ")
                self.limpiar()

                socio = Socio(nombre, apellido, fec_nac, tel, mail, dni, direccion)
                self.biblioteca.registrar_socio(socio)

            elif opcion == "2":
                self.limpiar()
                try:
                    dni = input("Ingrese el DNI del socio a eliminar: ")
                    self.biblioteca.eliminar_socio(dni)
                except Exceptions as e:
                    print(e)
                    continue

            elif opcion == "3":
                self.limpiar()
                try:
                    self.biblioteca.listar_socios()
                except Exception as e:
                    print(e)
                
            elif opcion == "4":
                self.limpiar()
                try:
                    dni = input("Ingrese el DNI del socio a modificar: ")
                    socio = self.biblioteca.buscar_socio(dni)

                    if socio is None:
                        raise Exceptions(111)

                    print("Ingrese los nuevos datos del socio (deje en blanco para no modificar):")
                    nombre = input(f"Nombre ({socio.nombre}): ") or socio.nombre
                    apellido = input(f"Apellido ({socio.apellido}): ") or socio.apellido
                    fec_nac = input(f"Fecha nacimiento ({socio.fec_nac}): ") or socio.fec_nac
                    tel = input(f"Teléfono ({socio.tel}): ") or socio.tel
                    mail = input(f"Mail ({socio.mail}): ") or socio.mail
                    dni = input(f"DNI ({socio.dni}): ") or socio.dni
                    direccion = input(f"Dirección ({socio.direccion}): ") or socio.direccion

                    self.limpiar()
                    socio.modificar(nombre, apellido, fec_nac, tel, mail, direccion)
                except Exceptions as e:
                    print(e)
                    continue

            elif opcion == "0":
                self.limpiar()
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
                self.limpiar()

                try:
                    self.biblioteca.listar_prestamos_activos()
                except Exception as e:
                    print(e)

            # --------------------------
            # REGISTRAR PRÉSTAMO
            # --------------------------
            elif opcion == "2":
                self.limpiar()

                codigo = input("Código de ejemplar: ")
                dni = input("DNI del socio: ")
                fec_devo = input("fecha de devolución(y/m/d): ")

                try:
                    ejemplar = self.biblioteca.buscar_ejemplar(codigo)
                    socio = self.biblioteca.buscar_socio(dni)

                    self.biblioteca.registrar_prestamo(ejemplar, socio, fec_devo)

                except Exception as e:
                    print(e)

            # --------------------------
            # DEVOLUCIÓN
            # --------------------------
            elif opcion == "3":
                self.limpiar()
                codigo = input("Código del ejemplar: ")
                self.limpiar()

                prestamo = self.biblioteca.buscar_prestamo(codigo)

                if prestamo is None:
                    print("No se encontró un préstamo activo con ese código.")
                else:
                    self.biblioteca.registrar_devolucion(prestamo)

            elif opcion == "0":
                self.limpiar()
                break

    # ==========================
    # EJECUCIÓN PRINCIPAL
    # ==========================
    def ejecutar(self):

        while True:

            opcion = self.mostrar_menu_principal()

            # LIBROS
            if opcion == "1":
                self.limpiar()
                self.menu_libros()

            # SOCIOS
            elif opcion == "2":
                self.limpiar()
                self.menu_socios()

            # PRÉSTAMOS
            elif opcion == "3":
                self.limpiar()
                self.menu_prestamos()

            # SALIR
            elif opcion == "0":
                break

            else:
                print("Opción inválida.")
