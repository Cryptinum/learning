# Import classes from a file.


from testclasses import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


import testclasses as car

my_beetle = car.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())
my_tesla = car.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())


from testclasses import * # not recommended

my_tesla = ElectricCar('tesla', 'model 3', 2019)
my_tesla.battery.upgrade_battery(150)
my_tesla.battery.get_range()
