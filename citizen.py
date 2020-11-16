from character import Character
from player import Player
import time
import math
from random import randint


class Citizen(Character):
    infected = False
    img_url = ''
    infect_time = 0
    character_idx = 0
    fadeout_alpha = 225

    def __init__(self, screen, map, size):
        self.speed = 3
        self.size = (32, 32)
        self.character_index = randint(0, 6)
        self.img_url = './assets/hospital_set_jestan/hospital_npcs_' + str(self.character_index) + '.png'
        self.direction_tiles = (
            (12, 15),
            (8, 11),
            (8, 11),
            (4, 7),
        )
        super().__init__(screen, map, size)

        self.tilemap = []
        for y in range(4):
            for x in range(4):
                self.tilemap.append(
                    [
                        self.size[0] * x,
                        self.size[1] * y,
                        self.size[0],
                        self.size[1]
                    ]
                )

    def get_infected(self):
        return self.infected

    def set_infected(self):
        self.infected = True
        self.infect_time = int(round(time.time() * 1000))

    def get_removable(self):
        if self.infected and (int(round(time.time() * 1000)) - self.infect_time > 3000):
            return True
        return False

    def check_infected(self, infector):
        if self.infected:
            return

        infector_pos = infector.get_position()
        infector_size = infector.get_size()
        infector_pos = (
            infector_pos[0] + (infector_size[0] / 2),
            infector_pos[1] + (infector_size[1] / 2)
        )
        infection_radius = infector.get_infection_radius()
        dist = math.sqrt(
            math.pow(self.position[0] + (self.size[0] / 2) - infector_pos[0], 2)
            + math.pow(self.position[1] + (self.size[1] / 2) - infector_pos[1], 2)
        )

        if dist < infection_radius:
            self.set_infected()
            Player().decrease_points(5)

    def update(self, clock):
        if self.infected:
            if self.fadeout_alpha > 0:
                self.fadeout_alpha -= 5
            self.tile_img.set_alpha(self.fadeout_alpha)

        Character.update(self, clock)
