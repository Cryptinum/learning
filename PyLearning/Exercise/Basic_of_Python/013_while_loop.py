# While loops

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

'''
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# Use flag to avoid comparison in while line.
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Exit a loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while 1:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
'''

# Use continue to skip.
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# While loop in lists and dictionaries.
# Start with users that need to be verified, 
#   and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = [] # confirmed_users is 'False'
while unconfirmed_users:
    current_user = unconfirmed_users.pop() # Remove from unconfirmed
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user) # Add to confirmed
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# Remove specific values.
'''
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
pet = input("Input a pet: ")
while pet in pets:
    pets.remove(pet)
print(pets)
'''

# A polling program
responses = {}
polling_active = False

while polling_active:
    # Prompt for the person's name and response.
    name = input("What is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store in dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

print("\n\n-----Exercises-----\n\n")
# Exercise
active = False
while active:
    age = int(input("\n(Enter 0 to quit.)\nPlease input your age: "))
    if age < 0:
        print("Invalid number, please enter again.")
    elif age == 0:
        break
    elif age < 3:
        print("The ticket is free.")
    elif age < 12:
        print("The ticket is $10.")
    else:
        print("The ticket is $15.")

sandwich_orders = ['ham sandwich', 'pastrami', 'salad sandwich',
                   'sausage sandwich', 'pastrami', 'pastrami']
finished_sandwiches = []
print("Sorry,the deli has run out of pastrami。")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich_order = sandwich_orders.pop()
    finished_sandwiches.append(sandwich_order)
    print(f"I made your {sandwich_order}.")

vacation = {}
active = True
while active:
    name = input("\nHello, would you tell me what is your name? ")
    location = input("And where would you like to spend your vacation? ")
    vacation[name] = location

    repeat = input("Anyone else? (y/n) ")
    if repeat == 'n':
        break
print("\n--- Poll Result ---")
for name, location in vacation.items():
    print(f"{name.title()} would like to go to {location.title()}")
