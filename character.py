import pygame
from random import randint


class Character(object):
    img_url = ''
    position = (0, 0)
    size = (32, 36)
    direction = 0
    direction_tiles = (
        (0, 2),
        (3, 5),
        (6, 8),
        (9, 11),
    )
    speed = 2
    tile_img = None
    tilemap = []
    curr_tile_idx = 0
    screen = None
    map = None

    def __init__(self, screen, map, size):
        self.map = map
        self.screen = screen
        self.direction = randint(0, 3)
        self.curr_tile_idx = self.direction_tiles[self.direction][0]
        self.position = (randint(0, size[0] - self.size[0]), randint(0, size[1] - self.size[1]))
        self.tile_img = pygame.image.load(self.img_url).convert()

    def get_size(self):
        return self.size

    def get_position(self):
        return self.position

    def update(self, clock):
        if self.tile_img is None:
            return

        screen_size = pygame.display.get_surface().get_size()

        if self.position[0] < 0:
            self.position = (0, self.position[1])

        if self.position[1] < 0:
            self.position = (self.position[0], 0)

        if self.position[0] > screen_size[0]:
            self.position = (screen_size[0] - self.size[0], self.position[1])

        if self.position[1] > screen_size[1]:
            self.position = (self.position[0], screen_size[1] - self.size[1])

        self.screen.blit(self.tile_img.subsurface(self.tilemap[self.curr_tile_idx]),
                         [self.position[0], self.position[1], self.size[0], self.size[1]])

        if clock % 30 < 10:
            if self.curr_tile_idx >= self.direction_tiles[self.direction][1]:
                self.curr_tile_idx = self.direction_tiles[self.direction][0]
            else:
                self.curr_tile_idx = self.curr_tile_idx + 1

        if clock % 30 < 10:
            if self.direction == 0:
                self.position = (self.position[0] - self.speed, self.position[1] - self.speed)
            elif self.direction == 1:
                self.position = (self.position[0] + self.speed, self.position[1] - self.speed)
            elif self.direction == 2:
                self.position = (self.position[0] + self.speed, self.position[1] + self.speed)
            else:
                self.position = (self.position[0] - self.speed, self.position[1] + self.speed)

            hit_wall = (
                    self.position[0] < self.size[0]
                    or self.position[1] < self.size[1]
                    or self.position[0] > screen_size[0] - self.size[0]
                    or self.position[1] > screen_size[1] - self.size[1]
            )

            if not hit_wall:
                for tile in self.map.get_landscape_tiles():
                    hit_wall = tile.check_collision(self)

            if hit_wall:
                self.direction = (self.direction + 1) % 4
                secure_collision_dist = 5
                if self.direction == 0:
                    self.position = (self.position[0] - secure_collision_dist, self.position[1] - secure_collision_dist)
                elif self.direction == 1:
                    self.position = (self.position[0] + secure_collision_dist, self.position[1] - secure_collision_dist)
                elif self.direction == 2:
                    self.position = (self.position[0] + secure_collision_dist, self.position[1] + secure_collision_dist)
                else:
                    self.position = (self.position[0] - secure_collision_dist, self.position[1] + secure_collision_dist)

