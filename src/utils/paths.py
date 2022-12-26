# Auteur : Sébastien Voide
# Création : 20.12.2022
# Modification :
# Description : Tous les chemins de fichier/dossier sont stoqués ici
# /!\ : Un système automatique est mis en place pour check si les chemins éxistent toujours.
#       Pour qu'il fonctionne correctement, veuillez mettre comme préfixe à chaque constantes :
#           - DIR_  => Pour les dossiers
#           - FILE_ => Pour les fichiers

#---------- IMPORTS ----------#

# Os
import os


#---------- DOSSIERS ----------#

# Root
DIR_ROOT = os.path.abspath("")
DIR_LOG = os.path.join(DIR_ROOT, "log")


#---------- FICHIERS ----------#

# Config
FILE_COMMAND_DEFAULT = os.path.join(DIR_ROOT, "datas\commands_default.json")
FILE_COMMAND_CREATED = os.path.join(DIR_ROOT, "datas\commands_created.json")


#---------- FONCTIONS ----------#

# On récupére la liste des dossiers de ce fichier
def get_folders():
    return { path: name for path, name in globals().items() if path.startswith('DIR') }

# On récupére la liste des fichiers de ce fichier
def get_files():
    return { path: name for path, name in globals().items() if path.startswith('FILE') }