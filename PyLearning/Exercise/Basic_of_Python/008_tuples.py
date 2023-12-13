# Tuples are immutable variables.

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Include a trailing comma to define a tuple with just 1 element.
my_tuple = (3,)

# Elements in tuples can be looped as elements in lists.
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# We can only change the value of tuple by assigning a new value.
# It will alse change the address of the tuple.
dimensions = (200, 50)
print(f"\nOriginal dimensions: {dimensions}, id = {id(dimensions)}")
dimensions = (400, 100)
print(f"Modified dimensions: {dimensions}, id = {id(dimensions)}")



# Exercises
menus = ('coffee', 'tea', 'pasta', 'soup', 'coke')
print("\nFirst menu:")
for menu in menus:
    print(menu)
menus = ('coffee', 'tea', 'rice', 'soup', 'juice')
print("\nSecond menu:")
for menu in menus:
    print(menu)
