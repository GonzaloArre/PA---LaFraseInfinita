from Biblio.People.Persona import Persona
#Clase Usuario que representa a un usuario del sistema con credenciales de acceso. Hereda de la clase Persona.

class Usuario(Persona):
    def __init__(self, nombre, apellido, fec_nac, username, password):
        super().__init__(nombre, apellido, fec_nac)
        self.username = username #Nombre de usuario para el login
        self.password = password #Contraseña para el login

#Metodo para registrar el usuario en el sistema.
    def agregar(self):
        print(f"Usuario {self.username} agregado al sistema.")

#Metodo str de Usuario para mostrar su informacion de manera legible.
    def __str__(self):
        return f"Usuario: {self.obtener_nombre_completo()} - Username: {self.username}"