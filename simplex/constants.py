

biome = {
    "DEEPOCEAN": (0, 0, 80),
    "OCEAN": (0, 0,128),
    "SHORE": (255,193,37),
    "PLAINS": (100,200,112),
    "FOREST": (34,139,34),
    "JUNGLE": (0,100,0),
    "ROCK": (138,54,15),
    "MOUNTAIN": (169,169,169),
    "SNOW": (255, 250, 250)
}

WIDTH = 300
HEIGHT = 300
FREQUENCY = 10.0

#### ISLAND CALCULATION ####
## Formula: ((e + a) * (1 - b*d**c)) ##

ISLAND_A = 0.10 # Pushes everything up
ISLAND_B = 1.10 # Pushes edges down
ISLAND_C = 1.50 # Controls how fast the dropdown is