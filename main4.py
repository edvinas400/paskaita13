from PIL import Image

img = Image.open("kate.jpg")

def bandw(data, r, g, b):
    newdata=[]
    for x in data:
        if x[0] > r or x[1] > g or x[2] > b:
            newdata.append((255, 255, 255))
        else:
            newdata.append((0, 0, 0))
    return newdata



def koreguoti(r, g, b):
    data = img.getdata()
    newdata = []
    for x in data:
        if x[0] > r or x[1] > g or x[2] > b:
            newdata=bandw(data, r, g, b)
            break
        newdata=data

    img.putdata(newdata)
    img.show()

koreguoti(150, 150, 150)
