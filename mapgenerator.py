from opensimplex import OpenSimplex
from PIL import Image, ImageDraw
import sys

HEIGHT = 5
WIDTH = 5



def mapgen():

    tmp = OpenSimplex()
    value = [[0 for x in range(WIDTH)] for y in range(HEIGHT)] 

    for x in range(HEIGHT):
        for y in range(WIDTH):
            nx = x/WIDTH + 1
            ny = y/HEIGHT + 1
            value[y][x] = tmp.noise2d(nx, ny)

    print (value)
    return value

def drawmap(value):
    im = Image.new("RGB", (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(im)
    for x in range(HEIGHT):
        for y in range(WIDTH):
            im.putpixel((x, y), (0, int(value[x][y]*255), 0))

    im.save("test.png", "PNG")



if __name__ == "__main__":
    value = mapgen()


    drawmap(value)