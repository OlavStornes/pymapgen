
from PIL import Image 
from opensimplex import OpenSimplex

WIDTH = 512
HEIGHT = 512
FEATURE_SIZE = 24.0


def createelevation():
    simplex = OpenSimplex()

    print('Generating noise from OpenSimplex...')
    elevation = [[0 for x in range(WIDTH)] for y in range(HEIGHT)] 
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            elevation[y][x] = simplex.noise2d(x / FEATURE_SIZE, y / FEATURE_SIZE)
    return elevation


def saveimg(elevation):
    print ("Saving Image...")
    im = Image.new('L', (WIDTH, HEIGHT))
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            color = int((elevation[x][y] + 1) * 128)
            im.putpixel((x, y), color)
    im.save('noise.png')

def main():
    elevation = createelevation()
    saveimg(elevation)

if __name__ == '__main__':
    main()