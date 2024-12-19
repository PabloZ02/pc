import pathlib
import os
import shutil
from time import sleep

nombre = input("Nombre del archivo: ")

# Carpeta donde se ubica el script
parent_dir = pathlib.Path(__file__).parent

# Nombre de la carpeta a crear
directory = "Ejercicio " + nombre

# Pega en el path el nombre de la carpeta
path = os.path.join(parent_dir, directory)
   
# si ya existe esa carpeta se rompe todo
if os.path.exists(path) : 
    print("este contest ya existe perrachon")
    sleep(2)
else :
    os.mkdir(path)   
    macros = r"C:\Users\usuario1\Documents\Programacion_competitiva\Template\macros.cpp"
    template = r"C:\Users\usuario1\Documents\Programacion_competitiva\Template\template.cpp"
    name = nombre + ".cpp"
    newpath = os.path.join(path, name)
    newcpp = open(newpath, 'wb')
    shutil.copyfileobj(open(macros, 'rb'), newcpp)
    shutil.copyfileobj(open(template, 'rb'), newcpp)
    newcpp.close()
    
    
