# How to define functions.

# A function for displaying informations.
# username is a parameter(形参); user is an argument(实参)
def GREET_USR(username):
    """Display a simple greeting."""
    print(f"Hello! {username.title()}")

user = input("Please enter your username: ")
GREET_USR(user)

# Positional arguments and keyword arguments.
# Positional arguments.
def DESCRIBE_PET(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
DESCRIBE_PET('hamster', 'harry')
DESCRIBE_PET('dog', 'willie')

# Keyword arguments.
# When arguments inferred clearly, then order doesn't matter.
def DESCRIBE_PET(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
DESCRIBE_PET(animal_type='hamster', pet_name='harry')
DESCRIBE_PET(pet_name='willie', animal_type='dog')

# Default value.
# Set a default value in the function call.
# Must set default argument after non-default arguments.
def DESCRIBE_PET(pet_name, animal_type='cat'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
DESCRIBE_PET('miko')
DESCRIBE_PET('willie', 'dog') # Still can define animal_type.



# Let function returns value.
def FORMATTED_NAME(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"\n{first_name} {middle_name} {last_name}"
    else:
        full_name = f"\n{first_name} {last_name}"
    return full_name.title()
musician = FORMATTED_NAME('john', 'bach', 'sebastian')
print(musician)
musician = FORMATTED_NAME('john', 'cage') # Omit some positional arguments
print(musician)

# Returning a dictionary
print()
def PERSONAL_INFO(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age: # age = None then age is False
        person['age'] = age
    return person
musician = PERSONAL_INFO('john', 'cage', age=67)
print(musician)

# Call a function in a loop
def FORMATTED_NAME_2(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
active = False
while active:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    name = FORMATTED_NAME_2(f_name, l_name)
    print(f"\nHello, {name}!")
    label = input("\nExit?(y/n)")
    if label == 'y':
        active = False


# List and functions
print()
def GREET_USR(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
users = ['hannah', 'ty', 'margot']
GREET_USR(users)



# Make program more structured.
# Consider Line 50 Example 'Modify users' in 013_while_loop.py
# We can use functions to make our code more organized.
print()
def PRINT_MODELS(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def SHOW_COMPLETED_MODELS(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

PRINT_MODELS(unprinted_designs, completed_models)
SHOW_COMPLETED_MODELS(completed_models)



# Arbitrary number of arguments.
print()
def MAKE_PIZZA(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
MAKE_PIZZA('pepperoni')
MAKE_PIZZA('mushrooms', 'green peppers', 'extra cheese') # return a tuple

# We can also mixing positional and arbitrary arguments.
def SUMMARIZE_PIZZA(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
SUMMARIZE_PIZZA(16, 'pepperoni')
SUMMARIZE_PIZZA(12, 'mushrooms', 'green peppers', 'extra cheese')

# Arbitrary keyword arguments.
### use '**' to create an empty dictionary in function.
def PROFILE(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = PROFILE('albert', 'einstein',
                       location = 'princeton',
                       field = 'physics')
print(user_profile)
my_profile = PROFILE('david', 'stone',
                     location = 'shanghai',
                     field = 'math', 
                     birth = '3/4/1969')
print(my_profile)



# Exercise
def MAKE_SHIRT(size, text):
    """Print T-shirt size and a message."""
    print(f"\n{size}\n{text}")
MAKE_SHIRT('XL', 'MADE IN CHINA')
MAKE_SHIRT(size = 'M', text = 'MADE IN VIETNAM')


def MAKE_SHIRT(text, size='L'):
    """Print T-shirt size and a message."""
    print(f"\n{size}\n{text}")
MAKE_SHIRT('I LOVE PYTHON')

print()
def CITY_COUNTRY(city, country):
    """Print city and country of it."""
    print(f"{city.title()}, {country.title()}")
CITY_COUNTRY('beijing', 'china')
CITY_COUNTRY('bangkok', 'thailand')
CITY_COUNTRY('hanoi', 'vietnam')

albums = {}
def ALBUM_MANAGEMENT(albums, title, artist):
    """Managing info of my albums"""
    albums[title] = artist
active = False
while active:
    title = input("Title: ")
    artist = input("Artist: ")
    ALBUM_MANAGEMENT(albums, title, artist)
    label = input("Exit?(y/n)\n")
    if label == 'y':
        active = False
        print("\nAlbums I have:")
for title, artist in albums.items():
    print(f"{title.title()} -- by {artist.title()}")

print()
def SEND_MESSAGES(messages, send_messages):
    while messages:
        message = messages.pop()
        print(message)
        send_messages.append(message)
def SHOW_MESSAGES(messages):
    for message in messages:
        print(message)
greeting = ['Hello!', 'How are you?', 'Bye!']
sent_greeting = []
SEND_MESSAGES(greeting, sent_greeting)
SHOW_MESSAGES(sent_greeting)

def SANDWICHES(items):
    print("\nYou have ordered these sandwiches:")
    for item in items:
        print(f" - {item}")
items_0 = ['ham sandwich']
items_1 = ['ham sandwich', 'egg sandwich']
items_2 = ['ham sandwich', 'egg sandwich', 'vegetable sandwich']
SANDWICHES(items_0)
SANDWICHES(items_1)
SANDWICHES(items_2)

def SANDWICHES(*items):
    print("\nYou have ordered these sandwiches:")
    for item in items:
        print(f" - {item}")
SANDWICHES('ham sandwich')
SANDWICHES('ham sandwich', 'egg sandwich')
SANDWICHES('ham sandwich', 'egg sandwich', 'vegetable sandwich')

print()
def CARS_INFO(manufac, model, **car_info):
    car_info['manufacturer'] = manufac
    car_info['model name'] = model
    return car_info
car = CARS_INFO('subaru', 'outback', color='blue', tow_package=True)
print(car)