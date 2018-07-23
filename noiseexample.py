
from PIL import Image 
from opensimplex import OpenSimplex
from biomes import *
import math

WIDTH = 400
HEIGHT = 400
FREQUENCY = 10.0


def noise(nx, ny, gen):
    # Rescale from -1.0:+1.0 to 0.0:1.0
    return gen.noise2d(nx, ny) / 2.0 + 0.5

def island(e, nx, ny):
    a = 0.10 # Pushes everything up
    b = 1.10 # Pushes edges down
    c = 1.20 # Controls how fast the dropdown is
    d = 2*max(abs(nx), abs(ny)) # Distance from the centre
    return ((e + a) * (1 - b*d**c))
    

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
            # Split up different gradiants at different frequencies
            e0 = 1.00 * noise(FREQUENCY * nx, FREQUENCY * ny, gen)
            e1 = 0.50 * noise(2 * nx, 2 * ny, gen)
            e2 = 0.25 * noise(4 * nx, 4 * ny, gen)

            e = e0# + e1 + e2
            e = island(e, nx, ny)
            # e = math.pow(e, 1.2)
            elevation[y][x] = e
            # print (elevation[y][x])
        
    return elevation

def saveimg(elevation):
    print ("Saving Image...")
    im = Image.new('RGB', (WIDTH, HEIGHT))
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            color = decidebiome(elevation[y][x])
            # print (color)
            im.putpixel((x, y), color)
    im.save('noise.bmp')

def decidebiome(e):
    if (e <= 0.10):
        return biome["DEEPOCEAN"]
    if (e < 0.25):
        return biome["OCEAN"]
    if (e < 0.30):
        return biome["SHORE"]    
    if (e < 0.55):
        return biome["FOREST"]
    if (e < 0.70):
        return biome["JUNGLE"]
    if (e < 0.80):
        return biome["ROCK"]
    if (e < 0.85):
        return biome["MOUNTAIN"]
    else:
        # print (e)
        return biome["SNOW"]

def main():
    elevation = createelevation()
    saveimg(elevation)

if __name__ == '__main__':
    main()