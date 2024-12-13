from .animal import Animal

class Ave(Animal):
    
    halcones = 0
    aguilas = 0
    _listado = []

    def __init__(self, nombre, edad, habitat, genero, colorPlumas, zona = None):

        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(zona)
        self._colorPlumas = colorPlumas
    
    def getColorPlumas(self):
        return self._colorPlumas
    
    def setColorPlumas(self, colorPlumas):
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
    def crearHalcon(cls, nombre, edad, genero, zona = None):
        Ave._listado.append(Ave(nombre, edad, "montanas", genero, "cafe glorioso",zona))
        Ave.halcones += 1

    #método crearAguila
    @classmethod
    def crearAguila(cls, nombre, edad, genero, zona = None):
        Ave._listado.append(Ave(nombre, edad, "montanas", genero, "blanco y amarillo", zona))
        Ave.aguilas += 1
