import json
import os
from datetime import date
from .Books.ejemplar import Ejemplar
from .People.Socio import Socio


# Clase Prestamo que representa el préstamo de un Ejemplar a un Socio y el registro de fechas de préstamo y devolución.
class Prestamo:
    def __init__(self, ejemplar: Ejemplar, socio: Socio, fecha_devolucion=None):
        self.ejemplar = ejemplar
        self.socio = socio
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = fecha_devolucion
        self.activo = False

    # Método para mostrar la información del préstamo.
    def __str__(self):

        devolucion = (
            self.fecha_devolucion.isoformat()
            if isinstance(self.fecha_devolucion, date)
            else self.fecha_devolucion
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
            f"  Estado: {'Activo' if self.esta_activo() else 'Finalizado'}"
        )

    #Método par registrar un prestamo
    def registrar_prestamo(self):
        estado_anterior = self.ejemplar.estado if self.ejemplar is not None else None

        try:
            # El estado del ejemplar decide si se puede prestar o no.
            estado_actual = self.ejemplar.estado
            estado_actual.prestar(self.ejemplar)
            self.activo = self.ejemplar is not None and self.ejemplar.estado.__class__.__name__ == "EstadoPrestado"

            ruta_archivo = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "Files", "prestamos.json")
            )
            os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)

            if os.path.exists(ruta_archivo):
                with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                    try:
                        prestamos = json.load(archivo)
                    except json.JSONDecodeError:
                        prestamos = []
            else:
                prestamos = []

            fecha_devolucion = None
            if isinstance(self.fecha_devolucion, date):
                fecha_devolucion = self.fecha_devolucion.isoformat()
            elif self.fecha_devolucion:
                fecha_devolucion = str(self.fecha_devolucion)

            prestamos.append({
                "codigo_barras": self.ejemplar.codigo_barras,
                "socio_dni": self.socio.dni,
                "fecha_prestamo": self.fecha_prestamo.isoformat(),
                "fecha_devolucion": fecha_devolucion,
                "activo": True,
            })

            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(prestamos, archivo, indent=4, ensure_ascii=False)

            return True
        except Exception:
            if self.ejemplar is not None and estado_anterior is not None:
                self.ejemplar.estado = estado_anterior
            raise

    # Método para registrar la devolución del libro
    def registrar_devolucion(self):
        if not self.activo:
            raise Exception("Este préstamo ya fue cerrado")

        self.fecha_devolucion = date.today()
        self.activo = False

        # El ejemplar vuelve a estar disponible.
        if self.ejemplar is not None:
            self.ejemplar.devolver()

        # Actualizar también el estado del préstamo en el archivo JSON
        ruta_archivo = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "Files", "prestamos.json")
        )

        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                try:
                    prestamos = json.load(archivo)
                except json.JSONDecodeError:
                    prestamos = []

            for prestamo_data in prestamos:
                if prestamo_data.get("codigo_barras") == self.ejemplar.codigo_barras and prestamo_data.get("activo"):
                    prestamo_data["activo"] = False
                    prestamo_data["fecha_devolucion"] = self.fecha_devolucion.isoformat()
                    break

            with open(ruta_archivo, "w", encoding="utf-8") as archivo:
                json.dump(prestamos, archivo, indent=4, ensure_ascii=False)

    def esta_activo(self):
        return self.activo and self.ejemplar is not None and self.ejemplar.estado.__class__.__name__ == "EstadoPrestado"
