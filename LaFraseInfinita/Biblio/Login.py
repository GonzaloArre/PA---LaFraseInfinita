import json
import os
import hashlib
import pwinput
from Biblio.People.Usuario import Usuario
from Biblio.Exceptions import Exceptions

class Login:
    # Archivo donde se guardan los usuarios registrados
    USUARIOS_DB = "usuarios.json"

    def __init__(self):
        # Diccionario en memoria con usuarios cargados desde el JSON
        self.usuarios_memoria = self._cargar_usuarios_locales()

        # Usuario actualmente logueado en el sistema
        self.usuario_activo = None

    # ==========================
    # MÉTODOS PRIVADOS
    # ==========================

    def _encriptar_contrasena(self, contrasena: str) -> str:
        # Convierte la contraseña en un hash SHA-256 para seguridad
        return hashlib.sha256(contrasena.encode("utf-8")).hexdigest()

    def _cargar_usuarios_locales(self) -> dict:
        # Carga usuarios desde el archivo JSON
        # Si no existe, lo crea vacío
        if not os.path.exists(self.USUARIOS_DB):
            with open(self.USUARIOS_DB, "w", encoding="utf-8") as archivo:
                json.dump({}, archivo)
            return {}

        with open(self.USUARIOS_DB, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    def _guardar_usuarios_locales(self, datos: dict):
        # Guarda el diccionario de usuarios en el JSON
        with open(self.USUARIOS_DB, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)

    # ==========================
    # MÉTODOS PÚBLICOS
    # ==========================

    def registrar_usuario(self, usuario: Usuario):
        # Registra un nuevo usuario en el sistema

        datos = self._cargar_usuarios_locales()

        # Verifica si el usuario ya existe
        if usuario.username in datos:
            print(f"El usuario '{usuario.username}' ya está registrado.")
            return False

        # Guarda la contraseña encriptada
        datos[usuario.username] = self._encriptar_contrasena(usuario.password)

        self._guardar_usuarios_locales(datos)

        print(f"Usuario '{usuario.username}' registrado correctamente.")

        return True

    def iniciar_sesion(self):
        # Inicia sesión validando usuario y contraseña

        datos = self._cargar_usuarios_locales()

        if not datos:
            print("No hay usuarios registrados en el sistema.")
            return False

        # Solicita credenciales
        username = input("Nombre de usuario: ").strip()
        password = pwinput.pwinput("Contraseña: ", mask="*")

        # Verifica existencia del usuario
        if username not in datos:
            raise Exceptions(111)

        # Encripta la contraseña ingresada
        password_hash = self._encriptar_contrasena(password)

        # Verifica contraseña
        if datos[username] != password_hash:
            raise Exceptions(110)

        # Crea el usuario activo en memoria
        self.usuario_activo = Usuario(username, password)

        print(f"\nInicio de sesión exitoso. Bienvenido {username}.")

        return True

    def cambiar_contrasena(self):
        # Permite cambiar la contraseña del usuario logueado

        if self.usuario_activo is None:
            raise Exceptions(112)

        datos = self._cargar_usuarios_locales()

        # Solicita nueva contraseña
        nueva = pwinput.pwinput("Nueva contraseña: ", mask="*")
        confirmar = pwinput.pwinput("Confirmar contraseña: ", mask="*")

        # Verifica coincidencia
        if nueva != confirmar:
            print("Las contraseñas no coinciden.")
            return False

        # Actualiza el JSON
        datos[self.usuario_activo.username] = self._encriptar_contrasena(nueva)

        self._guardar_usuarios_locales(datos)

        # Actualiza en memoria
        self.usuario_activo.password = nueva

        print("Contraseña modificada correctamente.")

        return True

    def cerrar_sesion(self):
        # Cierra la sesión actual

        if self.usuario_activo is None:
            print("No hay ningún usuario logueado.")
            return

        print(f"Hasta luego, {self.usuario_activo.username}.")

        self.usuario_activo = None
