from Biblio.People.Usuario import Usuario
from Biblio.Exceptions import Exceptions

#Clase login que gestiona la autenticación de los usuarios en el sistema.
class Login:
    def __init__(self):
     self.usuarios = []  # Lista de usuarios registrados
     self.usuario_activo = None  # Usuario que esta logueado


#Metodo para registrar un nuevo usuario en el sistema.
    def registrar_usuario(self, usuario: Usuario):
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.username}' registrado correctamente.")

#Metodo para iniciar sesion corroborando con usuario y contraseña.
def iniciar_sesion(self, username, password):
   for usuario in self.usuarios:
      if usuario.username == username and usuario.password ==password:
         self.usuario_activo = usuario
         print(f"Bienvenido, {usuario.obtener_nombre_completo()}!")
         return True
      else:
         raise Exceptions(110) # Usuario o contraseña incorrectos. Por favor, intente nuevamente.
   raise Exceptions(111) # Usuario no encontrado. Por favor, registrese o intente con otro usuario.
   
#Metodo para cerrar la sesion del usuario activo.
def cerrar_sesion(self):
   if self.usuario_activo:
      print(f"Hasta luego, {self.usuario_activo.obtener_nombre_completo()}!")
      self.usuario_activo = None
   else:
      print("No hay ningun usuario logueado.")