from PIL import Image, ImageDraw
def z1():
    im = Image.open('otkr.jpg')
    obr = im.crop((230, 230, 800, 800))
    obr.save('1im.jpg')
    obr.show()

def z2():
    pr = {'Новый год': '31.jpeg', '23 февраля':'23.jpeg', '8 марта':'8.jpeg'}
    p = input('Введите название праздника:')
    if p in pr:
        otkr = pr[p]
        im = Image.open(otkr)
        im.show()
    else:
        print('Открытки нет')

def z3():
    n = str(input("введите имя:"))
    t = n + ", congratulations!"
    im = Image.open('1im.jpg')
    draw = ImageDraw.Draw(im)
    draw.text((70,70), t, fill='pink')
    im.show()
z3()

