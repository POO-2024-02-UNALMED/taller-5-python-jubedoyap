from .animal import Animal

class Mamifero(Animal):

    caballos = 0
    leones = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        
        super.__init__(nombre, edad, habitat, genero)
        self._pelaje = pelaje
        self._patas = patas
        Mamifero._listado.append(Mamifero(nombre, edad, habitat, genero, pelaje, patas))
    
    def getPatas(self):
        return self._patas
    
    def setPatas(self, patas):
        self._patas = patas

    def getPelaje(self):
        return self._pelaje
    
    def setPelaje(self, pelaje):
        self._pelaje = pelaje

    @classmethod
    def getListado(cls):
        return cls._listado
    
    #Método cantidadMamiferos()
    @classmethod
    def cantidadMamiferos(cls):
        return len(Mamifero.getListado())
    
    #Método crearCaballo()
    def crearCaballo(self, nombre, edad, genero):
        Mamifero(nombre, edad, "pradera", genero, True, 4)
        Mamifero.caballos += 1

    #Método crearLeon()
    def crearLeon(self, nombre, edad, genero):
        Mamifero(nombre, edad, "selva", genero, True, 4)
        Mamifero.leones += 1

    