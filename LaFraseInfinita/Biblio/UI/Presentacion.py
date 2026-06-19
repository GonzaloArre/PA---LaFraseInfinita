import os
import sys
import time

class PresentacionBiblioteca:
    def __init__(self, velocidad_tipeo=0.03, delay_pausa=1.0):
        """
        Gestiona la interfaz estética, banners y animaciones de consola
        diseñadas específicamente para el ecosistema 'La Frase Infinita'.
        """
        self.velocidad = velocidad_tipeo
        self.delay = delay_pausa

    def limpiar(self):
        """Limpia la terminal de forma multiplataforma."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def escribir(self, texto: str, nueva_linea=True, velocidad_custom=None):
        """Efecto máquina de escribir (typewriter) para los textos."""
        vel = velocidad_custom if velocidad_custom is not None else self.velocidad
        for caracter in texto:
            sys.stdout.write(caracter)
            sys.stdout.flush()
            time.sleep(vel)
        if nueva_linea:
            print()

    def mostrar_banner_ascii(self):
        """Despliega un diseño moderno de bloques que no se deforma."""
        print(" ╔══════════════════════════════════════════════════════════════════╗")
        print(" ║  ██╗      █████╗      ███████╗██████╗  █████╗ ███████╗███████╗   ║")
        print(" ║  ██║     ██╔══██╗     ██╔════╝██╔══██╗██╔══██╗██╔════╝██╔════╝   ║")
        print(" ║  ██║     ███████║     █████╗  ██████╔╝███████║███████╗█████╗     ║")
        print(" ║  ██║     ██╔══██║     ██╔══╝  ██╔══██╗██╔══██║╚════██║██╔══╝     ║")
        print(" ║  ███████╗██║  ██║     ██║     ██║  ██║██║  ██║███████║███████╗   ║")
        print(" ║  ╚══════╝╚═╝  ╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝   ║")
        print(" ║                                                                  ║")
        print(" ║                ═══  I N F I N I T A  ═══                         ║")
        print(" ╚══════════════════════════════════════════════════════════════════╝")

    def ejecutar_secuencia_carga(self):
        """Simula la apertura de los archivos de la biblioteca, tomos y JSON."""
        self.limpiar()
        print("[SISTEMA]: Conectando con los archivos de la Biblioteca...")
        time.sleep(0.4)
        
        self.escribir(" > Indexando catálogos de manuscritos...", velocidad_custom=0.02)
        self.escribir(" > Consultando registro de lectores persistidos... OK", velocidad_custom=0.02)
        
        time.sleep(self.delay)

    def mostrar_introduccion(self):
        """Secuencia conceptual de bienvenida literaria."""
        self.limpiar()
        self.mostrar_banner_ascii()
        print("\n")
        
        # Frase mística sobre el conocimiento continuo
        self.escribir(" \"Donde las palabras fluyen...", velocidad_custom=0.05)
        self.escribir("  en el silencio de un archivo.\"", velocidad_custom=0.05)
        time.sleep(0.6)

    def mostrar_despedida(self, usuario=None):
        """Animación de cierre al abandonar el sistema de lectura."""
        self.limpiar()
        self.escribir(" -> Cerrando tomos y asegurando estanterías virtuales... OK", velocidad_custom=0.03)
        self.escribir(" -> Devolviendo la terminal al silencio del archivo. Hasta luego. 📚", velocidad_custom=0.04)
        print("====================================================================")
        time.sleep(1.2)
        self.limpiar()