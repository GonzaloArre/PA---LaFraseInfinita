from Biblio.Biblioteca import Biblioteca
from Biblio.UI.presentacion import PresentacionBiblioteca
from Biblio.UI.menu import Menu

def main():

    biblioteca = Biblioteca("La Frase Infinita")

    interfaz = PresentacionBiblioteca()

    interfaz.ejecutar_secuencia_carga()
    interfaz.mostrar_introduccion()

    menu = Menu(biblioteca)
    menu.ejecutar()

    interfaz.mostrar_despedida()

if __name__ == "__main__":
    main()
