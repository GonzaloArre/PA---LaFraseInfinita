# estado_prestado.py
from Biblio.Exceptions import Exceptions
from typing import TYPE_CHECKING
from Biblio.Books.estado_ejemplar import EstadoEjemplar

if TYPE_CHECKING:
    from Biblio.Books.ejemplar import Ejemplar

class EstadoPrestado(EstadoEjemplar):
    def prestar(self, ejemplar: "Ejemplar") -> None:
        raise Exceptions(310)  # El ejemplar ya tiene un préstamo activo.

    def devolver(self, ejemplar: "Ejemplar") -> None:
        from Biblio.Books.estado_disponible import EstadoDisponible
        print(f"Éxito: El ejemplar {ejemplar.codigo_barras} fue devuelto con éxito.")
        ejemplar.estado = EstadoDisponible()  # Transición de estado

    def obtener_nombre(self) -> str:
        return "Prestado"