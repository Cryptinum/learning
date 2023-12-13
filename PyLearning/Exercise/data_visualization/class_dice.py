from random import randint

class Dice(object):
    """A class representing a single dice."""

    def __init__(self, num_sides=6):
        """Assume a n-sided dice."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number od sides."""
        return randint(1, self.num_sides)