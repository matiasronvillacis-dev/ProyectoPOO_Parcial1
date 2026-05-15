# Integrantes:
# Ambar Barrera
# Jesus Valencia
# Mayerly Reyes
# Matías Ron
# Cecilia Jacome

class Cliente:

    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if valor == "":
            print("El nombre no puede estar vacío")
            return
        self._nombre = valor

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        if valor == "":
            print("El teléfono no puede estar vacío")
            return
        self._telefono = valor

    def __str__(self):
        return f"{self._nombre} - {self._telefono}"