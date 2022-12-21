from PIL import Image
import os

direktorija = "C:\\Users\\edvin\\OneDrive\\Desktop"
logo = Image.open("newlogo.png")

def funkcija(direktorija, aukstis):
    os.chdir(direktorija)
    for x in os.listdir():
        if x.endswith(('.png', '.jpg', '.jpeg',  '.gif')):
            pic = Image.open(x)
            pic = pic.resize((round(pic.size[0] / pic.size[1] * aukstis), aukstis))
            logolocation = (pic.size[0]-logo.size[0], pic.size[1]-logo.size[1], pic.size[0], pic.size[1])
            pic.paste(logo, logolocation, logo)
            pic.show()

funkcija(direktorija, 200)
# dog = Image.open('dog.jpg')
# logo = Image.open('logo.png')
# logo_location = (0, 0, logo.size[0], logo.size[1])
# dog.paste(logo, logo_location, logo)
# dog.show()
