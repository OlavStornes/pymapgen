
from PIL import Image
from opensimplex import OpenSimplex
import math
import random


biome = {
    "DEEPOCEAN": (0, 0, 80),
    "OCEAN": (0, 0, 128),
    "SHORE": (255, 193, 37),
    "PLAINS": (100, 200, 112),
    "FOREST": (34, 139, 34),
    "JUNGLE": (0, 100, 0),
    "ROCK": (138, 54, 15),
    "MOUNTAIN": (169, 169, 169),
    "SNOW": (255, 250, 250)
}

WIDTH = 200
HEIGHT = 200
FREQUENCY = 15.0

#### ISLAND CALCULATION ####
## Formula: ((e + a) * (1 - b*d**c)) ##

ISLAND_A = 0.05  # Pushes everything up
ISLAND_B = 1.00  # Pushes edges down
ISLAND_C = 1.50  # Controls how fast the dropdown is


def saveimg(elevation):
    """Save data to a bmp"""

    im = Image.new('RGB', (WIDTH, HEIGHT))
    for y in trange(0, HEIGHT, desc="Saving Image"):
        for x in range(0, WIDTH):
            color = decidebiome(elevation[y][x])
            im.putpixel((x, y), color)
    im.save('island.bmp')


class SimplexGenerator():
    def __init__(self, parent, height, length):
        self.parent = parent
        self.height = height
        self.length = length

    def noise(self, nx, ny, gen):
        """Rescale from -1.0:+1.0 to 0.0:1.0"""
        f = FREQUENCY
        return gen.noise2d(nx * f, ny * f) / 2.0 + 0.5

    def island(self, e, nx, ny):
        """Generate boundaries for island creation (ie. have water on all edges"""
        a = ISLAND_A  # Pushes everything up
        b = ISLAND_B  # Pushes edges down
        c = ISLAND_C  # Controls how fast the dropdown is
        d = 2 * math.sqrt(nx * nx + ny * ny)  # Distance from the centre
        return ((e + a) * (1 - b * d**c))

    def createelevation(self):
        """Create an elevation chart with "data" from simplex noise"""
        gen = OpenSimplex(random.randint(1, 99999))

        progress_bar = self.parent.ui.creationBar

        elevation = []
        progress_bar.setMaximum(self.height)
        for y in range(0, self.height):
            elevation.append([0] * self.length)
            for x in range(0, self.length):
                nx = x / self.length - 0.5
                ny = y / self.height - 0.5

                # Create uneven elevation points
                e0 = 1.00 * self.noise(1 * nx, 1 * ny, gen)
                e1 = 0.15 * self.noise(2 * nx, 2 * ny, gen)
                e2 = 0.05 * self.noise(4 * nx, 4 * ny, gen)

                e = e0 + e1 + e2
                e = self.island(e, nx, ny)
                elevation[y][x] = e
            progress_bar.setValue(y + 1)

        return elevation

    def decidebiome(self, e):
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


