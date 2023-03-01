import pygame

from Max import maximum
from Terminate import terminate
from Loadings import load_image


def start_screen(screen):
    fon = pygame.transform.scale(load_image('start.png'), (500, 500))
    shr = pygame.font.Font(None, 50)
    txt0 = shr.render(str(f'Выберите на клавиатуре'), True, (0, 0, 0))
    txt01 = shr.render(str(f' кол-во игроков(1 или 2)'), True, (0, 0, 0))
    screen.blit(fon, (0, 0))
    screen.blit(txt0, (10, 10))
    screen.blit(txt01, (10, 50))
    e = True
    while e:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    players_count = 2
                    e = False
                    screen.fill((0, 0, 0))
                elif event.key == pygame.K_1:
                    players_count = 1
                    e = False
                    screen.fill((0, 0, 0))
        pygame.display.flip()
    return players_count


def final_screen(players, cont, screen):
    fon = pygame.transform.scale(load_image('final.png'), (500, 500))
    screen.blit(fon, (0, 0))
    shr = pygame.font.Font(None, 50)
    txt0 = shr.render(str(f'Выберите на клавиатуре'), True, (255, 255, 255))
    txt01 = shr.render(str(f' кол-во игроков(1 или 2)'), True, (255, 255, 255))
    screen.blit(txt0, (10, 10))
    screen.blit(txt01, (10, 50))
    if players == 1:
        txt = shr.render(str(f'Ваш счет {cont}'), True, (0, 0, 0))
        txt1 = shr.render(str(f'Ваш лучший счет - {maximum()}'), True, (170, 10, 10))
        screen.blit(txt, (30, 360))
        screen.blit(txt1, (80, 400))

    elif players == 2:
        txt = shr.render(str(f'Победил Игрок {cont}'), True, (0, 0, 0))
        screen.blit(txt, (30, 360))
    e = True
    playing = True
    while e:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    players_count = 2
                    e = False
                    screen.fill((0, 0, 0))
                elif event.key == pygame.K_1:
                    players_count = 1
                    e = False
                    screen.fill((0, 0, 0))
        pygame.display.flip()
    return players_count, playing
