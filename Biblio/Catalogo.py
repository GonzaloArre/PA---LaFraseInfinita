from Biblio.Books.ejemplar import Ejemplar

#Clase Catalogo que gestiona la coleccion de ejemplares de la biblioteca.
class Catalogo:
    def __init__(self):
        self.ejemplares = []  #Lista donde se guardan todos los ejemplares

#Metodo para agregar un ejemplar al catalogo.
    def agregar_ejemplar(self, ejemplar: Ejemplar):
        self.ejemplares.append(ejemplar)
        print(f"Ejemplar '{ejemplar.libro.titulo}' agregado al catalogo.")

#Metodo para eliminar un ejemplar del catalogo por su codigo de barras.
    def eliminar_ejemplar(self, codigo_barras):
     for ejemplar in self.ejemplares:
        if ejemplar.codigo_barras == codigo_barras:
            self.ejemplares.remove(ejemplar)
            print(f" Ejemplar '{codigo_barras}' eliminado del catalogo.")
            return
     print(f"No se encontro ningun ejemplar con codigo {codigo_barras}.")
    
#Metodo para buscar un ejemplar por su codigo de barras.
    def buscar_ejemplar(self, codigo_barras):
     for ejemplar in self.ejemplares:
        if ejemplar.codigo_barras == codigo_barras:
         return ejemplar
     print(f"No se encontro ningun ejemplar con codigo {codigo_barras}.")
     return None

#Metodo para listar todos los ejemplares del catalogo.
    def listar_ejemplares(self):
     if not self.ejemplares:
        return print("El catalogo esta vacio")   
     for ejemplar in self.ejemplares:
        print(ejemplar)