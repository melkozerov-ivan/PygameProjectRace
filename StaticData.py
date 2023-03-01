import pygame

from Loadings import load_image

tile_width = tile_height = 50
size = width, height = 500, 500
pygame.init()
screen = pygame.display.set_mode(size)

tile_images = {
    'problem1': pygame.transform.scale(load_image('polcar.png', (255, 255, 255)), (45, 75)),
    'problem2': pygame.transform.scale(load_image('longstrike.png', (255, 255, 255)), (45, 75 * 3)),
    'problem3': pygame.transform.scale(load_image('moto.png', (255, 255, 255)), (45, 45)),
    'problem4': pygame.transform.scale(load_image('time.png', (255, 255, 255)), (35, 70)),
    'problem5': pygame.transform.scale(load_image('stairs.png', (255, 255, 255)), (45, 75)),
    'problem6': pygame.transform.scale(load_image('twin1.png', (255, 255, 255)), (45, 75)),
    'problem7': pygame.transform.scale(load_image('twin2.png', (255, 255, 255)), (45, 75)),
    'problem8': pygame.transform.scale(load_image('pont.png', (255, 255, 255)), (45, 70)),
    'problem9': pygame.transform.scale(load_image('family.png', (255, 255, 255)), (45, 65)),
    'empty': pygame.transform.scale(load_image('asw.png', (255, 255, 255)), (50, 50)),
    'heart': pygame.transform.scale(load_image('heart.png', (0, 0, 0)), (50, 50))
}
problems = ['problem1', 'problem2', 'problem3', 'problem4', 'problem5', 'problem6', 'problem8', 'problem9', 'problem7']
player_image = [pygame.transform.scale(load_image('player_car1.png', (255, 255, 255)), (35, 60)),
                pygame.transform.scale(load_image('player_car2.png', (255, 255, 255)), (35, 60)),
                pygame.transform.scale(load_image('player_car3.png', (255, 255, 255)), (35, 60)),
                pygame.transform.scale(load_image('player_car4.png', (255, 255, 255)), (35, 60))]


bombirst = pygame.transform.scale(load_image("BOOM.png", (255, 255, 255)), (750, 150))
