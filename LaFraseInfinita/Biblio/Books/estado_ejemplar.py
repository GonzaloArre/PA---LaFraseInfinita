from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .ejemplar import Ejemplar

class EstadoEjemplar(ABC):
    estado = "Sin estado"

    @abstractmethod
    def prestar(self, ejemplar: "Ejemplar") -> None:
        """Define la acción de prestar según el estado actual."""
        pass

    @abstractmethod
    def devolver(self, ejemplar: "Ejemplar") -> None:
        """Define la acción de devolver según el estado actual."""
        pass

    def obtener_estado(self) -> str:
        """Devuelve el nombre legible del estado."""
        return self.estado

    def obtener_nombre(self) -> str:
        """Compatibilidad con el código que espera un método de nombre."""
        return self.obtener_estado()

