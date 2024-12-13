from .animal import Animal

class Pez(Animal):

    salmones = 0
    bacalaos = 0
    _listado = []
    
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):

        super().setNombre(nombre)
        super().setEdad(edad)
        super().setHabitat(habitat)
        super().setGenero(genero)
        self._colorEscamas = colorEscamas
        self._cantidadAletas = cantidadAletas
    
    def getColorEscamas(self):
        return self._colorEscamas
    
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas

    def getCantidadAletas(self):
        return self._cantidadAletas
    
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas

    
    #método movimiento()
    @classmethod
    def movimiento(cls):
        return "nadar"
    
    @classmethod
    def getListado(cls):
        return cls._listado
    
    #método cantidadPeces()
    @classmethod
    def cantidadPeces(cls):
        return len(Pez.getListado())
    
    #método crearSalmon()
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        Pez._listado.append(Pez(nombre, edad, "ocenao", genero, "rojo", 6))
        Pez.salmones += 1
    
    #método crearBacalao()
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        Pez._listado.append(Pez(nombre, edad, "ocenao", genero, "gris", 6))
        Pez.bacalaos += 1
    
