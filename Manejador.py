from ViajeroFrecuente import ViajeroFrecuente

class Manejador:
    __ListaViaj = []

    def __init__ (self):
        __ListaViaj = []

    def agregarViajeros (self, agregarViajero):
        if (agregarViajero[0] != '') & (agregarViajero[1] != '') & (agregarViajero[2] != '') & (agregarViajero[3] != '') & (agregarViajero[4].isdigit()):
             unViajero = ViajeroFrecuente(agregarViajero[0],agregarViajero[1],agregarViajero[2],agregarViajero[3],int(agregarViajero[4]))
             self.__ListaViaj.append(unViajero)

    def Mostrar (self):
        for elemento in self.__ListaViaj:
            print(elemento)
            print('\n')

    def buscaIndice(self,n):
        indice = 0
        band = True
        while (indice < len(self.__ListaViaj)) & (band):
            if self.__ListaViaj[indice].getnumViaj() == n:
                band = False
            else:
                indice+=1
        if indice < len(self.__ListaViaj):
            return indice
        else:
            return -1

    def getViajero (self, i):
        return self.__ListaViaj[i]
