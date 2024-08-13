import os
from Funciones import *
from Validaciones import *
from os import system

extensiones = ["flp"]

while True:
    extension = validar_extension(extensiones)
    system("cls")
    carpeta_a_ordenar = validar_carpeta()
    
    archivos = os.listdir(carpeta_a_ordenar)
    seleccionados = seleccionar_archivos(archivos, extension)
    
    if seleccionados != False:
        carpeta_destino = input("Direccion de la carpeta de destino: ")
        
        mover_archivos(seleccionados, carpeta_a_ordenar, carpeta_destino)
        print("Ordenamiento terminado")        
        system("pause")
    
    break