import pathlib
import os
import shutil

# Carpeta donde se ubica el script
path_script = pathlib.Path(__file__).parent

# Lista con los archivos de la carpeta
list_contest = os.listdir(path_script)

for contest in list_contest:
    path_contest = os.path.join(path_script, contest)
    if(os.path.isdir(path_contest)):
        list_problemas = os.listdir(path_contest)
        for problema in list_problemas:
            if problema.endswith(".exe"):
                path_problema = os.path.join(path_contest, problema)
                os.remove(path_problema)
