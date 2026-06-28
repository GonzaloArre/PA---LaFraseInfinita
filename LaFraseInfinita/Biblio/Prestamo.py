from datetime import date
from .Books.ejemplar import Ejemplar
from .People.Socio import Socio


# Clase Prestamo que representa el préstamo de un Ejemplar a un Socio y el registro de fechas de préstamo y devolución.
class Prestamo:
    def __init__(self, ejemplar: Ejemplar, socio: Socio):
        self.ejemplar = ejemplar
        self.socio = socio
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None
        self.activo = True

# Método para mostrar la información del préstamo.
    def __str__(self):

        devolucion = (
            self.fecha_devolucion
            if self.fecha_devolucion
            else "Pendiente"
        )

        return (
            f"Préstamo:\n"
            f"  Libro: {self.ejemplar.libro.title}\n"
            f"  Código: {self.ejemplar.codigo_barras}\n"
            f"  Socio: {self.socio.get_nombre_completo()}\n"
            f"  Fecha préstamo: {self.fecha_prestamo}\n"
            f"  Fecha devolución: {devolucion}\n"
            f"  Estado: {'Activo' if self.activo else 'Finalizado'}"
        )

    # Método para registrar la devolución del libro
    def registrar_devolucion(self):
        if not self.activo:
            raise Exception("Este préstamo ya fue cerrado")
            
        self.fecha_devolucion = date.today()
        self.activo = False

        # El ejemplar vuelve a estar disponible.
        self.ejemplar.devolver()

    # Método para verificar si el préstamo está activo.
    def esta_activo(self):
        return self.activo
    
