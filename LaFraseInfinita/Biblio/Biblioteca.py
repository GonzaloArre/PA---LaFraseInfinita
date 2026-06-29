import json
import os
from datetime import date
from .Catalogo import Catalogo
from .People.Socio import Socio
from .Prestamo import Prestamo
from .Exceptions import Exceptions
from .Books.estado_prestado import EstadoPrestado

#Metaclase que registra automaticamente cuando se crea una clase del sistema.
class MetaBiblioteca(type):
    def __new__(cls, nombre, bases, atributos):
        print(f"Creando clase: {nombre}")
        return super().__new__(cls, nombre, bases, atributos)

class Biblioteca(metaclass=MetaBiblioteca):
    def __init__(self,nombre):
        self.nombre = nombre
        self.catalogo = Catalogo() # Composicion: Biblioteca tiene un Catalogo
        self.prestamos = [] #Lista de prestamos registrados
        self._cargar_prestamos()

    def _cargar_prestamos(self):
        ruta_archivo = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "Files", "prestamos.json")
        )
        if not os.path.exists(ruta_archivo):
            return

        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            try:
                datos = json.load(archivo)
            except json.JSONDecodeError:
                datos = []

        self.prestamos = []
        for item in datos:
            ejemplar = self.buscar_ejemplar(item.get("codigo_barras"))
            socio = self.buscar_socio(item.get("socio_dni"))
            if ejemplar is None or socio is None:
                continue

            fecha_devolucion = None
            if item.get("fecha_devolucion"):
                try:
                    fecha_devolucion = date.fromisoformat(item["fecha_devolucion"])
                except ValueError:
                    fecha_devolucion = None

            prestamo = Prestamo(ejemplar, socio, fecha_devolucion)
            prestamo.activo = bool(item.get("activo", False))
            if prestamo.activo:
                ejemplar.estado = EstadoPrestado()
            self.prestamos.append(prestamo)

    #Metodo para agregar un ejemplar al sistema
    def agregar_ejemplar(self, ejemplar):
        self.catalogo.agregar_ejemplar(ejemplar)

    #Metodo para buscar un ejemplar en el sistema
    def buscar_ejemplar(self, codigo_barras):
        return self.catalogo.buscar_ejemplar(codigo_barras)
    
    #Metodo para eliminar un ejemplar del sistema
    def eliminar_ejemplar(self, codigo_barras):
        self.catalogo.eliminar_ejemplar(codigo_barras)

    #Metodo para listar todos los ejemplares
    def listar_ejemplares(self):
        self.catalogo.listar_ejemplares()

    def registrar_socio(self, socio):
        Socio.agregar_socio(socio)
    
    def buscar_socio(self, dni):
        return Socio.buscar(dni)

    def eliminar_socio(self, dni):
        Socio.eliminar_socio(dni)

    def listar_socios(self):
        Socio.listar_socios()

    #Metodo para registrar un prestamo
    def registrar_prestamo(self, libro, socio, fecha_devolucion=None):
        if libro is None:
            raise Exceptions(210)
        if socio is None:
            raise Exceptions(111)

        if isinstance(fecha_devolucion, str) and fecha_devolucion:
            fecha_devolucion = fecha_devolucion.strip()
            try:
                fecha_devolucion = date.fromisoformat(fecha_devolucion)
            except ValueError:
                try:
                    fecha_devolucion = date.fromisoformat(fecha_devolucion.replace('/', '-'))
                except ValueError:
                    fecha_devolucion = None

        prestamo = Prestamo(libro, socio, fecha_devolucion)
        prestamo.registrar_prestamo()
        self.prestamos.append(prestamo)
        print(f"Prestamo registrado: {prestamo}")
        return prestamo
    
    #Metodo para registrar una devolucion
    def registrar_devolucion(self,prestamo):
        prestamo.registrar_devolucion()

    def buscar_prestamo(self, codigo_barras):
        for prestamo in self.prestamos:
            if prestamo.ejemplar is not None and prestamo.ejemplar.codigo_barras == codigo_barras and prestamo.esta_activo():
                return prestamo
        return None

    #Metodo para listar prestamos activos
    def listar_prestamos_activos(self):
        activos = [prestamo for prestamo in self.prestamos if prestamo.esta_activo()]
        if not activos:
            print("No hay prestamos activos.")
            return
        for prestamo in activos:
            print(prestamo)
