from PIL import Image

def are_two_tuple_eguals(tuple1: tuple, tuple2: tuple) -> bool:
    return sorted(tuple1) == sorted(tuple2)


class Group:
    def __init__(self, color: tuple) -> None:
        self.color: tuple = color
        self.positions: list = []

    def add(self, position: tuple) -> bool:
        self.positions.append(position)

# On démarre l'action
def start() -> bool:
    img = Image.open(r"C:/Users/svoide/Desktop/Draw.jpeg")
    img = img.convert('P', palette=Image.Palette.ADAPTIVE, colors=3).convert('RGBA')

    width, height = img.size

    colors: dict[tuple, list[tuple]] = {}

    colors_grouped: dict[tuple, Group] = {}

    for x in range(1):
        for y in range(2):
            # On récupére la position actuelle (x, y)
            current_pos: tuple = (x, y)

            # On récupére les couleurs rgba/rgb
            color_rgba: tuple = img.getpixel(current_pos)
            color_rgb: tuple = color_rgba[:-1]

            # Checks des couleurs
            if color_rgba[-1] == 0: continue                                # Si la couleur est transparente
            #if sorted(color_rgb) == sorted((255, 255, 255)): continue       # Si la couleur est blanche

            # On ajoute la couleur dans le dictionnaire
            if(color_rgb not in colors): colors[color_rgb] = []
            colors[color_rgb].append(current_pos)

            # Todo : créer le groupe que si on ne peut pas ajouter la couleur dans un groupe
            if(current_pos not in colors_grouped): colors_grouped[current_pos] = Group(color_rgb)

            """
            last_pos_x = (x - 1, y)
            #get_list_x = colors_grouped.get(last_pos_x, None)
            last_color_x = colors_grouped.get(last_pos_x, None)
            if (x >= 1 and (last_color_x is not None) and are_two_tuple_eguals(color_rgb, img.getpixel(last_pos_x)[:-1])):
                pass
            """

            last_pos_y = (x, y - 1)
            #get_list_y = colors_grouped.get(last_pos_y, None)
            last_group_y = colors_grouped.get(last_pos_y, None)
            if (y >= 1 and (last_group_y is not None) and are_two_tuple_eguals(color_rgb, img.getpixel(last_pos_y)[:-1])):
                last_group_y.add(current_pos)
                colors_grouped[current_pos] = last_group_y
                pass

        print(colors_grouped)

    # Succès
    return True


start()