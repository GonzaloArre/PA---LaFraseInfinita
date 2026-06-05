# estado_en_reparacion.py
from typing import TYPE_CHECKING
from Biblio.Books.estado_ejemplar import EstadoEjemplar

if TYPE_CHECKING:
    from Biblio.Books.ejemplar import Ejemplar

class EstadoEnReparacion(EstadoEjemplar):
    def prestar(self, ejemplar: "Ejemplar") -> None:
        print(f"Error: El ejemplar {ejemplar.codigo_barras} está en reparación y no se puede prestar.")

    def devolver(self, ejemplar: "Ejemplar") -> None:
        from Biblio.Books.estado_disponible import EstadoDisponible
        print(f"Info: El ejemplar {ejemplar.codigo_barras} está en taller. Se repara y pasa a Disponible.")
        ejemplar.estado = EstadoDisponible()

    def obtener_nombre(self) -> str:
        return "En Reparación"