# estado_en_reparacion.py
from Biblio.Exceptions import Exceptions
from typing import TYPE_CHECKING
from Biblio.Books.estado_ejemplar import EstadoEjemplar

if TYPE_CHECKING:
    from Biblio.Books.ejemplar import Ejemplar

class EstadoEnReparacion(EstadoEjemplar):
    def prestar(self, ejemplar: "Ejemplar") -> None:
        raise Exceptions(311) # El ejemplar se encuentra en reparación y no puede ser prestado.

    def devolver(self, ejemplar: "Ejemplar") -> None:
        from Biblio.Books.estado_disponible import EstadoDisponible
        print(f"Info: El ejemplar {ejemplar.codigo_barras} está en taller. Se repara y pasa a Disponible.")
        ejemplar.estado = EstadoDisponible()

    def obtener_nombre(self) -> str:
        return "En Reparación"