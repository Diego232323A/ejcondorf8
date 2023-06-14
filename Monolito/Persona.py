class Persona():

    def __init__(self, id_persona=None, nombre=None, apellido=None, email=None):
        self._id_persona = id_persona
        self._nombre = nombre
        self._apellido = apellido
        self._email = email


    def __str__(self) -> str:
        return f'Hola esto es una prueba {self._apellido}+{self._nombre}+{self._email}'
    @property
    def id_persona(self):
        return self._id_persona
    @property
    def nombre(self):
        return self._nombre
    @property
    def apellido(self):
        return self._apellido
    @property
    def email(self):
        return self._email


