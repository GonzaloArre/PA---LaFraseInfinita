from Biblio.Catalogo import Catalogo
from Biblio.login import Login
from Biblio.Prestamo import Prestamo

#Metaclase que registra automaticamente cuando se crea una clase del sistema.
class MetaBiblioteca(type):
    def __new__(cls, nombre, bases, atributos):
        print(f"Creando clase: {nombre}")
        return super().__new__(cls, nombre, bases, atributos)

#Decorador que verifica que haya un usuario logueado antes de ejecutar una accion.
def requiere_login(funcion):
        def verificar(self,*args, **kwargs):
            if self.login.usuario_actual is None:
                print("Debes iniciar sesión para realizar esta acción.")
                return
            return funcion(self, *args, **kwargs)
        return verificar

class Biblioteca(metaclass=MetaBiblioteca):
    def __init__(self,nombre):
        self.nombre = nombre
        self.catalogo = Catalogo() # Composicion: Biblioteca tiene un Catalogo
        self.login = Login() # Composicion: Biblioteca tiene un Login
        self.prestamo = [] #Lista de prestamos registrados

#Metodo para agregar un ejemplar al sistema
    def agregar_ejemplar(self, ejemplar):
        self.catalogo.agregar_ejemplar(ejemplar)
    
#Metodo para eliminar un ejemplar del sistema
    def eliminar_ejemplar(self, codigo_barras):
        self.catalogo.eliminar_ejemplar(codigo_barras)

#Metodo para listar todos los ejemplares
    def listar_ejemplares(self):
        self.catalogo.listar_ejemplares()

#Metodo para registrar un nuevo usuario
    def registrar_usuario(self,usuario):
        self.login.registrar_usuario(usuario)

#Metodo para iniciar sesion
    def iniciar_sesion(self, username, password):
        return self.login.iniciar_sesion(username, password)
    
#Metodo para cerrar sesion
    def cerrar_sesion(self):
        self.login.cerrar_sesion()

#Metodo para registrar un prestamo
    @requiere_login
    def registrar_prestamo(self,libro, socio):
        prestamo = Prestamo(libro, socio)
        self.prestamos.append(prestamo)
        print(f"Prestamo registrado: {prestamo}")
        return prestamo
    
#Metodo para registrar una devolucion
    def registrar_devolucion(self,prestamo):
        prestamo.registrar_devolucion()

#Metodo para listar prestamos activos
    @requiere_login
    def listar_prestamos_activos(self):
        activos = [prestamo for prestamo in self.prestamos if prestamo.esta_activo()]
        if not activos:
            print("No hay prestamos activos.")
            return
        for prestamo in activos:
            print(prestamo)
    