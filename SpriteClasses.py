import random

import pygame

tile_width, tile_height = 50, 50


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, anim_sprites):
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

    def update(self, anim_sprites):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        if self.cur_frame == 0:
            anim_sprites.remove(self)
        self.image = self.frames[self.cur_frame]


class Kill(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, kills_group, tile_images):
        super().__init__(kills_group)
        self.image = tile_images['problem1']
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y, tiles_group, tile_images):
        super().__init__(tiles_group)
        self.image = tile_images[tile_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, player_group, plr_image):
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
    def __init__(self, problem_type, pos_x, pos_y, problem_group, tile_images):
        super().__init__(problem_group)
        self.image = tile_images[problem_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Test(pygame.sprite.Sprite):
    def __init__(self, problem_type, pos_x, pos_y, test_group, problem_group, tile_images):
        super().__init__(test_group)
        self.image = tile_images[problem_type]
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)
        if pygame.sprite.spritecollide(self, problem_group, False):
            pass
        else:
            Problem(problem_type, pos_x, pos_y, problem_group, tile_images)
