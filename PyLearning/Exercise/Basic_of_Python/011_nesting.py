# Nesting is lists of dictionaries.

# Examples of nesting: dictionaries in a list.
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Generate new aliens in list aliens.
print()
aliens = []
for alien_number in range(30): # Create 30 new aliens.
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]: # Change values of first 3 aliens.
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
for alien in aliens[:5]: # Show the first 5 aliens.
    print(alien)
print(f"......Total number of aliens: {len(aliens)}")


# Examples of nesting: lists in a dictionary.
print()
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
print(f"You ordered a {pizza['crust']}-crust pizza"
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite languages is:")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

languages = []
for name in favorite_languages: # Show all mentioned languages.
    for language in favorite_languages[name]:
        languages.append(language)
print(f"Mentioned languages: {sorted(set(languages))}")


# Examples of nesting: dictionaries in a dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    # Inner layer
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFullname: {full_name.title()}")
    print(f"\tLocation: {location.title()}")



# Exercises
print("\n**********Exercises**********\n")
user_0 = {
    'first_name': 'david',
    'last_name': 'rupert',
    'birth_y': 1988,
    'birth_m': 5,
    'birth_d': 18,
    'location': 'new york'
    }
user_1 = {
    'first_name': 'john',
    'last_name': 'ross',
    'birth_y': 1962,
    'birth_m': 7,
    'birth_d': 3,
    'location': 'london'
    }
user_2 = {
    'first_name': 'lucas',
    'last_name': 'quinn',
    'birth_y': 1994,
    'birth_m': 11,
    'birth_d': 27,
    'location': 'berlin'
    }
people = [user_0, user_1, user_2]
for person in people:
    name = f"{person['first_name']} {person['last_name']}"
    birth = f"{person['birth_m']}/{person['birth_d']}/{person['birth_y']}"
    location = f"{person['location'].title()}"
    print(f"{name.title()} was born in {birth}, lives in {location} now.")
    
print()
pet_0 = {
    'name': 'mike',
    'species': 'cat',
    'owner': 'yukina',
    }
pet_1 = {
    'name': 'tama',
    'species': 'cat',
    'owner': 'yukina',
    }
pet_2 = {
    'name': 'suama',
    'species': 'cat',
    'owner': 'yukina',
    }
pets = [pet_0, pet_1, pet_2]
for pet in pets:
    name = f"{pet['name'].title()}"
    own = f"{pet['owner'].title()}"
    spec = f"{pet['species'].title()}"
    print(f"{name} fed by {own} is a {spec}.")

print()
favorite_places = {
    'david': ['beijing', 'london'],
    'mike': ['paris', 'tokyo', 'new york'],
    'john': ['london', 'shanghai', 'sydney'],
    'joe': ['new york', 'paris', 'london'],
    'nancy': ['shanghai'],
    }
for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"\n{name.title()}'s favorite place is:")
    else:
        print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")

print()
musicians = {
    'wamozart': {
        'first': 'wolfgang',
        'middle': 'amadeus',
        'last': 'mozart',
        'location': 'germany'
        },
    'jsbach': {
        'first': 'johann',
        'middle': 'sebastian',
        'last': 'bach',
        'location': 'germany'
        },
    'ffchopin': {
        'first': 'frederic',
        'middle': 'francois',
        'last': 'chopin',
        'location': 'poland'
        },
    }

def MUSICIAN_INFO(dictionary):
    for musician, info in dictionary.items():
        name = f"{info['first']} {info['middle']} {info['last']}"
        location = f"{info['location'].title()}"
        print(f"{name.title()} lives in {location}.")

MUSICIAN_INFO(musicians)

print()
new_musician = {}
new_musician['first'] = 'georg'
new_musician['middle'] = 'friedrich'
new_musician['last'] = 'handel'
new_musician['location'] = 'london'
musicians['gfhandel'] = new_musician

MUSICIAN_INFO(musicians)