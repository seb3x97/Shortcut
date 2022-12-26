# Check si une classe contient une fonction (callable)
def class_contains_function(element: object, func_name: str) -> bool:
    return hasattr(element, func_name) and callable(getattr(element, func_name))


# On récupére les variables d'une class (publique)
def get_class_public_variables(element: object) -> list:
    return [attr for attr in dir(element) if not callable(getattr(element, attr)) and not attr.startswith("_")]


# On récupére les variables d'une class (publique) avec leurs valeurs
def get_class_public_variables_with_values(element: object) -> dict:
    # Va contenir la liste des variables (publique) d'une classe
    datas: dict = {}

    # On boucle les variables de la classe pour récupérer leurs valeurs pour les push ses infos dans un dictionnaire
    for variable in get_class_public_variables(element):
        datas[variable] = getattr(element, variable)

    # On retourne les données
    return datas


# On sauvegarde les données des variables dans la classe
def save_class_public_variables_with_values(element: object, datas: dict) -> bool:
    # On enregistre les données dans la classe
    for data in datas:
        setattr(element, data, datas[data])

    # Succès
    return True