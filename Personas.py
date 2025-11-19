class Persona:
    def __init__(self,nombre,cedula,email,edad):
        self.nombre=nombre
        self.cedula=cedula
        self.email=email
        self.edad=edad
    def __str__(self):
        return f"{self.cedula},{self.nombre}"
class Adoptante(Persona):
    def __init__(self,nombre,cedula,email,edad):
        super().__init__(nombre,cedula,email,edad)
        self.adopciones=[]
    def registrar_adopcion(self,adopcion):
        if self.edad<18:
            raise MenorEdad(f"El adoptante {self.nombre} es menor de edad.")
        self.adopciones.append(adopcion)
    def __str__(self):
        return f"Adoptante:{self.cedula},{self.nombre}"
class Trabajador(Persona):
    def __init__(self,nombre,cedula,email,edad,cargo):
        super().__init__(nombre,cedula,email,edad)
        self.cargo=cargo
        self.tareas=[]
    def asignar_tarea(self,tarea):
        self.tareas.append(tarea)
    def __str__(self):
        return f"Trabajador:{self.cedula},{self.nombre}"
    