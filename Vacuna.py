class Vacuna:
    def __init__(self, nombre, fecha, dosis):
        self.nombre = nombre
        self.fecha = fecha
        self.dosis = int(dosis)

    def __repr__(self):
        return f"<{self.dosis}: {self.nombre} ({self.fecha})>"
