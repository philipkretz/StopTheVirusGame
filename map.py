from tinfoilhead import TinfoilHead
from citizen import Citizen
from player import Player
from landscape_tile import LandscapeTile


class Map(object):
    __instance = None

    # make it singleton
    def __new__(cls):
        if Map.__instance is None:
            Map.__instance = object.__new__(cls)
        return Map.__instance

    background_color = (110, 139, 61)
    landscape_tiles = []
    tinfoil_heads = []
    citizens = []
    size = ()
    screen = None

    def init(self, screen, width, height):
        self.screen = screen
        self.size = (width, height)
        self.init_landscape()

    def get_landscape_tiles(self):
        return self.landscape_tiles

    def init_landscape(self):
        self.landscape_tiles.append(LandscapeTile(self.screen, 'tree1', (500, 500)))
        self.landscape_tiles.append(LandscapeTile(self.screen, 'tree2', (10, 10)))
        self.landscape_tiles.append(LandscapeTile(self.screen, 'tree3', (800, 25)))
        self.landscape_tiles.append(LandscapeTile(self.screen, 'tree4', (100, 300)))
        self.landscape_tiles.append(LandscapeTile(self.screen, 'tree5', (300, 150)))
        self.landscape_tiles.append(LandscapeTile(self.screen, 'antenna', (50, 600)))
        self.landscape_tiles.append(LandscapeTile(self.screen, 'plant1', (150, 75)))
        self.landscape_tiles.append(LandscapeTile(self.screen, 'plant3', (750, 650)))
        self.landscape_tiles.append(LandscapeTile(self.screen, 'rod1', (400, 225)))
        self.landscape_tiles.append(LandscapeTile(self.screen, 'rod2', (550, 385)))
        self.landscape_tiles.append(LandscapeTile(self.screen, 'water1', (800, 485)))
        self.landscape_tiles.append(LandscapeTile(self.screen, 'water2', (200, 550)))

    def check_actors(self, level, clock):
        if clock % 30000 < 20:
            Player().raise_level()
            level = Player().get_level()

        for citizen in self.citizens:
            if citizen.get_removable():
                self.citizens.remove(citizen)
            else:
                for tinfoil_head in self.tinfoil_heads:
                    citizen.check_infected(tinfoil_head)

        for tinfoil_head in self.tinfoil_heads:
            if tinfoil_head.get_removable():
                self.tinfoil_heads.remove(tinfoil_head)

        citizen_count = 4 + 2 * level
        citizens_to_add = citizen_count - len(self.citizens)
        for _ in range(citizens_to_add):
            self.citizens.append(Citizen(self.screen, self, self.size))

        tinfoil_heads_count = 2 * level
        tinfoil_heads_to_add = tinfoil_heads_count - len(self.tinfoil_heads)
        for _ in range(tinfoil_heads_to_add):
            self.tinfoil_heads.append(TinfoilHead(self.screen, self, self.size))

    def draw_landscape(self, draw_hiding_objects):
        for tile in self.landscape_tiles:
            if draw_hiding_objects:
                if tile.is_hiding():
                    tile.update()
            else:
                if not tile.is_hiding():
                    tile.update()

    def update(self, clock):
        self.screen.fill(self.background_color)
        self.draw_landscape(False)

        for tinfoil_head in self.tinfoil_heads:
            tinfoil_head.update(clock)

        for citizen in self.citizens:
            citizen.update(clock)

        self.draw_landscape(True)

    def check_hit(self, pos):
        for tinfoil_head in self.tinfoil_heads:
            if (not tinfoil_head.get_hit()
                    and pos[0] >= tinfoil_head.position[0]
                    and pos[1] >= tinfoil_head.position[1]
                    and pos[0] <= tinfoil_head.position[0] + tinfoil_head.size[0]
                    and pos[1] <= tinfoil_head.position[1] + tinfoil_head.size[1]):
                tinfoil_head.set_hit()
                Player().increase_points(10)
