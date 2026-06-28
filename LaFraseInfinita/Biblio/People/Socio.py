import json
import os
from .Persona import Persona
from ..Exceptions import Exceptions

# Ruta única para el archivo de socios dentro del paquete Biblio
DB_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "Files", "socios.json"))

# Clase Socio hijo de Persona
class Socio(Persona):
    def __init__(self, nombre, apellido, fec_nac, tel, mail, dni, direccion):
        super().__init__(nombre, apellido, fec_nac)
        self.tel = tel
        self.mail = mail
        self.dni = dni
        self.direccion = direccion

    # Permite usar una instancia de Socio para agregarse al sistema
    def agregar(self):
        Socio.agregar_socio(self)
    
    # Permite usar una instancia de Socio para eliminarse del sistema
    def eliminar(self):
        Socio.eliminar_socio(self.dni)
    
    
    # Método para agregar un socio a la biblioteca.
    @staticmethod
    def agregar_socio(socio):
        # Asegura existencia del archivo en la ruta del paquete y carga con tolerancia a JSON vacío
        if not os.path.exists(os.path.dirname(DB_PATH)):
            os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        if not os.path.exists(DB_PATH):
            with open(DB_PATH, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, ensure_ascii=False, indent=4)
        with open(DB_PATH, "r", encoding="utf-8") as archivo:
            try:
                socios = json.load(archivo)
            except json.JSONDecodeError:
                socios = []
        socios.append({
            "nombre": socio.nombre,
            "apellido": socio.apellido,
            "fec_nac": socio.fec_nac,
            "tel": socio.tel,
            "mail": socio.mail,
            "dni": socio.dni,
            "direccion": socio.direccion
        })
        with open(DB_PATH, "w", encoding="utf-8") as archivo:
            json.dump(socios, archivo, indent=4, ensure_ascii=False)

    # Método para eliminar un socio de la biblioteca.
    @staticmethod
    def eliminar_socio(dni):
        if not os.path.exists(DB_PATH):
            return
        with open(DB_PATH, "r", encoding="utf-8") as archivo:
            try:
                socios = json.load(archivo)
            except json.JSONDecodeError:
                socios = []
        encontrados = [socio for socio in socios if socio["dni"] == dni]
        if not encontrados:
            raise Exceptions(111)
        socios = [socio for socio in socios if socio["dni"] != dni]
        with open(DB_PATH, "w", encoding="utf-8") as archivo:
            json.dump(socios, archivo, indent=4, ensure_ascii=False)

    # Método para listar todos los socios de la biblioteca.
    @staticmethod
    def listar_socios():
        if not os.path.exists(DB_PATH):
            print("No hay socios registrados.")
            return
        with open(DB_PATH, "r", encoding="utf-8") as archivo:
            try:
                socios = json.load(archivo)
            except json.JSONDecodeError:
                socios = []
        if not socios:
            print("No hay socios registrados.")
            return
        for socio in socios:
            print(f"Nombre: {socio['nombre']} {socio['apellido']}, DNI: {socio['dni']}")

    @staticmethod
    def buscar(dni):
        if not os.path.exists(DB_PATH):
            return None
        with open(DB_PATH, "r", encoding="utf-8") as archivo:
            try:
                socios = json.load(archivo)
            except json.JSONDecodeError:
                socios = []
        for socio in socios:
            if socio["dni"] == dni:
                return Socio(
                    socio["nombre"],
                    socio["apellido"],
                    socio["fec_nac"],
                    socio["tel"],
                    socio["mail"],
                    socio["dni"],
                    socio["direccion"]
                )
        return None

    # Método para modificar los atributos del socio.
    def modificar(self, nombre=None, apellido=None, fec_nac=None, tel=None, mail=None, direccion=None):
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
        if direccion:
            self.direccion = direccion
        print(f"Socio modificado: {self.get_nombre_completo()}, {self.fec_nac}, {self.tel}, {self.mail}, {self.direccion}")

    # Método str de Socio.
    def __str__(self):
        return f"Socio: {self.get_nombre_completo()}, Nacimiento: {self.fec_nac}, Tel: {self.tel}, Mail: {self.mail}, DNI: {self.dni}, Dirección: {self.direccion}"