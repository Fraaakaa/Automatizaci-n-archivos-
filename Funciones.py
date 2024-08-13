import os
import shutil
from os import system

def seleccionar_archivos(archivos:list, extension:str) -> list:
    """Selecciona los archivos con la extension correspondiente

    Args:
        archivos (list): Archivos de la carpeta
        extension (str): Extension de los archivos a seleccionar

    Returns:
        list: Devuelve la lista con los archivos seleccionados 
    """
    retorno = []
    
    for i in range(len(archivos)):
        separado = archivos[i].split(".")
        
        if separado[-1] == extension:
            retorno.append(archivos[i])
    
    if len(retorno) == 0:
        print("No se encontraron archivos en la carpeta con esa extension")
        system("pause")
        retorno = False
        
    return retorno

def mover_archivos(archivos:list, carpeta_a_ordenar:str, carpeta_destino:str):
    """Mueve los archivos al destino

    Args:
        archivos (list): Archivos con la extension
        carpeta_a_ordenar (str): La carpeta de origen
        carpeta_destino (str): La carpeta de destino
    """
    for archivo in archivos:
        origen = os.path.join(carpeta_a_ordenar, archivo)
        destino = os.path.join(carpeta_destino, archivo)
        
        shutil.move(origen, destino)
        print(f"El archivo {archivo} fue movido a {carpeta_destino}")