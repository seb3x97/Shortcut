#---------- Package ----------#

import json
import pymsgbox
import typing

#---------- Function ----------#

# On affiche un message
def show_message(text: str = "", title: str = ""):
    pymsgbox.alert(text=text, title=title)

# On récupére le contenu d'un fichier
def read_file_content(src: str) -> typing.Union[str, None]:
    try:
        with open(file=src, mode='r') as file:
            return file.read()
    except IOError:
        return None

# On écrit un contenu dans un fichier
def write_file_content(src: str, content: str) -> bool:
    try:
        with open(file=src, mode='w') as file:
            file.write(content)

        return True
    except IOError:
        return False

# On convertit du texte en format json (dictionnaire)
def convert_text_to_json_object(text: str) -> typing.Union[dict, None]:
    try:
        return json.loads(s=text)
    except json.JSONDecodeError:
        return None

# On convertit un objet en texte json
def convert_object_to_json_text(obj: object) -> typing.Union[dict, None]:
    # Encodeur
    class CustomEncoder(json.JSONEncoder):
        def default(self, o):
                return o.__dict__
    
    try:
        return json.dumps(obj=obj, indent=4, cls=CustomEncoder)
    except json.JSONDecodeError:
        return None