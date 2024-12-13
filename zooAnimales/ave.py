from .animal import Animal

class Ave(Animal):
    
    halcones = 0
    aguilas = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorPlumas):

        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        self._colorPlumas = colorPlumas
    
    def getPlumas(self):
        return self._colorPlumas
    
    def setPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas
    
    #Método movimiento()
    @classmethod
    def movimiento(cls):
        return "volar"
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    #método cantidadAves
    @classmethod
    def cantidadAves(cls):
        return len(Ave.getListado())
    
    #método crearHalcon
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        Ave._listado.append(Ave(nombre, edad, "montanas", genero, "cafe glorioso"))
        Ave.halcones += 1

    #método crearAguila
    def crearAguila(cls, nombre, edad, genero):
        Ave._listado.append(Ave(nombre, edad, "montanas", genero, "blanco y amarillo"))
        Ave.aguilas += 1
