from Libro import Libro
from Usuario import Usuario
from datetime import date

# Clase Prestamo que representa el préstamo de un Libro a un Socio y el registro de fechas de préstamo y devolución.
class Prestamo:
    def __init__(self, libro: Libro, usuario: Usuario):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None
        self.activo = True

    # Método str de Prestamo.
    def __str__(self):
        devolucion = self.fecha_devolucion or "Pendiente"
        return (f"Préstamo: {self.libro.title} → {self.usuario.name} | "
                f"Desde: {self.fecha_prestamo} | Devolución: {devolucion}")

    # Método para registrar la devolución del libro, marcando el préstamo como inactivo y registrando la fecha de devolución.
    def registrar_devolucion(self):
        if not self.activo:
            raise Exception("Este préstamo ya fue cerrado")
        self.fecha_devolucion = date.today()
        self.activo = False
        self.libro.devolver()  # avisa al libro que quedó libre

    # Método para verificar si el préstamo está activo.
    def esta_activo(self):
        return self.activo
    