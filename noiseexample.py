
from PIL import Image 
from opensimplex import OpenSimplex

WIDTH = 512
HEIGHT = 512
FEATURE_SIZE = 24.0


def createelevation():
    simplex = OpenSimplex()

    print('Generating noise from OpenSimplex...')
    im = Image.new('L', (WIDTH, HEIGHT))
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            elevation = simplex.noise2d(x / FEATURE_SIZE, y / FEATURE_SIZE)
            color = int((elevation + 1) * 128)
            im.putpixel((x, y), color)
    im.save('noise.png')

def saveimg(elevation):
    pass


if __name__ == '__main__':
    main()