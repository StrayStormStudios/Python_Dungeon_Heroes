class Hero():
    def __init__(self, name):
        self.name = name
        self.health = 100;

    def set_health(self, new_health):
        self.health = new_health

    def __repr__(self):
        return "{} has {} hp".format(self.name, self.health)
