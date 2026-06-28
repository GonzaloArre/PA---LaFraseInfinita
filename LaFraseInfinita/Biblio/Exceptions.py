class Exceptions(Exception):

    ERRORS = {
        110: "Error 110: No hay socios registrados en la biblioteca.",
        111: "Error 111: No se encontró un socio con ese DNI.",
        210: "Error 210: No se a encontrado ningun libro con ese codigo. Por favor, verifique el codigo e intente nuevamente.",
        310: "Error 310: El ejemplar ya tiene un préstamo activo.",
        311: "Error 311: El ejemplar se encuentra en reparación y no puede ser prestado.",
        410: "Error 410: El catalogo esta vacio en estos momentos."
    }

    def __init__(self, error_code: int):
        self.error_code = error_code
        self.message = self.ERRORS.get(error_code, "Error desconocido.")
        super().__init__(f"{self.error_code}: {self.message}")

