import numpy as np

# Class and instantiation(实例化).

# Making an object from a class is called instantiation,
# and you work with instances(实例) of a class.

### Creating a simple class - dog, which DESCRIBES a dog.
class Dog(object):
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Notes
'''
-------- The explanation of the structure above. --------

0. Some terms
    method: A function that is a part of a class.

1. The __init__() method
        A special method that creates automatically whenever we
    create a new instance based on the 'Dog' class.
        Leading and trailing underscores can prevent python from
    conflicting with users custom method names.

    ---- Parameters: ----
    self: required, comes first in defining methods, represents a instance.

2. Variables and values
        Pay attention, 'name' and 'dog' are values of the variable,
    or we can call them parameters, which will be regarded as arguments
    while python passes class Dog().

3. Variables defined in __init__() method
        Every variables should prefixed with self.
        For example, self.name = name will take the value associated with
    the parameter name (which is the second 'name'), then assigns it to
    the variable name (which is the first 'name').
        Variables that are accessible through instances like this
    are called 'attributes'(属性).

4. Other methods
        sit() and roll_over() are other methods. The methods which are
    defined under just 1 parameter 'self' don't need additional information
    to run. 
'''

# Making an instance from a class
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.\n")

# Calling methods
my_dog.sit()
my_dog.roll_over()
print()

# Creating multiple instances
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()



print("\n\n\n--------------- Car ----------------")
# Working with classes and instances.
### Setting a default value for an attribute.
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

print()
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# How to modifying attribute values?
### 1. Modifying directly through an instance.
print("\n1. Modifying directly through an instance.")
my_new_car.odometer_reading = 23
my_old_car = Car('honda', 'accord', 2016)
my_new_car.read_odometer()
my_old_car.read_odometer()

### 2. Modifying internally through a new method.
print("\n2. Modifying internally through a method.")
my_new_car.update_odometer(23)
my_new_car.read_odometer()
my_old_car.read_odometer()

### 3. Incrementing through a new method.
print("\n3. Incrementing through a new method.")
my_old_car.update_odometer(23_500)
my_old_car.read_odometer()
my_old_car.increment_odometer(100)
my_old_car.read_odometer()
my_new_car.read_odometer()

### Use class Subclass(Parentclass): to create a child class.
### Subclass will inherit EVERY functions in parent class.
print()
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
my_tesla.battery.describe_battery() # 2 layers of classes.
my_tesla.battery.get_range()

print()
my_new_tesla = ElectricCar('tesla', 'model 3', 2021)
print(my_tesla.get_descriptive_name())
# my_new_tesla.battery = Battery(100) # Change battery size in attribute 'battery'
my_new_tesla.battery.upgrade_battery(150)
my_new_tesla.battery.describe_battery()
my_new_tesla.battery.get_range()


### Subclass has higher priority level.
print()
my_old_car.fill_gas_tank()
my_tesla.fill_gas_tank()




# Exercise
print("\n\n\n--------------- Exercise ----------------")
class Restaurant(object):
    """Managing restaurants."""

    def __init__(self, name, cuisine):
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        name = self.restaurant_name
        cuisine = self.cuisine_type
        print(f"{name.title()} mainly makes {cuisine.title()}.")

    def open_restaurant(self):
        print("The restaurant is open now.")

    def customers_number(self):
        name = self.restaurant_name
        print(f"{name.title()} has served {self.number_served} customers.")

    def set_number_served(self, customers):
        if customers >= self.number_served:
            self.number_served = customers
        else:
            print("You can't set negative number of customers!")

    def increment_number_served(self, increments):
        if increments >= 0:
            self.number_served += increments
        else:
            print("You can't set negative number of customers!")

class IceCreamStand(Restaurant):
    """Managing ice cream stands."""

    def __init__(self, name, crusine='ice cream'):
        super().__init__(name, crusine)
        self.flavors = []

    def display_flavors(self):
        flavors = self.flavors
        print("\nThis ice cream stand provides these flavors:")
        for flavor in flavors:
            print(f" - {flavor.title()}")

restaurant = Restaurant('Coco', 'milk tea')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print()
restaurant.customers_number()
restaurant.number_served = 200
restaurant.customers_number()
restaurant.set_number_served(300)
restaurant.customers_number()
restaurant.increment_number_served(20)
restaurant.customers_number()

print()
icecreamStand = IceCreamStand('Haagen Dazs')
icecreamStand.describe_restaurant()
icecreamStand.open_restaurant()
icecreamStand.flavors = ['banana', 'blueberry', 'mango']
icecreamStand.display_flavors()


class User(object):
    """Managing users' profiles."""

    def __init__(self, first, last, age, location):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        name = f"{self.first_name} {self.last_name}"
        location = f"{self.location.title()}"
        print(f"\n{name.title()} is {self.age} years old, living in {location}.")

    def greet_user(self):
        name = f"{self.first_name} {self.last_name}"
        print(f"Hello, {name.title()}!")

    def show_login_attempts(self):
        print(f"Have tried {self.login_attempts} login attempts.")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    """Managing admin's profile."""

    def __init__(self, first, last, age, location):
        super().__init__(first, last, age, location)
        self.privilege = Privileges()

class Privileges(object):
    """Managing privileges of admin."""

    def __init__(self):
        self.privileges = ['can add post',
                           'can delete post',
                           'can ban user']

    def show_privileges(self):
        print("\nAdmin has privileges below:")
        privileges = self.privileges
        for privilege in privileges:
            print(f" - {privilege}")

user_0 = User('john', 'cage', 67, 'new york')
user_1 = User('alex', 'spencer', 37, 'london')
user_2 = User('graham', 'pinhey', 46, 'los angeles')
user_0.describe_user()
user_0.greet_user()
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()

print()
for i in range(1,11):
    user_0.increment_login_attempts()
    user_0.show_login_attempts()
user_0.reset_login_attempts()
user_0.show_login_attempts()

user_admin = Admin('admin', 'admin', 0, 'admin')
user_admin.privilege.show_privileges()







print("\n\n----------------------------------------")
class Circle(object): # 创建Circle类
    """Circle model."""
    pi = 3.14 # 类属性，通过'.'引用
    
    def __init__(self, R): # 初始化一个属性r（不要忘记self参数，他是类下面所有方法必须的参数）
        self.r = R # 表示给我们将要创建的实例赋予属性r赋值
    
    def get_area(self):
       """ 圆的面积 """
       # return self.r**2 * Circle.pi # 通过实例修改pi的值对面积无影响，这个pi为类属性的值
       # 在方法的内部调用实例属性需要采用 "self.属性名" 调用
       return self.r**2 * self.pi  # 通过实例修改pi的值对面积我们圆的面积就会改变

circle1 = Circle(1) # 1为赋的值，也就是说类的实例circle1中属性r的值为R=1
circle2 = Circle(2)

print(circle1.r)  # 使用 实例名.属性名 可以访问我们的属性
print(circle2.r)

print('----未修改前-----')
print('pi=\t', Circle.pi)
print('circle1.pi=\t', circle1.pi)  #  3.14
print('circle2.pi=\t', circle2.pi)  #  3.14

print('----通过类名修改后-----')
Circle.pi = 3.14159  # 通过类名修改类属性，所有实例的类属性被改变
print('pi=\t', Circle.pi)   #  3.14159
print('circle1.pi=\t', circle1.pi)   #  3.14159
print('circle2.pi=\t', circle2.pi)   #  3.14159

print('----通过circle1实例名修改后-----')
circle1.pi = 3.14111   # 实际上这里是给circle1创建了一个与类属性同名的实例属性
print('pi=\t', Circle.pi)     #  3.14159
print('circle1.pi=\t', circle1.pi)  # 实例属性的访问优先级比类属性高，所以是3.14111   
print('circle2.pi=\t', circle2.pi)  #  3.14159

print('----删除circle1实例属性pi-----')
del circle1.pi
print('pi=\t', Circle.pi)
print('circle1.pi=\t', circle1.pi)
print('circle2.pi=\t', circle2.pi)

# 调用方法 self不需要传入参数，不要忘记方法后的括号  输出 3.14
Circle.pi = 3.14 # 修改类属性
print(circle1.get_area())