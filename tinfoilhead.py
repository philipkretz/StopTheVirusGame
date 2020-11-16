from character import Character
import time
import pygame


class TinfoilHead(Character):
    img_url = './assets/tinfoilhead.png'
    hit = False
    hit_time = 0
    fadeout_alpha = 225
    infection_radius = 50

    def __init__(self, screen, map, size):
        self.speed = 3
        self.size = (34, 48)
        self.direction_tiles = (
            (0, 12),
            (13, 25),
            (13, 25),
            (0, 12),
        )
        super().__init__(screen, map, size)

        self.tilemap = []
        for _ in range(13):
            self.tilemap.append([self.size[0] * _, 0, self.size[0], self.size[1]])

        for _ in range(13):
            self.tilemap.append([self.size[0] * _, self.size[1], self.size[0], self.size[1]])

    def get_infection_radius(self):
        return self.infection_radius

    def get_hit(self):
        return self.hit

    def set_hit(self):
        self.hit = True
        self.hit_time = int(round(time.time() * 1000))

    def get_removable(self):
        if self.hit and (int(round(time.time() * 1000)) - self.hit_time > 1000):
            return True
        return False

    def update(self, clock):
        if self.hit:
            if self.fadeout_alpha > 0:
                self.fadeout_alpha -= 5
            self.tile_img.set_alpha(self.fadeout_alpha)
        pygame.draw.circle(
            self.screen,
            (0, 250, 154),
            (self.position[0] + self.size[0] / 2,
             self.position[1] + self.size[1] / 2),
            self.infection_radius
        )

        Character.update(self, clock)
