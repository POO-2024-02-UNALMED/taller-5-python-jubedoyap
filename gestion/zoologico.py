class Zoologico():

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []
    
    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nuevoNombre):
        self._nombre = nuevoNombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def setUbicacion(self, nuevaUbicacion):
        self._ubicacion = nuevaUbicacion

    def agregarZonas(self, nuevaZona):
        self._zonas.append(nuevaZona)

    def getZonas(self):
        return self._zonas
    
    def getZona(self):
        if self._zonas:
            return self._zonas[0]
        return None
    

    def cantidadTotalAnimales(self):
        cantidadTotalAnimales = 0
        for zona in self._zonas:
            cantidadTotalAnimales += zona.cantidadAnimales()
        return cantidadTotalAnimales