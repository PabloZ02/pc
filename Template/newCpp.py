import pathlib
import os
import shutil
from time import sleep


name = input("name of file: ") + ".cpp"
# Carpeta donde se ubica el script
parent_dir = pathlib.Path(__file__).parent

# Pega en el path el nombre de la carpeta
path = os.path.join(parent_dir, name)
   
# si ya existe esa carpeta se rompe todo
if os.path.exists(path) : 
    print("este ejercicio ya existe perrachon")
    sleep(2)
else :
    macros = "/home/natanvek/0-COMPUTER/0-PROGRAMACION/8-COMPETENCIA/Template/macros.cpp"
    template = "/home/natanvek/0-COMPUTER/0-PROGRAMACION/8-COMPETENCIA/Template/template.cpp"
    # shutil.copy(src, path) 
    newcpp = open(path, 'wb')
    shutil.copyfileobj(open(macros, 'rb'), newcpp)
    shutil.copyfileobj(open(template, 'rb'), newcpp)
    newcpp.close()

# shutil.copy(src, newpath) :
# copia un archivo en el path src y lo pega en el path newpath
# si newpath es una carpeta lo pega con el mismo nombre al archivo
# si newpath es un archivo le pone ese nombre pero si ya existe ese nombre
# creo que sobreescribe

