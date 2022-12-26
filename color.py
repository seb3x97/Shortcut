from colorthief import ColorThief
from PIL import Image

src = r"C:\Users\svoide\Desktop\Avatar.jpg"


color_thief = ColorThief(src)
# get the dominant color
dominant_color = color_thief.get_palette(10, 10)
print(dominant_color)



img = Image.open(src)
imageWithColorPalette = img.convert('P', palette=Image.Palette.ADAPTIVE, colors=20).convert('RGB')
imageWithColorPalette.show()
pixels = imageWithColorPalette.load()