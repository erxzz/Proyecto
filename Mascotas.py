class Mascota:
    def __init__(self,id_mascota,nombre,edad,estado):
        self.id_mascota=id_mascota
        self.nombre=nombre
        self.edad=edad
        self.estado=estado
    def __str__(self):
        return f"{self.nombre} {self.edad}"
    def marcar_adoptado(self):
        self.estado="adoptado"
    def marcar_disponible(self):
        self.estado="disponible"
    def en_tratamiento(self):
        self.estado="en_tratamiento"
class Perro(Mascota):
    def __init__(self,id_mascota,nombre,edad,raza,estado):
        super().__init__(id_mascota,nombre,edad,estado)
        self.raza=raza
    def __str__(self):
        return f"Perro:{self.nombre};Raza:{self.raza},{self.edad}/Estado:{self.estado}"
class Gato(Mascota):
    def __init__(self,id_mascota,nombre,edad,color,estado):
        super().__init__(id_mascota,nombre,edad,estado)
        self.color=color
    def __str__(self):
        return f"Gato:{self.nombre};Color:{self.color},{self.edad}/Estado:{self.estado}"
class Otro(Mascota):
    def __init__(self,id_mascota,nombre,especie,edad,estado):
        super().__init__(id_mascota,nombre,edad,estado)
        self.especie=especie
    def __str__(self):
        return f"{self.especie}:{self.nombre};{self.edad} /Estado:{self.estado}"