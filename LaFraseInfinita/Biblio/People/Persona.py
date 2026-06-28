from abc import ABC, abstractmethod
# Clase abstracta Persona que define los atributos y metodos comunes para Socio, Autor y Usuario.
class Persona(ABC):
    def __init__(self, nombre, apellido, fec_nac):
        self.nombre = nombre
        self.apellido = apellido
        self.fec_nac = fec_nac

    @abstractmethod
    def agregar(self):
        pass

    @abstractmethod
    def eliminar(self):
        pass
    
    # Método para obtener el nombre completo de la persona.
    def get_nombre_completo(self):
        return f"{self.nombre}, {self.apellido}"