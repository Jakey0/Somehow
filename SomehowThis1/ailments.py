class Ailment:
    def __init__(self, name, hp, damage, duration):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.duration = duration

    def is_suffering(self):
        return self.hp > 0
    def is_lingering(self):
        return self.duration > 0

class Hangover(Ailment):
    def __init__(self):
        super().__init__(name="Hangover", hp=6, damage=1, duration = 7)

