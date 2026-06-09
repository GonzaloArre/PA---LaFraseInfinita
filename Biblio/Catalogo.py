from Biblio.Libros.Libro import Libro

#Clase Catalogo que gestiona la coleccion de libros de la biblioteca.
class Catalogo:
    def __init__(self):
     self.libros = []  #Lista donde se guardan todos los libros

#Metodo para agregar un libro al catalogo.
    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado al catalogo.")

#Metodo para eliminar un libro del catalogo por su ISBN.
def eliminar_libro(self,isbn):
    for libro in self.libros:
        if libro.ISBN == isbn:
            self.libros.remove(libro)
            print(f"Libro con ISBN '{isbn}' eliminado del catalogo.")
            return
    print(f"No se encontro ningun libro con ISBN {isbn}.")
    
#Metodo para buscar un libro por su ISBN.
def buscar_libro(self,isbn):
    for libro in self.libros:
        if libro.ISBN == isbn:
            return libro
    print(f"No se encontro ningun libro con ISBN {isbn}.")
    return None

#Metodo para listar todos los libros del catalogo.
def listar_libros(self):
    if not self.libros:
        print("El catalogo esta vacio")
        return
    for libro in self.libros:
        print(libro)