# How to input.

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

# Multi-line string as prompt.
print()
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"Hello, {name.title()}")

# Numerical input.
age = int(input("\nHow old are you? "))
if age>=18:
    print(age)

# Modulo (output remainder)
a = int(input("\nPlease input an integer: "))
b = int(input("Please input another integer: "))
print(f"{a} % {b} = {a%b} ({b} * {int((a-(a%b))/b)} + {a%b} = {a})")

a = int(input("\nPlease input a number: "))
if a % 10 == 0:
    print(f"{a} is a multiple of 10.")
else:
    print(f"{a} is not a multiple of 10.")


# Exercise
car = input("\nWhat kind of car would you like? ")
print(f"Let me see if I can find you a {car.title()}.")