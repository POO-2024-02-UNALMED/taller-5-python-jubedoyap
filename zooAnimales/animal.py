from gestion.zona import Zona
from zooAnimales.mamifero import Mamifero
from zooAnimales.ave import Ave
from zooAnimales.reptil import Reptil
from zooAnimales.pez import Pez
from zooAnimales.anfibio import Anfibio

class Animal():

    _totalAnimales = 0
    
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = []
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
        self._zona[0] = nuevaZona
    
    def getZona(self):
        return self._zona
    
    #Método total por tipo
    @classmethod
    def totalPorTipo(cls):
        return ("Mamiferos : ", Mamifero.cantidadMamiferos(), "\nAves : ", Ave.cantidadAves(), "\nReptiles : ", Reptil.cantidadReptiles(), 
                "\nPeces : ", Pez.cantidadPeces(), "\nAnfibios : ", Anfibio.cantidadAnfibios())
    
    #Método toString()
    def __str__(self):
        cadena = ""
        if (self.getZona()[0] == None):
            cadena = "Mi nombre es ", self.getNombre(), " tengo una edad de ", self.getEdad(), ", habito en ", self.getHabitat(), " y mi genero es ", self.getGenero()
        else:
            cadena = ("Mi nombre es ", self.getNombre(), " tengo una edad de ", self.getEdad(), ", habito en ", self.getHabitat(), " y mi genero es ", self.getGenero(),
                      ", la zona en la que me ubico es ", self.getZona(), ", en el ", self.getZona().getZoo())
        return cadena
    
    #Método movimiento()
    @classmethod
    def movimiento(cls):
        return "desplazarse"