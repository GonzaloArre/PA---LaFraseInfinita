# estado_disponible.py
from typing import TYPE_CHECKING
from Biblio.Books.estado_ejemplar import EstadoEjemplar

if TYPE_CHECKING:
    from Biblio.Books.ejemplar import Ejemplar

class EstadoDisponible(EstadoEjemplar):
    def prestar(self, ejemplar: "Ejemplar") -> None:
        from Biblio.Books.estado_prestado import EstadoPrestado
        print(f"Éxito: El ejemplar {ejemplar.codigo_barras} ha sido prestado.")
        ejemplar.estado = EstadoPrestado()  # Transición de estado

    def devolver(self, ejemplar: "Ejemplar") -> None:
        print(f"Info: El ejemplar {ejemplar.codigo_barras} ya estaba disponible en estantería.")

    def obtener_nombre(self) -> str:
        return "Disponible"