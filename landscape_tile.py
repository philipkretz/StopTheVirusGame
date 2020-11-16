import pygame
import math


class LandscapeTile(object):
    img_url = './assets/iso-64x64-outside.png'
    tile_type = ''
    position = (0, 0)
    tile_position = (0, 0)
    size = (0, 0)
    blocking = False
    hiding = False
    image = None
    screen = None

    def is_hiding(self):
        return self.hiding

    def __init__(self, screen, tile_type, position):
        self.screen = screen
        self.tile_type = tile_type
        self.position = position
        if tile_type == 'antenna':
            self.img_url = './assets/antenna.png'
            self.size = (226, 225)
            self.tile_position = (0, 0)
            self.blocking = True
            self.hiding = True

        self.image = pygame.image.load(self.img_url).convert()

        if tile_type == 'tree1':
            self.size = (176, 150)
            self.tile_position = (450, 862)
            self.blocking = True
            self.hiding = True
        elif tile_type == 'tree2':
            self.size = (58, 105)
            self.tile_position = (130, 783)
            self.blocking = True
            self.hiding = True
        elif tile_type == 'tree3':
            self.size = (145, 120)
            self.tile_position = (275, 900)
            self.blocking = True
            self.hiding = True
        elif tile_type == 'tree4':
            self.size = (54, 109)
            self.tile_position = (196, 901)
            self.blocking = True
            self.hiding = True
        elif tile_type == 'tree5':
            self.size = (65, 117)
            self.tile_position = (131, 895)
            self.blocking = True
            self.hiding = True
        elif tile_type == 'plant1':
            self.size = (63, 63)
            self.tile_position = (65, 773)
            self.hiding = True
        elif tile_type == 'plant2':
            self.size = (64, 58)
            self.tile_position = (579, 703)
            self.hiding = True
        elif tile_type == 'plant3':
            self.size = (62, 64)
            self.tile_position = (575, 771)
            self.hiding = True
        elif tile_type == 'rock1':
            self.size = (60, 60)
            self.tile_position = (582, 332)
            self.hiding = True
        elif tile_type == 'rock2':
            self.size = (40, 43)
            self.tile_position = (392, 400)
            self.hiding = True
        elif tile_type == 'rock3':
            self.size = (57, 51)
            self.tile_position = (3, 461)
            self.hiding = True
        elif tile_type == 'water1':
            self.size = (54, 39)
            self.tile_position = (68, 668)
            self.blocking = True
        elif tile_type == 'water2':
            self.size = (55, 40)
            self.tile_position = (198, 603)
            self.blocking = True
        elif tile_type == 'water3':
            self.size = (56, 47)
            self.tile_position = (326, 601)
            self.blocking = True
        elif tile_type == 'ground1':
            self.size = (63, 35)
            self.tile_position = (2, 26)
        elif tile_type == 'ground2':
            self.size = (65, 42)
            self.tile_position = (130, 26)
        elif tile_type == 'ground3':
            self.size = (66, 37)
            self.tile_position = (385, 26)
        elif tile_type == 'rod1':
            self.size = (50, 50)
            self.tile_position = (259, 788)
            self.hiding = True
        elif tile_type == 'rod2':
            self.size = (53, 40)
            self.tile_position = (319, 797)
            self.hiding = True
        elif tile_type == 'grass1':
            self.size = (63, 53)
            self.tile_position = (3, 711)
            self.hiding = True
        elif tile_type == 'grass2':
            self.size = (57, 52)
            self.tile_position = (515, 716)
            self.hiding = True
        elif tile_type == 'grass3':
            self.size = (133, 56)
            self.tile_position = (64, 716)
            self.hiding = True
        elif tile_type == 'wall1':
            self.size = (66, 72)
            self.tile_position = (188, 255)
            self.hiding = True
            self.blocking = True
        elif tile_type == 'wall2':
            self.size = (65, 68)
            self.tile_position = (257, 313)
            self.hiding = True
            self.blocking = True
        elif tile_type == 'wall3':
            self.size = (65, 60)
            self.tile_position = (320, 449)
            self.hiding = True
            self.blocking = True

    def update(self):
        self.screen.blit(
            self.image.subsurface(
                (self.tile_position[0], self.tile_position[1], self.size[0], self.size[1])
            ),
            [self.position[0], self.position[1], self.size[0], self.size[1]]
        )

    def check_collision(self, character):
        if not self.blocking:
            return False

        character_pos = character.get_position()
        character_size = character.get_size()
        character_pos = (
            character_pos[0] + (character_size[0] / 2),
            character_pos[1] + (character_size[1] / 2)
        )

        dist = math.sqrt(
            math.pow(self.position[0] + (self.size[0] / 2) - character_pos[0], 2)
            + math.pow(self.position[1] + (self.size[1] / 2) - character_pos[1], 2)
        )

        if dist < (self.size[0] / 2 + self.size[1] / 2) / 2:
            return True
