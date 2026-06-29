import json
import os
from .Books.ejemplar import Ejemplar
from .Books.Libro import Libro
from .Exceptions import Exceptions

#Clase Catalogo que gestiona la coleccion de ejemplares de la biblioteca.
class Catalogo:
    def __init__(self):
        self.db_path = os.path.join(os.path.dirname(__file__), "Files", "libros.json")
        self.ejemplares = self._cargar_ejemplares()

    def _cargar_ejemplares(self):
        if not os.path.exists(self.db_path):
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            with open(self.db_path, "w", encoding="utf-8") as archivo:
                json.dump([], archivo, indent=4, ensure_ascii=False)
            return []

        with open(self.db_path, "r", encoding="utf-8") as archivo:
            try:
                datos = json.load(archivo)
            except json.JSONDecodeError:
                datos = []

        ejemplares = []
        for item in datos:
            libro_data = item.get("libro", {})
            libro = Libro(
                libro_data.get("title", ""),
                libro_data.get("isbn", ""),
                libro_data.get("anio_pub", ""),
                libro_data.get("pag", ""),
            )
            for autor in libro_data.get("autor", []):
                libro.agregar_autor(autor)

            ejemplar = Ejemplar(item.get("codigo_barras", ""), libro)
            ejemplares.append(ejemplar)

        return ejemplares

    def _guardar_ejemplares(self):
        datos = []
        for ejemplar in self.ejemplares:
            datos.append({
                "codigo_barras": ejemplar.codigo_barras,
                "libro": {
                    "title": ejemplar.libro.title,
                    "isbn": ejemplar.libro.isbn,
                    "anio_pub": ejemplar.libro.anio_pub,
                    "pag": ejemplar.libro.pag,
                    "autor": ejemplar.libro.autor,
                },
            })

        with open(self.db_path, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

#Metodo para agregar un ejemplar al catalogo.
    def agregar_ejemplar(self, ejemplar: Ejemplar):
        self.ejemplares.append(ejemplar)
        self._guardar_ejemplares()
        print(f"Ejemplar '{ejemplar.libro.title}' agregado al catalogo.")

#Metodo para eliminar un ejemplar del catalogo por su codigo de barras.
    def eliminar_ejemplar(self, codigo_barras):
     for ejemplar in self.ejemplares:
        if ejemplar.codigo_barras == codigo_barras:
            self.ejemplares.remove(ejemplar)
            self._guardar_ejemplares()
            print(f" Ejemplar '{codigo_barras}' eliminado del catalogo.")
            return
     raise Exceptions(210) # Ejemplar no encontrado.

#Metodo para buscar un ejemplar por su codigo de barras.
    def buscar_ejemplar(self, codigo_barras):
     for ejemplar in self.ejemplares:
        if ejemplar.codigo_barras == codigo_barras:
         return ejemplar
     raise Exceptions(210) # Ejemplar no encontrado.

#Metodo para listar todos los ejemplares del catalogo.
    def listar_ejemplares(self):
     if not self.ejemplares:
        raise Exceptions(410) # El catalogo esta vacio en estos momentos.   
     for ejemplar in self.ejemplares:
        print(ejemplar.descripcion())