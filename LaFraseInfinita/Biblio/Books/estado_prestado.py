# estado_prestado.py
from ..Exceptions import Exceptions
from typing import TYPE_CHECKING
from .estado_ejemplar import EstadoEjemplar

if TYPE_CHECKING:
    from .ejemplar import Ejemplar

class EstadoPrestado(EstadoEjemplar):
    estado = "Prestado"

    def prestar(self, ejemplar: "Ejemplar") -> None:
        raise Exceptions(310)  # El ejemplar ya tiene un préstamo activo.

    def devolver(self, ejemplar: "Ejemplar") -> None:
        from .estado_disponible import EstadoDisponible
        print(f"Éxito: El ejemplar {ejemplar.codigo_barras} fue devuelto con éxito.")
        ejemplar.estado = EstadoDisponible()  # Transición de estado