class Libro:
    def __init__(self, title, isbn, anio_pub, pag):
        self.title = title
        self.autor = []
        self.isbn = isbn
        self.anio_pub = anio_pub
        self.pag = pag
    
    def agregar_autor(self, autor):
        self.autor.append(autor)