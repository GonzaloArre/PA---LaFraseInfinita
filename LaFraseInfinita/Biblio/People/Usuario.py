class Usuario:
    """
    Representa un usuario del sistema con credenciales de acceso.
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def agregar(self):
        print(f"Usuario '{self.username}' agregado al sistema.")

    def obtener_nombre_completo(self):
        return self.username

    def __str__(self):
        return f"Usuario: {self.username}"
