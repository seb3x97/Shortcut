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
FILE_CONFIG_MODE_NORMAL = os.path.join(DIR_ROOT, "config/modes/normal.json")
FILE_CONFIG_MODE_ACTION = os.path.join(DIR_ROOT, "config/modes/action.json")
FILE_CONFIG_MODE_CREATIVE = os.path.join(DIR_ROOT, "config/modes/creative.json")

# Datas
FILE_COMMAND_CREATED = os.path.join(DIR_ROOT, "datas\commands_created.json")


#---------- FONCTIONS ----------#

# On récupére la liste des chemins de dossiers renseigné plus haut
def get_folders():
    return { path: name for path, name in globals().items() if path.startswith('DIR') }

# On récupére la liste des chemins de fichiers renseigné plus haut
def get_files():
    return { path: name for path, name in globals().items() if path.startswith('FILE') }