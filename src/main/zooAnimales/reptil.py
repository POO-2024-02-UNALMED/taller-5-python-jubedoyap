from .animal import Animal

class Reptil(Animal):

    iguanas = 0
    serpientes = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):

        super.__init__(nombre, edad, habitat, genero)
        self._colorEscamas = colorEscamas
        self._largoCola = largoCola
        Reptil._listado.append(Reptil(nombre, edad, habitat, genero, colorEscamas, largoCola)) # Pilas con el bucle infinito

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
    def crearIguana(cls,nombre, edad, genero):
        Reptil._listado.append(Reptil(nombre, edad, "humedal", genero, "verde", 3))
        Reptil.iguanas += 1

    #método crearSerpiente()
    @classmethod
    def crearSerpiente(cls,nombre, edad, genero):
        Reptil._listado.append(Reptil(nombre, edad, "jungla", genero, "blanco", 1))
        Reptil.serpientes += 1