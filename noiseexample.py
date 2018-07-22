
from PIL import Image 
from opensimplex import OpenSimplex
from biomes import *
import math

WIDTH = 900
HEIGHT = 400
FREQUENCY = 5.0


def noise(nx, ny, gen):
    # Rescale from -1.0:+1.0 to 0.0:1.0
    return gen.noise2d(nx, ny) / 2.0 + 0.5

def createelevation():
    print('Generating noise from OpenSimplex...')
    gen = OpenSimplex(123456)
    # os2 = OpenSimplex(22)
    # os3 = OpenSimplex(20202)
    
    
    elevation = []
    for y in range(0, HEIGHT):
        elevation.append([0] * WIDTH)
        for x in range(0, WIDTH):
            nx = x/WIDTH - 0.5
            ny = y/HEIGHT - 0.5
            e = (1 * noise(FREQUENCY * nx, FREQUENCY * ny, gen) +
                0.5 * noise(2 * nx, 2 * ny, gen) + 
                0.25 * noise(4 * nx, 4 * ny, gen))

            e = math.pow(e, 4)
            elevation[y][x] = e
            # print (elevation[y][x])
        
    return elevation

def saveimg(elevation):
    print ("Saving Image...")
    im = Image.new('RGB', (WIDTH, HEIGHT))
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            e = elevation[y][x]
            # print (e)
            if (e < 0.15):
                color = biome["OCEAN"]
            else:
                color = (0, int((e) * 128), 0)
                # print (color)
            im.putpixel((x, y), color)
    im.save('noise.bmp')

def main():
    elevation = createelevation()
    saveimg(elevation)

if __name__ == '__main__':
    main()