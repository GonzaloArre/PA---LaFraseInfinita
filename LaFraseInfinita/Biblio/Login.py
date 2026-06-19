import json
import os
import hashlib
import pwinput
from Biblio.People.Usuario import Usuario
from Biblio.Exceptions import Exceptions

class Login:
    USUARIOS_DB = 'usuarios.json'

    def __init__(self):
        self.usuario_activos_memoria = self._cargar_usuarios_locales() # Mapeo username -> hash para validación rápida
        self.usuario_activo = None  # Instancia de Objeto Usuario que está logueado

    # Métodos privados para manejo interno de usuarios y contraseñas
    def _encriptar_contrasena(self, contrasena: str) -> str:
        #Aplica el algoritmo SHA-256 para transformar la contraseña en un hash
        return hashlib.sha256(contrasena.encode('utf-8')).hexdigest()

    def _cargar_usuarios_locales(self) -> dict:
        #Carga el diccionario {username: hash} desde el JSON
        if not os.path.exists(self.USUARIOS_DB):
            with open(self.USUARIOS_DB, 'w', encoding='utf-8') as f:
                json.dump({}, f)
            return {}
        with open(self.USUARIOS_DB, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _guardar_usuarios_locales(self, datos_usuarios: dict):
        #Guarda el diccionario actualizado en el archivo JSON
        with open(self.USUARIOS_DB, 'w', encoding='utf-8') as f:
            json.dump(datos_usuarios, f, indent=4)

    # Métodos Públicos de la Clase Login para interacción con el sistema
    def registrar_usuario(self, usuario: Usuario):
        #Registra un nuevo objeto Usuario, encripta su clave y lo persiste en el JSON
        datos_json = self._cargar_usuarios_locales()
        
        if usuario.username in datos_json:
            print(f"El usuario '{usuario.username}' ya se encuentra registrado.")
            return False
            
        # Encriptamos la contraseña del objeto antes de guardarla en el JSON
        datos_json[usuario.username] = self._encriptar_contrasena(usuario.password)
        self._guardar_usuarios_locales(datos_json)
        
        print(f"Usuario '{usuario.username}' registrado correctamente en la base de datos.")
        return True

    def iniciar_sesion(self):
        #Gestiona el bucle de autenticación interrumpiendo con excepciones según corresponda
        datos_json = self._cargar_usuarios_locales()
        if not datos_json:
            print("No hay usuarios registrados en el sistema.")
            return False

        while True:
            username = input("Ingrese su nombre de usuario: ").strip()
            password = pwinput.pwinput("Ingrese su contraseña: ", mask="*")
            
            # 1. Validación de existencia de usuario
            if username not in datos_json:
                raise Exceptions(111) # Usuario no encontrado.
                
            # 2. Validación de contraseña (comparando hashes)
            password_encriptada = self._encriptar_contrasena(password)
            if datos_json[username] == password_encriptada:
                # Se instancia temporalmente al usuario activo
                self.usuario_activo = Usuario(username, password) 
                print(f"\nInicio de sesión exitoso. ¡Bienvenido, {self.usuario_activo.obtener_nombre_completo()}!")
                return True
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                raise Exceptions(110) # Usuario o contraseña incorrectos.

    def cambiar_contrasena(self):
        #Permite al usuario actualmente logueado modificar su contraseña en el JSON
        if not self.usuario_activo:
            print("Debe iniciar sesión para cambiar la contraseña.")
            return False

        username = self.usuario_activo.username
        datos_json = self._cargar_usuarios_locales()

        print(f"\n--- Modificando contraseña del usuario: {username} ---")
        
        coinciden = False
        while not coinciden:
            nueva_contrasena = pwinput.pwinput("Ingrese su NUEVA contraseña: ", mask="*")
            confirmar_contrasena = pwinput.pwinput("Confirme su NUEVA contraseña: ", mask="*")
            
            if nueva_contrasena == confirmar_contrasena:
                coinciden = True
            else:
                print("Las contraseñas no coinciden. Intente de nuevo.\n")
                
        # Actualizamos tanto el JSON como la instancia en memoria
        datos_json[username] = self._encriptar_contrasena(nueva_contrasena)
        self._guardar_usuarios_locales(datos_json)
        self.usuario_activo.password = nueva_contrasena 
        
        print("¡Contraseña modificada con éxito!")
        return True

    def cerrar_sesion(self):
        # Limpia el estado del usuario activo
        if self.usuario_activo:
            print(f"Hasta luego, {self.usuario_activo.obtener_nombre_completo()}!")
            self.usuario_activo = None
        else:
            print("No hay ningún usuario logueado.")