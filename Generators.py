import random

from SpriteClasses import Kill, Tile, Test
from StaticData import height, problems


def generate_level(level, tiles_group, kills_group, tile_images):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y, tiles_group, tile_images)
            elif level[y][x] == '#':
                Kill(x, y, kills_group, tile_images)
    return x, y


def generate_problems(test_group, problem_group, tile_images):
    num = random.randrange(1, 9)
    for i in range(num):
        Test(random.choice(problems), random.randrange(0, height), -20, test_group, problem_group, tile_images)
