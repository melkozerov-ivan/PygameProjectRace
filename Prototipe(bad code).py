import sys
import random

import pygame

from Loadings import load_image

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
tile_width = tile_height = 50


def generate_level(level):
    x, y = None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '#':
                Kill(x, y, )
    Tile('heart', 2, 1)
    return x, y


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    fon = pygame.transform.scale(load_image('start.png'), (500, 500))
    shr = pygame.font.Font(None, 50)
    txt0 = shr.render(str(f'Выберите на клавиатуре'), True, (0, 0, 0))
    txt01 = shr.render(str(f' кол-во игроков(1 или 2)'), True, (0, 0, 0))
    screen.blit(fon, (0, 0))
    screen.blit(txt0, (10, 10))
    screen.blit(txt01, (10, 50))
    e = True
    global players_count
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


def maximum():
    with open('res.txt', 'r') as file:
        a = list(map(int, file.readlines()))
    return max(a)


def write(result):
    with open('res.txt', 'r') as file:
        s = file.readlines()
    with open('res.txt', 'w') as file:
        s.append(str(result) + '\n')
        file.write(''.join(s))


def final_screen(players, cont):
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
    global players_count
    global playing
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


def generate_problems():
    num = random.randrange(1, 9)
    for i in range(num):
        Test(random.choice(problems), random.randrange(0, height), -20)


def load_level(filename):
    filename = filename
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y):
        super().__init__(anim_sprites)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        if self.cur_frame == 0:
            anim_sprites.remove(self)
        self.image = self.frames[self.cur_frame]


class Kill(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(kills_group)
        self.image = tile_images['problem1']
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, plr_image):
        super().__init__(player_group)
        self.xc = pos_x
        self.yc = pos_y
        self.image = random.choice(plr_image)
        self.rect = self.image.get_rect().move(self.xc, self.yc)

    def right(self, tick):
        self.rect.x += int(600 * tick / 1000)

    def left(self, tick):
        self.rect.x -= int(600 * tick / 1000)


class Problem(pygame.sprite.Sprite):
    def __init__(self, problem_type, pos_x, pos_y):
        super().__init__(problem_group)
        self.image = tile_images[problem_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Test(pygame.sprite.Sprite):
    def __init__(self, problem_type, pos_x, pos_y):
        super().__init__(test_group)
        self.image = tile_images[problem_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        if pygame.sprite.spritecollide(self, problem_group, False):
            pass
        else:
            Problem(problem_type, pos_x, pos_y)


tile_images = {
    'problem1': pygame.transform.scale(load_image('polcar.png'), (45, 75)),
    'problem2': pygame.transform.scale(load_image('longstrike.png'), (45, 75 * 3)),
    'problem3': pygame.transform.scale(load_image('moto.png'), (45, 45)),
    'problem4': pygame.transform.scale(load_image('time.png'), (35, 70)),
    'problem5': pygame.transform.scale(load_image('stairs.png'), (45, 75)),
    'problem6': pygame.transform.scale(load_image('twin1.png'), (45, 75)),
    'problem7': pygame.transform.scale(load_image('twin2.png'), (45, 75)),
    'problem8': pygame.transform.scale(load_image('pont.png'), (45, 70)),
    'problem9': pygame.transform.scale(load_image('family.png'), (45, 65)),
    'empty': pygame.transform.scale(load_image('asw.png'), (50, 50)),
    'heart': pygame.transform.scale(load_image('heart.png'), (50, 50))
}
problems = ['problem1', 'problem2', 'problem3', 'problem4', 'problem5', 'problem6', 'problem8', 'problem9',
            'problem7']
player_image = [pygame.transform.scale(load_image('player_car1.png', (255, 255, 255)), (35, 60)),
                pygame.transform.scale(load_image('player_car2.png', (255, 255, 255)), (35, 60)),
                pygame.transform.scale(load_image('player_car3.png', (255, 255, 255)), (35, 60)),
                pygame.transform.scale(load_image('player_car4.png', (255, 255, 255)), (35, 60))]

for i in tile_images.keys():
    tile_images[i].set_colorkey((255, 255, 255))
tile_images['heart'].set_colorkey((0, 0, 0))
bombirst = pygame.transform.scale(load_image("BOOM.png"), (750, 150))
bombirst.set_colorkey((255, 255, 255))

if __name__ == '__main__':
    players_count = 2
    kills_group = pygame.sprite.Group()
    tiles_group = pygame.sprite.Group()
    anim_sprites = pygame.sprite.Group()
    lvl = load_level('map.txt')
    level_x, level_y = generate_level(lvl)
    pygame.init()
    pygame.display.set_caption('Игра?')
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    font1 = pygame.font.Font(None, 50)
    running = True
    playing = True
    clock = pygame.time.Clock()
    start_screen()
    while running:
        if players_count == 1:
            count = 0
            hp = 10
            time = 0
            right = False
            left = False
            problem_group = pygame.sprite.Group()
            player_group = pygame.sprite.Group()
            player = Player(202, 350, player_image[0:2])
            while playing:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            left = True
                        elif event.key == pygame.K_RIGHT:
                            right = True
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            left = False
                        elif event.key == pygame.K_RIGHT:
                            right = False
                tic = clock.tick()
                if left:
                    if player.rect.x != 0:
                        player.left(tic)
                elif right:
                    if player.rect.x < width - 45:
                        player.right(tic)
                if player.rect.x < 0:
                    player.rect.x = 0
                for i in problem_group:
                    i.rect.y += 500 * tic / 1000
                exp = pygame.sprite.spritecollide(player, problem_group, True)
                if exp:
                    hp -= 1
                    AnimatedSprite(bombirst, 6, 1, *exp[-1].rect[:2])
                if hp == 0:
                    write(count)
                    final_screen(1, count)
                    break
                time += tic
                for i in kills_group:
                    if pygame.sprite.spritecollide(i, problem_group, True):
                        count += 1
                if time // 10 >= 10:
                    test_group = pygame.sprite.Group()
                    generate_problems()
                if time >= 220:
                    time = 0
                    anim_sprites.update()
                tiles_group.draw(screen)
                player_group.draw(screen)
                problem_group.draw(screen)
                anim_sprites.draw(screen)
                text1 = font1.render(str(count), True, (255, 255, 255))
                screen.blit(text1, (230, 60))
                text2 = font1.render(str(hp), True, (255, 0, 0))
                screen.blit(text2, (150, 60))

                pygame.display.update()
                pygame.display.flip()
        elif players_count == 2:
            count = 0
            hp = 10
            hp2 = 10
            time = 0
            right = False
            left = False
            right2 = False
            left2 = False
            problem_group = pygame.sprite.Group()
            player_group = pygame.sprite.Group()
            player = Player(202, 350, player_image[0:2])
            player2 = Player(202, 290, player_image[2:4])
            second = Tile('heart', 5, 1)
            while playing:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        terminate()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            left = True
                        elif event.key == pygame.K_RIGHT:
                            right = True
                        if event.key == pygame.K_a:
                            left2 = True
                        elif event.key == pygame.K_d:
                            right2 = True
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LEFT:
                            left = False
                        elif event.key == pygame.K_RIGHT:
                            right = False
                        if event.key == pygame.K_a:
                            left2 = False
                        elif event.key == pygame.K_d:
                            right2 = False
                tic = clock.tick()
                if left:
                    if player.rect.x >= 0:
                        player.left(tic)
                elif right:
                    if player.rect.x < width - 45:
                        player.right(tic)
                if left2:
                    if player2.rect.x >= 0:
                        player2.left(tic)
                elif right2:
                    if player2.rect.x < width - 45:
                        player2.right(tic)
                for i in problem_group:
                    i.rect.y += 500 * tic / 1000
                exp = pygame.sprite.spritecollide(player, problem_group, True)
                if exp:
                    hp -= 1
                    AnimatedSprite(bombirst, 6, 1, *exp[-1].rect[:2])
                if hp == 0:
                    final_screen(2, 2)
                    break
                exp2 = pygame.sprite.spritecollide(player2, problem_group, True)
                if exp2:
                    hp2 -= 1
                    AnimatedSprite(bombirst, 6, 1, *exp2[-1].rect[:2])
                if hp2 == 0:
                    final_screen(2, 1)
                    break
                time += tic
                for i in kills_group:
                    if pygame.sprite.spritecollide(i, problem_group, True):
                        count += 1
                if time // 10 >= 10:
                    test_group = pygame.sprite.Group()
                    generate_problems()
                if time >= 220:
                    time = 0
                    anim_sprites.update()
                tiles_group.draw(screen)
                player_group.draw(screen)
                problem_group.draw(screen)
                anim_sprites.draw(screen)
                text1 = font1.render(str(hp2), True, (255, 0, 0))
                screen.blit(text1, (300, 60))
                text2 = font1.render(str(hp), True, (255, 0, 0))
                screen.blit(text2, (150, 60))
                pygame.display.flip()
            pygame.sprite.spritecollide(second, tiles_group, True)
            Tile('empty', 5, 1)
