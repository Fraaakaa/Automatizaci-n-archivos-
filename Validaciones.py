from os import system
import os

def validar_extension(extensiones:list):
    """Valida si la extension esta soportada por el programa

    Args:
        extensiones (list): La lista de las extensiones soportadas

    Returns:
        _type_: Devuelve la extension validada
    """
    extension = None
    
    while extension not in extensiones:
        system("cls")
        extension = input("Ingrese la extension del archivo a ordenar(sin el punto): ")
        
    return extension

def validar_carpeta() -> str:
    """Valida la carpeta para ver si existe

    Returns:
        str: Devuelve la carpeta
    """
    validada = False
    carpeta_a_ordenar = None
    
    while validada == False:
        carpeta_a_ordenar = input("Direccion de la carpeta a ordenar: ")
        system("cls")
        
        if os.path.exists(carpeta_a_ordenar) == False:
            print("Esa carpeta no existe")
            system("pause")
            system("cls")
        else:
            validada = True
    
    return carpeta_a_ordenar