import image as image
from PIL import Image, ImageFilter

image = Image.open("kuş.jpg")


image.save("kuş2.jpg")

image.rotate(180).save("kuş3.jpg")

image.rotate(90).save("kuş4.jpg")

image.convert(mode = "L").save("kuş5.jpg")

değistir = (960,600)

image.thumbnail(değistir)

image.save("kuş6.jpg")

image.filter(ImageFilter.GaussianBlur(5)).save("kuş7.jpg")
image.filter(ImageFilter.GaussianBlur(20)).save("kuş8.jpg")

kırpılacak_alan = (340,0,950,600)

image2 = Image.open("atatürk.jpg")
image2.crop(kırpılacak_alan).save("atatürk2.jpg")

