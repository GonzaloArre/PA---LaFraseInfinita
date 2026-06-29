# ejemplar.py
from .Libro import Libro
from .estado_ejemplar import EstadoEjemplar
from .estado_disponible import EstadoDisponible

# Para evitar importaciones circulares, se utilizan importaciones locales dentro de los métodos
# Ejemplar es la clase central que representa cada copia física de un libro en la biblioteca.
class Ejemplar:
    def __init__(self, codigo_barras: str, libro: Libro):
        self.codigo_barras = codigo_barras
        self.libro: Libro = libro
        # El estado inicial por defecto según el negocio es Disponible
        self._estado: EstadoEjemplar = EstadoDisponible()

    @property
    def estado(self) -> EstadoEjemplar:
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado: EstadoEjemplar):
        self._estado = nuevo_estado

    def prestar(self) -> None:
        # Delega el comportamiento al estado actual
        self._estado.prestar(self)

    def devolver(self) -> None:
        # Delega el comportamiento al estado actual
        self._estado.devolver(self)

    def descripcion(self) -> str:
        return f"Ejemplar [{self.codigo_barras}] - {self.libro.nombre_libro()} - Estado: {self._estado.obtener_nombre()}"