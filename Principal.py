from ViajeroFrecuente import ViajeroFrecuente
from Manejador import Manejador
import csv

def consultarMillas(numero,lista):
    i = lista.buscaIndice(numero)
    if i != -1:
        print(lista.getViajero(i).cantidadTotaldeMillas())
    else:
        print('No existe un viajero frecuente con ese numero.')

def acumMillas(numero,lista):
    i = lista.buscaIndice(numero)
    if i != -1:
        cant = input('Ingrese la cantidad de millas a acumular: ')
        if cant.isdigit():
            lista.getViajero(i).acumularMillas(int(cant))
        else:
            print('Ese no es un valor aceptable.')
    else:
        print('No existe un viajero frecuente con ese numero.')

def canjMillas(numero,lista):
    i = lista.buscaIndice(numero)
    if i != -1:
        cant = input('Ingrese la cantidad de millas a canjear: ')
        if cant.isdigit():
            lista.getViajero(i).canjearMillas(int(cant))
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
    ListaViajeros = Manejador()
    for lista in reader:
        ListaViajeros.agregarViajeros(lista)
    archivo.close()
    ListaViajeros.Mostrar()

    viajero = input('Ingrese numero de viajero frecuente, ingrese 0 para terminar: ')
    while viajero != '0':
        print("")
        print("1 Consultar Cantidad de millas.")
        print("2 Acumular millas")
        print("3 Canjear millas")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion, viajero,ListaViajeros)
        viajero = input('Ingrese otro numero de viajero frecuente o ingrese 0 para terminar: ')
