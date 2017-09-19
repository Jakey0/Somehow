class Item():
    """The base class for all items"""

    def __init__(self, name, description, strength):
        self.name = name
        self.description = description
        self.strength = strength

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.strength)
class CreditCard(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="I can buy beers with this.".format(str(self.amt)),
                         strength=self.amt)
class Alcohol(Item):
    def __init__(self, name, description, strength, volume):
        self.volume = volume
        super().__init__(name, description, strength)

    def __str__(self):
        return "{}\n=====\n{}\nStrength: {}%\nVolume: {}".format(self.name, self.description, self.strength, self.volume)


class Flask(Alcohol):
    def __init__(self):
        super().__init__(name="Flask",
                         description="You've found a flask in your pocket, theres a bit of brandy left",
                         strength=30,
                         volume=5)


class Dagger(Alcohol):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger with some rust. Somewhat more dangerous than a rock.",
                         strength=10,
                         volume=10)