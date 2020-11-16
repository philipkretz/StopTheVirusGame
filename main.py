import pygame
from map import Map
from player import Player

if not pygame.font:
    print('Fehler pygame.font Modul konnte nicht geladen werden!')
if not pygame.mixer:
    print('Fehler pygame.mixer Modul konnte nicht geladen werden!')


class Game(object):
    SCREEN_WIDTH = 1024
    SCREEN_HEIGHT = 768
    TEXT_COLOR = (178, 34, 34)
    hint = 'Hit all Covid 19-deniers with the cursor to send them into quarantine, before they can spread the virus!'
    hint_start_time = 0
    __instance = None

    # make it singleton
    def __new__(cls):
        if Game.__instance is None:
            Game.__instance = object.__new__(cls)
            Game.__instance.start()
        return Game.__instance

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        player = Player()
        game_map = Map()
        game_map.init(screen, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        pygame.display.set_caption("Stop The Virus")
        pygame.mouse.set_visible(1)
        pygame.mouse.set_cursor(*pygame.cursors.broken_x)
        pygame.key.set_repeat(1, 30)
        clock = pygame.time.Clock()
        hint_font = pygame.font.SysFont("comicsansms", 20)
        info_font = pygame.font.SysFont("comicsansms", 36)
        running = True

        while running:
            clock.tick(30)
            raw_time = pygame.time.get_ticks()
            game_map.check_actors(player.get_level(), raw_time)
            game_map.update(raw_time)

            if self.hint != '':
                if raw_time-self.hint_start_time > 15000:
                    self.hint = ''
                else:
                    textsurface = hint_font.render(self.hint, True, self.TEXT_COLOR)
                    screen.blit(textsurface, (25, 15))

            textsurface = info_font.render('Points: %s' % player.get_points(), True, self.TEXT_COLOR)
            screen.blit(textsurface, (self.SCREEN_WIDTH-textsurface.get_width()-25, self.SCREEN_HEIGHT-textsurface.get_height()-15))
            textsurface = info_font.render('Level: %s' % player.get_level(), True, self.TEXT_COLOR)
            screen.blit(textsurface, (25, self.SCREEN_HEIGHT-textsurface.get_height()-15))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_map.check_hit(pygame.mouse.get_pos())
            pygame.display.flip()


if __name__ == '__main__':
    Game()
