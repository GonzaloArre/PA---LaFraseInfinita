from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Biblio.Books.ejemplar import Ejemplar

class EstadoEjemplar(ABC):
    
    @abstractmethod
    def prestar(self, ejemplar: "Ejemplar") -> None:
        """Define la acción de prestar según el estado actual."""
        pass

    @abstractmethod
    def devolver(self, ejemplar: "Ejemplar") -> None:
        """Define la acción de devolver según el estado actual."""
        pass

    @abstractmethod
    def obtener_nombre(self) -> str:
        """Devuelve el nombre legible del estado."""
        pass

