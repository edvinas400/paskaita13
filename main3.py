from PIL import Image

img = Image.open("kate.jpg")


def check(skaicius):
    if skaicius < 0:
        return 0
    elif skaicius > 255:
        return 255
    else:
        return skaicius


def koreguoti(r, g, b):
    data = img.getdata()
    newdata = []
    for x in data:
        raud = check(x[0] + r)
        zal = check(x[0] + g)
        mel = check(x[0] + b)
        newdata.append((raud, zal, mel))
    img.putdata(newdata)
    img.show()

koreguoti(0,6,80)