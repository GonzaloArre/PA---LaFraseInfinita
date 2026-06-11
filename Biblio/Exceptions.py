class Exceptions(Exception):

    ERRORS = {
        110: "Error 110: Usuario o contraseña incorrectos. Por favor, intente nuevamente.",
        111: "Error 111: Usuario no encontrado. Por favor, registrese o intente con otro usuario.",
        112: "Error 112: Debes iniciar sesión para realizar esta acción.",
        210: "Error 210: No se a encontrado ningun libro con ese codigo. Por favor, verifique el codigo e intente nuevamente.",
        310: "Error 310: El ejemplar ya tiene un préstamo activo.",
        311: "Error 311: El ejemplar se encuentra en reparación y no puede ser prestado.",
        410: "Error 410: El catalogo esta vacio en estos momentos."
    }

    def __init__(self, error_code: int):
        self.error_code = error_code
        self.message = self.ERRORS.get(error_code, "Error desconocido.")
        super().__init__(f"{self.error_code}: {self.message}")

