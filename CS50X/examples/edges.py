#Esto aplica el filtro negativo

from PIL import Image, ImageFilter

before = Image.open("brige.bmp")
after = before.filter(ImageFilter.FIND_EDGES)
after.save("out.bmp")
