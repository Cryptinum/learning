# A introduction of python standard library.

from random import randint, choice

a = randint(1, 6)
print(a)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

# Exercises:

# 1. Dice
class Die(object):
    """Simulate a custom sides dice."""

    def __init__(self, side=6):
        self.side = side

    def roll_die(self):
        side = self.side
        result = randint(1, side)
        print(f"\nRolled {result} in {side} sides.")

die = Die() # Simulate a 6-sides dice.
die.roll_die()
die_10 = Die(10) # Simulate a 10-sides dice.
die_10.roll_die()
die_20 = Die(20) # Simulate a 20-sides dice.
die_20.roll_die()

# 2. Lottery
class Lottery(object):
    """Simulate a lottery."""

    def __init__(self, num_1, num_2=0):
        self.part_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.part_2 = ['a', 'b', 'c',' d', 'e']
        self.num_1 = num_1
        self.num_2 = num_2

    def draw_part_1(self):
        num_1 = self.num_1 + 1
        part_1 = self.part_1
        chosen_1 = []
        for i in range(1,num_1):
            select = choice(part_1)
            chosen_1.append(select)
            part_1.remove(select)
        chosen_1.sort()
        return chosen_1

    def draw_part_2(self):
        num_2 = self.num_2 + 1
        part_2 = self.part_2
        chosen_2 = []
        for i in range(1,num_2):
            select = choice(part_2)
            chosen_2.append(select)
            part_2.remove(select)
        chosen_2.sort()
        return chosen_2

    def draw(self):
        chosen_1 = self.draw_part_1()
        chosen_2 = self.draw_part_2()
        chosen = chosen_1 + chosen_2
        return chosen

my_lottery = [3, 4, 7, 8, 'b']
my_draw = []
j = 0
while my_lottery != my_draw:
    lottery = Lottery(4, 1)
    my_draw = lottery.draw()
    j += 1
print(f"\nDraw {j} times to win the prize.")

# 3. 