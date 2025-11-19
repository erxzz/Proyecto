class CentroAdopcionError(Exception):
    pass
class MenorEdad(CentroAdopcionError):
    pass
class FormatoMascota(CentroAdopcionError):
    pass
class MascotaYaRegistrada(CentroAdopcionError):
    pass
class MascotaNoEncontrada(CentroAdopcionError):
    pass
class AdoptanteYaRegistrado(CentroAdopcionError):
    pass
class AdopcionYaRegistrada(CentroAdopcionError):
    pass
class MascotaNoDisponible(CentroAdopcionError):
    pass