import random


# if conditions

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users: # Checking value not in a list.
    print(f"{user.title()}, you can post a response if you wish.\n")

'''
age = float(input("\nPlease enter your age: "))
while age>0:
    if age>=18:
        print("You're old enough to vote!")
    else:
        print("Sorry, you're too young to vote.")
    age = float(input("Please enter your age: "))
else:
    print("Invalid number.")

ticket = input("\nPlease enter your age: ")
while isinstance(ticket, int) or isinstance(ticket, float):
    ticket = float()
    while ticket>0:
        if ticket<4:
            price = 0
            break
        elif ticket<18:
            price = 25
            break
        elif ticket<65:
            price = 40
            break
        else:
            price = 20
            break
    else:
        print("Invalid number.")
        break
    print(f"The ticket price is ${price}.")
    ticket = input("Please enter your age: ")
else:
    print("Invalid input.")
'''

# Conditional loops.
toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in toppings:
    if topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {topping}.")
print("\nFinished making your pizza!")

# Check whether the list is empty or not.
toppings = []
if toppings:
    for topping in toppings:
        print(f"Adding {topping}.")
    print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?\n")

# Multiple lists.
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

# Exercises
alien_color = ['green', 'yellow', 'red']
alien = random.randint(0,2)
if alien_color[alien] == 'green':
    print(f"You just beat a {alien_color[alien]} alien and get 5 points.")
elif alien_color[alien] == 'yellow':
    print(f"You just beat a {alien_color[alien]} alien and get 10 points.")
elif alien_color[alien] == 'red':
    print(f"You just beat a {alien_color[alien]} alien and get 15 points.")

ages = []
for i in range(1,11):
    ages.append(random.randint(1,100))
for age in ages:
    if age<2:
        print(f"A person at age of {age} is a baby.")
    elif age<4:
        print(f"A person at age of {age} is a toddler.")
    elif age<13:
        print(f"A person at age of {age} is a kid.")
    elif age<20:
        print(f"A person at age of {age} is a teenager.")
    elif age<65:
        print(f"A person at age of {age} is a adult.")
    else:
        print(f"A person at age of {age} is an elder.")

users = ['admin', 'zhao', 'qian', 'sun', 'li']
if users:
    for user in users:
        if user is 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    print("We need to find somme users!")

print()
current_users = ['admin', 'boris', 'cathy', 'david', 'emily']
new_users = ['felix', 'garthe', 'Boris', 'harry', 'david']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"The username {new_user.title()} has already exist.")
    else:
        print(f"Username {new_user.title()} is avaliable.")
print("Finished.\n")

numbers = [i for i in range(1,10)]
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")