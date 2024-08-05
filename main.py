import os
from Funciones import *
from os import system

while True:
    
    extension = input("Ingrese la extension del archivo a ordenar(sin el punto): ")
    system("cls")
    carpeta_a_ordenar = input("Direccion de la carpeta a ordenar: ")
    system("cls")
    
    if os.path.exists(carpeta_a_ordenar) == False:
        print("Esa carpeta no existe")
        system("pause")
        system("cls")
        
    else:
        archivos = os.listdir(carpeta_a_ordenar)
        seleccionados = seleccionar_archivos(archivos, extension)
        
        if seleccionados != False:
            carpeta_destino = input("Direccion de la carpeta de destino: ")
            
            mover_archivos(seleccionados, carpeta_a_ordenar, carpeta_destino)
            print("Ordenamiento terminado")        
            system("pause")
            break