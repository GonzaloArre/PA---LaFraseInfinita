from Persona import Persona

# Clase Socio hijo de Persona
class Socio(Persona):
    def __init__(self, nombre, apellido, fec_nac, tel, mail, dni, direccion):
        super().__init__(nombre, apellido, fec_nac)
        self.tel = tel
        self.mail = mail
        self.dni = dni
        self.direccion = direccion

    # Método para modificar los atributos del socio.
    def modificar(self, nombre=None, apellido=None, fec_nac=None, tel=None, mail=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if fec_nac:
            self.fec_nac = fec_nac
        if tel:
            self.tel = tel
        if mail:
            self.mail = mail
        print(f"Socio modificado: {self.get_nombre_completo()}, {self.fec_nac}, {self.tel}, {self.mail}")

    # Método str de Socio.
    def __str__(self):
        return f"Socio: {self.get_nombre_completo()}, Nacimiento: {self.fec_nac}, Tel: {self.tel}, Mail: {self.mail}, DNI: {self.dni}, Dirección: {self.direccion}"