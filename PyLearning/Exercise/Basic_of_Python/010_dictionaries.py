# Dictionaries

# A dictionary is a collection of key-value pairs.
alien_0 = {'color' : 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

score = alien_0['points']
print(f"You've just earned {score} points!")

# Add new key-values to dictionaries.
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Modifying values in a dictionary.
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

# Start with an empty dictionary.
alien_0 = {}
print(alien_0)
alien_0['color'] = 'green'
alien_0['points'] = 5
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Removing key-value pairs
alien_0 = {'color' : 'green', 'points': 5}
print(f"Before: {alien_0}")
del alien_0['points']
print(f"After: {alien_0}")

# Storing more similar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
    }
language = favorite_languages['sarah'].title() # Invoke a value of key
print(f"Sarah's favorite language is {language}.")

# get() command: prevent errors when key is not exist.
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points')
print(point_value) # Returns 'None'.
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value) # Returns default sentence.

# Looping through a dictionary
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }
# Parentheses can be omitted.
for (key, value) in user_0.items():
    print(f"\nKey: {key}")
    print(f"value:{value}")
for (name, language) in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
    
# Looping keys only.
friends = ['phil', 'sarah', 'eric']
for name in friends:
    print(f"{name.title()}")
    if name in favorite_languages.keys():
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
    if name not in favorite_languages.keys():
        print(f"\t{name.title()}, please take our poll!")

# Looping keys is default behavior.
for name in favorite_languages:
    print(f"{name.title()}")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thanks for taking the poll.")

# Looping values only.
# Use set() to check for repeats.
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(f"{language.title()}")
languages = {'python', 'ruby', 'python', 'c'} # Use braces to create a set.

# Exercises
user_profile = {
    'first_name': 'David',
    'last_name': 'Rupert',
    'birth_y': 1988,
    'birth_m': 5,
    'birth_d': 18,
    'location': 'New York'
    }
fav_numbers = {
    'zhao': 1,
    'qian': 2,
    'sun': 3,
    'li': 4,
    'zhou': 5
    }
rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'amazon': 'brazil',
    'mississippi': 'america',
    'yenisey': 'russia',
    'yellow': 'china'
    }
for river in rivers:
    print(f"{river.title()} runs through {rivers[river].title()}.")
for country in rivers.values():
    print(f"{country.title()}.")