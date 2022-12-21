from PIL import Image, ImageEnhance

logo = Image.open("logo.png")
newlogo = logo.crop((0, 28, 128, 100))
newlogo.save("newlogo.png")


def funkcija(image, kontr, spalv, astr, rysk, save=False):
    img = Image.open(image)
    new = ImageEnhance.Contrast(img)
    img = new.enhance(kontr)
    new = ImageEnhance.Color(img)
    img = new.enhance(spalv)
    new = ImageEnhance.Sharpness(img)
    img = new.enhance(astr)
    new = ImageEnhance.Brightness(img)
    img = new.enhance(rysk)
    img.show()
    if save == True:
        vardas = image.split(".")
        img.save(f"{vardas[0]}_modified.{vardas[1]}")


funkcija("dog.jpg", 2, 15, 9, 2, True)
