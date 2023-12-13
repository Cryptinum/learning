import random as rand


# Storing data.

numbers = []
for i in range(1,6):
    numbers.append(rand.randint(1,20))
numbers.sort()
'''
for i in range(1,21):
    times = numbers.count(i)
    print(f"{i} appears about {times} times.")
'''

# Using json module.
import json

filepath = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\021A_numbers.txt'
with open(filepath, 'w') as f:
    json.dump(numbers, f)
    print(f"\nsave as {numbers}")

with open(filepath) as f:
    numbers = json.load(f)
    print(f"\nload as {numbers}")

# Write and read custom text.
filepath = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\021B_customtext.json'
username = ''
with open(filepath, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}!")

with open(filepath) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")

# Combining as one part.
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filepath = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\021B_customtext.json'
try:
    with open(filepath) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("\nWhat is your name? ")
    with open(filepath, 'w') as f:
        json.dump(username, f)
        print(f"\nWe'll remember you when you come back, {username}!")
else:
    print(f"\nWelcome back, {username}!")



# Refactoring as functions.
def verify_username():
    """Verify if this is the correct username."""
    username = input("What is your name? ")
    return username

def get_stored_username():
    """Get stored username if available."""
    filepath = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\021C_greetuser.json'
    try:
        with open(filepath) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username(username): # Prevent "" (None)
    """Prompt for a new username."""
    filepath = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\021C_greetuser.json'
    with open(filepath, 'w') as f:
        json.dump(username, f)

def greet_user():
    """Greet the user by name."""
    stored_username = get_stored_username()
    my_username = verify_username()
    if my_username == stored_username:
        print(f"\nWelcome back, {my_username}!")
    else:
        get_new_username(my_username)
        print(f"\nWe'll remember you when you come back, {my_username}!")

greet_user()



##### Exercise #####
print("\n########## Exercise ##########")

# 1. Favorite number
print("\n1. Favorite number")

def read_number():
    """Read number from a file."""
    filepath = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\021D_ex1.json'
    while True:
        try:
            with open(filepath) as f:
                number = json.load(f)
                if number.isdigit() == True:
                    return number
                else:
                    store_number()
        except FileNotFoundError:
            return None

def store_number():
    """Store input number into a file."""
    filepath = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\021D_ex1.json'
    while True:
        number = input("Please input your lucky number: ")
        if number.isdigit() == True: # Judge whether is a number.
            with open(filepath, 'w') as f:
                json.dump(number, f)
            break
        else:
            print("Only numbers are allowed to input! Please try again.")
            continue

def lucky_number():
    """Show lucky number which stored in a file in advance."""
    number = read_number()
    if number:
        print(f"I know your lucky number! It’s {number}!")
    else:
        store_number()
        print(f"Successfully stored.")

lucky_number()