class Adopcion:
    def __init__(self,id_adopcion,mascota,adoptante,fecha):
        if not isinstance(mascota,Mascota):
            raise FormatoMascota("La mascota ingresada no pertenece a la clase Mascota")
        self.id_adopcion=id_adopcion
        self.mascota=mascota
        self.adoptante=adoptante
        self.fecha=fecha
    def __str__(self):
        return f"{self.id_adopcion},{self.mascota.nombre},{self.adoptante.nombre},{self.estado}"
    def confirmar(self):
        if self.mascota.estado!="disponible":
            raise MascotaNoDisponible(f"La mascota {self.mascota.nombre} no está disponible para ser adoptada")
        if self.adoptante.edad<18:
            raise Exception(f"El adoptante {self.adoptante.nombre} debe ser mayor de 18 años para adoptar.")
        self.estado="confirmada"
        self.mascota.marcar_adoptado()
        self.adoptante.registrar_adopcion(self)
    def cancelar(self):
        self.estado="cancelada"
        if self.mascota.estado=="adoptado":
            self.mascota.marcar_disponible()