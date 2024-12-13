from .animal import Animal

class Reptil(Animal):

    iguanas = 0
    serpientes = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola, zona = None):

        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        super().setZona(zona)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola

    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    
    def getLargoCola(self):
        return self._largoCola
    
    def setLargoCola(self, largoCola):
        self._largoCola = largoCola
    

    #Método movimiento()
    @classmethod
    def movimiento(cls):
        return "reptar"
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    #método cantidadReptiles()
    @classmethod
    def cantidadReptiles(cls):
        return len(Reptil.getListado())
    
    #método crearIguana()
    @classmethod
    def crearIguana(cls,nombre, edad, genero, zona = None):
        Reptil._listado.append(Reptil(nombre, edad, "humedal", genero, "verde", 3, zona))
        Reptil.iguanas += 1

    #método crearSerpiente()
    @classmethod
    def crearSerpiente(cls,nombre, edad, genero, zona = None):
        Reptil._listado.append(Reptil(nombre, edad, "jungla", genero, "blanco", 1, zona))
        Reptil.serpientes += 1