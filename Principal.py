from ViajeroFrecuente import ViajeroFrecuente
import csv

def agregarViajeros (listaViajero, agregarViajero):
    if (agregarViajero[0] != '') & (agregarViajero[1] != '') & (agregarViajero[2] != '') & (agregarViajero[3] != '') & (agregarViajero[4].isdigit()):
         unViajero = ViajeroFrecuente(agregarViajero[0],agregarViajero[1],agregarViajero[2],agregarViajero[3],int(agregarViajero[4]))
         listaViajero.append(unViajero)

def buscaIndice(n,l):
    indice = 0
    band = True
    while (indice < len(l)) & (band):
        if l[indice].getnumViaj() == n:
            band = False
        else:
            indice+=1
    if indice < len(l):
        return indice
    else:
        return -1

def consultarMillas(numero,lista):
    i = buscaIndice(numero,lista)
    if i != -1:
        print(lista[i].cantidadTotaldeMillas())
    else:
        print('No existe un viajero frecuente con ese numero.')

def acumMillas(numero,lista):
    i = buscaIndice(numero,lista)
    if i != -1:
        cant = input('Ingrese la cantidad de millas a acumular: ')
        if cant.isdigit():
            lista[i].acumularMillas(int(cant))
        else:
            print('Ese no es un valor aceptable.')
    else:
        print('No existe un viajero frecuente con ese numero.')

def canjMillas(numero,lista):
    i = buscaIndice(numero,lista)
    if i != -1:
        cant = input('Ingrese la cantidad de millas a canjear: ')
        if cant.isdigit():
            lista[i].canjearMillas(int(cant))
        else:
            print('Ese no es un valor aceptable.')
    else:
        print('No existe un viajero frecuente con ese numero.')

switcher = {
    1: consultarMillas,
    2: acumMillas,
    3: canjMillas
}

def switch(argument, num, lis):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func(num,lis)

if __name__ == '__main__':

    archivo = open('ejemplo.csv')
    reader = csv.reader(archivo, delimiter = ';')
    ListaViajeros = []
    for lista in reader:
        agregarViajeros(ListaViajeros, lista)
#    for elemento in ListaViajeros:  para ver la lista de objetos creados
#        print(elemento)
#        print('\n')

    viajero = input('Ingrese numero de viajero frecuente, ingrese 0 para terminar: ')
    while viajero != '0':
        print("")
        print("1 Consultar Cantidad de millas.")
        print("2 Acumular millas")
        print("3 Canjear millas")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion, viajero,ListaViajeros)
        viajero = input('Ingrese otro numero de viajero frecuente o ingrese 0 para terminar: ')
