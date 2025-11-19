class CentroAdopcion:
    def __init__(self,nombre,mascotas,adoptantes,adopciones):
        self.nombre=nombre
        self.mascotas=mascotas
        self.adoptantes=adoptantes
        self.adopciones=adopciones
    def entrada(self,mascota):
        if mascota in self.mascotas:
            raise MascotaYaRegistrada("Mascota ya registrada")
        self.mascotas.append(mascota)
    def salida(self,mascota):
        if mascota not in self.mascotas:
            raise MascotaNoEncontrada("Mascota no encontrada")
        self.mascotas.remove(mascota)
    def registro(self,adoptante):
        if adoptante in self.adoptantes:
            raise AdoptanteYaRegistrado("Adoptante ya registrado")
        self.adoptantes.append(adoptante)
    def adoptar(self,adopcion):
        if adopcion in self.adopciones:
            raise AdopcionYaRegistrada("Adopción ya registrada")
        self.adopciones.append(adopcion)
    def mascotas_disponibles(self):
        return [mascota for mascota in self.mascotas if m.estado=="disponible"]
    def __len__(self):
        return len(self.mascotas)
    def __iter__(self):
        for m in self.mascotas:
            if m.estado=="disponible":
                yield m
    def __str__(self):
        return f"Centro de Adopción {self.nombre} con {len(self.mascotas)} mascotas"