
from PIL import Image 
from opensimplex import OpenSimplex
from constants import *
from tqdm import tqdm
import math
import random

def saveimg(elevation):
    """Save data to a bmp"""

    print ("Saving Image...")
    im = Image.new('RGB', (WIDTH, HEIGHT))
    for y in tqdm(range(0, HEIGHT)):
        for x in range(0, WIDTH):
            color = decidebiome(elevation[y][x])
            im.putpixel((x, y), color)
    im.save('island.bmp')

def noise(nx, ny, gen):
    """Rescale from -1.0:+1.0 to 0.0:1.0"""
    f = FREQUENCY
    return gen.noise2d(nx * f, ny * f) / 2.0 + 0.5

def island(e, nx, ny):
    """Generate boundaries for island creation (ie. have water on all edges"""
    a = ISLAND_A # Pushes everything up
    b = ISLAND_B # Pushes edges down
    c = ISLAND_C # Controls how fast the dropdown is
    d = 2*math.sqrt(nx*nx + ny*ny) # Distance from the centre
    return ((e + a) * (1 - b*d**c))
    

def createelevation():
    """Create an elevation chart with "data" from simplex noise"""
    print('Generating noise from OpenSimplex...')
    gen = OpenSimplex(random.randint(1, 99999))
    # gen = OpenSimplex()    
    
    elevation = []
    for y in tqdm(range(0, HEIGHT)):
        elevation.append([0] * WIDTH)
        for x in range(0, WIDTH):
            nx = x/WIDTH - 0.5
            ny = y/HEIGHT - 0.5

            # Create uneven elevation points
            e0 = 1.00 * noise(1 * nx, 1 * ny, gen)
            e1 = 0.15 * noise(2 * nx, 2 * ny, gen)
            e2 = 0.05 * noise(4 * nx, 4 * ny, gen)

            e = e0 + e1 + e2
            e = island(e, nx, ny)
            elevation[y][x] = e
        
    return elevation



def decidebiome(e):
    """Calculate which color a specific pixel will get"""
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
    if (e < 0.95):
        return biome["MOUNTAIN"]
    else:
        return biome["SNOW"]

def main():
    elevation = createelevation()
    saveimg(elevation)

if __name__ == '__main__':
    main()