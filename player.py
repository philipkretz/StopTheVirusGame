

class Player(object):
    name = ''
    points = 0
    level = 1
    __instance = None

    # make it singleton
    def __new__(cls):
        if Player.__instance is None:
            Player.__instance = object.__new__(cls)
            Player.__instance.init()
        return Player.__instance

    def init(self):
        self.name = ''
        self.points = 0
        self.level = 1

    def set_name(self, name):
        self.name = name

    def increase_points(self, points):
        self.points += points

    def decrease_points(self, points):
        self.points -= points

    def raise_level(self):
        self.level += 1

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def get_level(self):
        return self.level



