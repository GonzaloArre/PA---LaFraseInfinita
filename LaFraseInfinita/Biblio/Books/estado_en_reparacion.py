# estado_en_reparacion.py
from ..Exceptions import Exceptions
from typing import TYPE_CHECKING
from .estado_ejemplar import EstadoEjemplar

if TYPE_CHECKING:
    from .ejemplar import Ejemplar

class EstadoEnReparacion(EstadoEjemplar):
    estado = "En Reparación"

    def prestar(self, ejemplar: "Ejemplar") -> None:
        raise Exceptions(311) # El ejemplar se encuentra en reparación y no puede ser prestado.

    def devolver(self, ejemplar: "Ejemplar") -> None:
        from .estado_disponible import EstadoDisponible
        print(f"Info: El ejemplar {ejemplar.codigo_barras} está en taller. Se repara y pasa a Disponible.")
        ejemplar.estado = EstadoDisponible()