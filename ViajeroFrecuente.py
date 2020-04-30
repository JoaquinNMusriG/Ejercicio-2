class ViajeroFrecuente:
    __numViaj = ''
    __DNI = ''
    __Nombre = ''
    __Apellido = ''
    __millasAcum = 0

    def __init__ (self, num, dni, nomb, ap, milla):
        self.__numViaj = num
        self.__DNI = dni
        self.__Nombre = nomb
        self.__Apellido = ap
        self.__millasAcum = milla

    def __str__ (self):
        return 'numero: '+ self.__numViaj + '\ndni: ' + self.__DNI + '\nNombre: '+ self.__Nombre + '\nApellido: ' + self.__Apellido + '\nMillas: ' + str(self.__millasAcum)

    def getnumViaj(self):
        return self.__numViaj

    def cantidadTotaldeMillas(self):
        return self.__millasAcum

    def acumularMillas(self, millasReco):
        self.__millasAcum += millasReco
        print('Millas actualizadas.')

    def canjearMillas (self, canjeMilla):
        if canjeMilla <= self.__millasAcum:
            self.__millasAcum -= canjeMilla
            print('Se han canjeado las millas.')
        else:
            print('NO hay millas suficientes para canjear.')
