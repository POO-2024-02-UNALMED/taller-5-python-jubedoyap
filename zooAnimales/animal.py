class Animal():

    _totalAnimales = 0
    
    def __init__(self, nombre, edad, habitat, genero, zona = None):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = zona
        Animal._totalAnimales += 1

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre
    
    def getEdad(self):
        return self._edad
    
    def setEdad(self, nuevaEdad):
        self._edad = nuevaEdad

    def getHabitat(self):
        return self._habitat
    
    def setHabitat(self, nuevaHabitat):
        self._habitat = nuevaHabitat
    
    def getGenero(self):
        return self._genero
    
    def setGenero(self, nuevoGenero):
        self._genero = nuevoGenero

    def setZona(self, nuevaZona):
        self._zona = nuevaZona
    
    def getZona(self):
        return self._zona
    
    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales
    
    #Método total por tipo
    @classmethod
    def totalPorTipo(cls):
        from .mamifero import Mamifero
        from .ave import Ave
        from .reptil import Reptil
        from .pez import Pez
        from .anfibio import Anfibio
        return "Mamiferos : " + str(Mamifero.cantidadMamiferos()) + "\n" + \
           "Aves : " + str(Ave.cantidadAves()) + "\n" + \
           "Reptiles : " + str(Reptil.cantidadReptiles()) + "\n" + \
           "Peces : " + str(Pez.cantidadPeces()) + "\n" + \
           "Anfibios : " + str(Anfibio.cantidadAnfibios())
    
    
    #Método toString()  
    def toString(self):
        cadena = ""
        if (self.getZona() is None):
            cadena = "Mi nombre es " + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero()
        else:
            cadena = "Mi nombre es " + self.getNombre() + ", tengo una edad de " + str(self.getEdad()) + ", habito en " + self.getHabitat() + " y mi genero es " + self.getGenero() + \
                     ", la zona en la que me ubico es " + str(self.getZona()) + ", en el " + str(self.getZona().getZoo())
        return cadena
    #Método movimiento()
    @classmethod
    def movimiento(cls):
        return "desplazarse"