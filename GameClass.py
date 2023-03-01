import pygame

from SpriteClasses import AnimatedSprite, Tile, Player
from Terminate import terminate
from WriteRes import write
from Generators import generate_level, generate_problems
from StaticData import tile_images, player_image, bombirst
from Loadings import load_level
from Screens import start_screen, final_screen


class Game:
    def run(self):
        kills_group = pygame.sprite.Group()
        tiles_group = pygame.sprite.Group()
        lvl = load_level('map.txt')
        generate_level(lvl, tiles_group, kills_group, tile_images)
        pygame.init()
        pygame.display.set_caption('Игра?')
        size = width, height = 500, 500
        screen = pygame.display.set_mode(size)
        font1 = pygame.font.Font(None, 50)
        running = True
        playing = True
        clock = pygame.time.Clock()
        players_count = start_screen(screen)
        while running:
            if players_count == 1:
                anim_sprites = pygame.sprite.Group()
                count = 0
                hp = 10
                time = 0
                right = False
                left = False
                problem_group = pygame.sprite.Group()
                player_group = pygame.sprite.Group()
                player = Player(202, 350, player_group, player_image[0:2])
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
                        AnimatedSprite(bombirst, 6, 1, *exp[-1].rect[:2], anim_sprites)
                    if hp == 0:
                        write(count)
                        players_count, playing = final_screen(1, count, screen)
                        break
                    time += tic
                    for i in kills_group:
                        if pygame.sprite.spritecollide(i, problem_group, True):
                            count += 1
                    if time // 10 >= 10:
                        test_group = pygame.sprite.Group()
                        generate_problems(test_group, problem_group, tile_images)
                    if time >= 220:
                        time = 0
                        anim_sprites.update(anim_sprites)
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
                anim_sprites = pygame.sprite.Group()
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
                player = Player(202, 350, player_group, player_image[0:2])
                player2 = Player(202, 290, player_group, player_image[2:4])
                second = Tile('heart', 5, 1, tiles_group, tile_images)
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
                        AnimatedSprite(bombirst, 6, 1, *exp[-1].rect[:2], anim_sprites)
                    if hp == 0:
                        players_count, playing = final_screen(2, 2, screen)
                        break
                    exp2 = pygame.sprite.spritecollide(player2, problem_group, True)
                    if exp2:
                        hp2 -= 1
                        AnimatedSprite(bombirst, 6, 1, *exp2[-1].rect[:2], anim_sprites)
                    if hp2 == 0:
                        players_count, playing = final_screen(2, 1, screen)
                        break
                    time += tic
                    for i in kills_group:
                        if pygame.sprite.spritecollide(i, problem_group, True):
                            count += 1
                    if time // 10 >= 10:
                        test_group = pygame.sprite.Group()
                        generate_problems(test_group, problem_group, tile_images)
                    if time >= 220:
                        time = 0
                        anim_sprites.update(anim_sprites)
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
                Tile('empty', 5, 1, tiles_group, tile_images)


if __name__ == "__main__":
    game = Game()
    game.run()
