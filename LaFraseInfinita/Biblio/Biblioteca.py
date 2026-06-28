from .Catalogo import Catalogo
from .People.Socio import Socio
from .Prestamo import Prestamo
from .Exceptions import Exceptions

#Metaclase que registra automaticamente cuando se crea una clase del sistema.
class MetaBiblioteca(type):
    def __new__(cls, nombre, bases, atributos):
        print(f"Creando clase: {nombre}")
        return super().__new__(cls, nombre, bases, atributos)

#Decorador que verifica que haya un usuario logueado antes de ejecutar una accion.
def requiere_login(funcion):
        def verificar(self,*args, **kwargs):
            if self.login.usuario_actual is None:
                raise Exceptions(112) #Lanza una excepcion si no hay un usuario logueado
            return funcion(self, *args, **kwargs)
        return verificar

class Biblioteca(metaclass=MetaBiblioteca):
    def __init__(self,nombre):
        self.nombre = nombre
        self.catalogo = Catalogo() # Composicion: Biblioteca tiene un Catalogo
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

    def registrar_socio(self, socio):
        Socio.agregar_socio(socio)
    
    def buscar_socio(self, dni):
        return Socio.buscar(dni)

    def eliminar_socio(self, dni):
        Socio.eliminar_socio(dni)

    def listar_socios(self):
        Socio.listar_socios()

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
