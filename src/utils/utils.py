#---------- Package ----------#

import json
import pymsgbox
from typing import Union

#---------- Function ----------#

# On affiche un message
def show_message(text: str = "", title: str = ""):
    pymsgbox.alert(text=text, title=title)

# On récupére le contenu d'un fichier
def read_file_content(src: str) -> Union[str, None]:
    try:
        with open(file=src, mode='r') as file: return file.read()
    except IOError:
        return None

# On convertit du texte en format json (dictionnaire)
def convert_text_to_json(text: str) -> Union[dict, None]:
    try:
        return json.loads(s=text)
    except json.JSONDecodeError:
        return None