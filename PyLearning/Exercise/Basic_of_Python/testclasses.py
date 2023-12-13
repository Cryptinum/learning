import numpy as np

# The sample class in 016_classes_and_subclasses.py
class Car(object):
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Setting a default value

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def fill_gas_tank(self):
        """Print a message showing gas has been fulfilled."""
        print("Gas has been fulfilled!")

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage # Only infect a specific instance.
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

# Create a subclass of Car.
'''
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year) # Call method from parent class.
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size} kWh battery.")

    def fill_gas_tank(self): # Subclass has higher priority level.
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")
'''

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery() # Instance as attribute.

    def fill_gas_tank(self): # Subclass has higher priority level.
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

# Separate classes into smaller pieces to make code more readable.
class Battery(object):
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75): # 75 as default value.
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        battery_size = self.battery_size
        range = 328.437 * np.log(0.0160932 * battery_size + 1)
        print(f"This car can go about {range:.1f} miles on a full charge.")

    def upgrade_battery(self, battery_size):
        self.battery_size = battery_size