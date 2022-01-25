class Persona:
    def __init__(self, cedula, fechanacimiento):
        self.cedula = cedula
        self.fechanacimiento = fechanacimiento
        self.vacunas = []
        self.nombre = ""
        self.idencrypt = ""
        self.url = ""

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def idencrypt(self):
        return self.__idencrypt
    @idencrypt.setter
    def idencrypt(self, id):
        self.__idencrypt = id

    @property
    def url(self):
        return self.__url
    @url.setter
    def url(self, url):
        self.__url = url

    def agregarVacuna(self, vacuna):
        self.vacunas.append(vacuna)

    def __repr__(self):
        return f"<{self.nombre} ({self.cedula}) {self.vacunas} {self.idencrypt}>"
