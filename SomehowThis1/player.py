import world, items, random


class Player():
    def __init__(self):
        self.inventory = [items.CreditCard(15), items.Flask()]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False

    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)


    def is_alive(self):
        return self.hp > 0

    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Alcohol):
                if i.volume <= max_dmg:
                    self.inventory.remove(i)
                    print("\nYou've drank all of your {}\n".format(i.name))
                    break
                else:
                    max_dmg = i.volume
                    best_weapon = i


        print("You use {} against {}!\n".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.volume
        i.volume -= 3
        if not enemy.is_alive():
            print("You defeated {} for now!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])

    def retrace(self):
        print('You think really hard what you did last night, you were at a party\n')