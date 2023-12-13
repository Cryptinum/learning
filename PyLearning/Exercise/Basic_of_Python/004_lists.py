# Square brackets indicate a list.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(f"bicycles = {bicycles}")
print(f"The number of element in the list 'bicycle' is {len(bicycles)}.")
print(bicycles[0])
print(bicycles[0].title()) # Use .title method.

'''
while True:
    i = input('Please enter a number no more than 4:')
    i = int(i) - 1
    if (i>=0 and i<=3):
        print(bicycles[i])
    else:
        print("Error.")
        break
'''

# Access the last element in a list without knowing where is the end.
print(bicycles[-1])

# Formatted invocation.
# i = int(input('Please enter a number no more than 4:'))
i = 3
message = f"My fisrt bicycle was a {bicycles[i].title()}"
print(message)

# Print all elements of the list.
friends = ['Zhao', 'Qian', 'Sun', 'Li']
i = 0
while i<=len(bicycles)-1: # Get the length of the list.
    print(friends[i])
    i += 1

# Print all elements of the list by using f-strings.
i = 0
while i<=len(bicycles)-1:
    print(f"Happy Birthday, {friends[i]}!")
    i += 1

# String can be converted into a list.
s = 'python'
s = list(s)
print(s)
print(s[:3])



print("----------------------------------------")
# Modifying elements in a list.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' # Changing.
print(motorcycles)

motorcycles.append('honda') # Adding to the end.
print(motorcycles)

motorcycles.insert(1, 'kawasaki') # Insert as the 2nd element.
print(motorcycles)

del motorcycles[1] # Knowing the position of the element. (index 1 is 'yamaha')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop() # Last element as default.
print(motorcycles)
print(popped_motorcycle) # We can access the popped element.

motorcycles = ['honda', 'yamaha', 'suzuki']
first_element = motorcycles.pop(0) # Pop the first element.
print(f"My fist motorcycle is a {first_element.title()}")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati') # Removing by value.
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")



print("----------------------------------------")
# Exercises
inviting = ['Zhao', 'Qian', 'Sun', 'Li']
i = 0
while i<=len(inviting)-1:
    print(f"I'd love to invite {inviting[i]} to eat dinner with me.")
    i += 1

i = len(inviting)-1
del inviting[i]
print(inviting)
inviting.append('Zhou')
print(inviting)
inviting.insert(0,'Wu')
inviting.insert(2,'Zheng')
inviting.append('Wang')
i = 0
while i<=len(inviting)-1:
    print(f"Hey {inviting[i]}, I've found a larger table for dinner!")
    i += 1

i = len(inviting)-1
while i>=2:
    sorry = inviting.pop()
    print(f"Sorry {sorry}, the table can't be delivered here in time.")
    i -= 1
print(inviting)
print("----------------------------------------")




# Organizing a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() # Sorted by dictionary. Permanently.
print(cars)
cars.sort(reverse=True) # Reversed
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars)) # Sorted temporarily.
print("\nHere is the original list again:")
print(cars)
print("\nHere is the reversedly sorted list:")
print(sorted(cars, reverse = True))

print("----------------------------------------")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars) # Simply reverse the list.

print("----------------------------------------")




# Exercises
locations = ['Beijing', 'Tokyo', 'Seoul', 'Pyongyang', 'Bankok']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)