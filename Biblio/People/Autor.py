from Persona import Persona
# Autor hereda de Persona, agregando atributos específicos como seudónimo y nacionalidad.
class Autor(Persona):
    def __init__(self, nombre, apellido, fec_nac, seudonimo, nacionalidad):
        super().__init__(nombre, apellido, fec_nac)
        self.seudonimo = seudonimo
        self.nacionalidad = nacionalidad

    # Método str de Autor.    
    def __str__(self):
        return f"Autor: {self.get_nombre_completo()}, Nacimiento: {self.fec_nac}, Seudónimo: {self.seudonimo}, Nacionalidad: {self.nacionalidad}"