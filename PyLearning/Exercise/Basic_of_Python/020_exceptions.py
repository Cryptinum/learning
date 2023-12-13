# Dealing with exceptions.

# Use try-except block to deal with 'ZeroDivisionError'
try:
    print(5/0)
except ZeroDivisionError: # If leads to a specific error, run code below.
    print("You can't divide by zero!")


# Use try-except block to prevent crash.
active = False
if active:
    print("Give me two numbers, and I'll divide them.")
    print("Enter 'q' to quit.")

    while active:
        first_number = input("\nFirst number: ")
        if first_number == 'q':
            break
        second_number = input("Second number: ")
        if second_number == 'q':
            break

        try:
            answer = int(first_number) / int(second_number)
        except ZeroDivisionError: # Prevent 0.
            print("You can't divide by zero!")
        except ValueError: # Prevent other characters.
            print("Invalid input, only numbers allowed!")
        else: # If try successfully, go to else block.
            print(answer)


# Handling missing files - 'FileNotFoundError'
filepath = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\020A_FileNotFoundError.txt'
try:
    with open(filepath, encoding='utf-8') as f:
        contents = f.read()
        print(contents)
except FileNotFoundError:
    print(f"Sorry, the file {filepath} does not exist.")


# Analyzing text.
# Working with multiple files.
def count_words(filepath):
    """Count the approximate number of words in a file."""

    try:
        with open(filepath, encoding='utf-8') as f:
            contents = f.read().lower() # Switch to lower case when reading file.
    except FileNotFoundError:
        print(f"Sorry, the file {filepath} does not exist.")
    else:
        # words = contents.split()
        words = ''.join(c for c in contents if c.isalnum() or c.isspace()).split()
        print(sorted(words))
        num_words = len(words)
        print(f"The file {filepath} has about {num_words} words.")

filepath = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\020B_pride.txt'
count_words(filepath)
filepath = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\020A_FileNotFoundError.txt'
count_words(filepath)





##### Exercise #####
print("\n########## Exercise ##########")
# 1. Simple Calculator
print("\n1. Simple Calculator")
active = False
if active:
    print("Please input 2 numbers: ")
    print("(Enter 'q' to quit program)")

    while active:
        first = input("First number: ")
        if first == 'q':
            break
        second = input("Second number: ")
        if second == 'q':
            break

        operator = input("Please select an operator(+,-,*,/): ")
        try:
            first = int(first)
            second = int(second)
            if operator == 'q':
                break
            elif operator == '+':
                print(f"{first} + {second} = {first+second}")
            elif operator == '-':
                print(f"{first} - {second} = {first-second}")
            elif operator == '*':
                print(f"{first} * {second} = {first*second}")
            elif operator == '/':
                print(f"{first} - {second} = {first/second}")
            else: # Prevent other operators.
                print("Invalid input, please input the given operators.")
        except ZeroDivisionError: # Prevent 0.
            print("You can't divide by zero!")
        except ValueError: # Prevent other characters.
            print("Invalid input, only numbers allowed!")
            
# 2. Cats & Dogs
print("\n2. Cats & Dogs")
cats = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\020C_ex_cats.txt'
dogs = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\020D_ex_dogs.txt'
missing = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\MISSING.txt'
files = [cats, dogs, missing]
def read_and_print(file):
    """Read and print the contents of a file."""

    try:
        with open(file) as f:
            contents = f.read()
            print(f"\nContents in '{file}':")
            print(contents)
    except FileNotFoundError:
        print(f"\n'{file}' is not exist, passed.")

for f in files:
    read_and_print(f)

# 3. Common words
print("\n3. Common words")
def common_words(file, specific_word):
    """Count how many times a word appears in a string"""

    try:
        with open(file, encoding='utf-8') as f:
            contents = f.read().lower() # Switch to lower to unify format.
    except FileNotFoundError:
        print(f"Sorry, the file {file} does not exist.")
    else:
        '''
        # words = contents.split()
        words = ''.join(c for c in contents if c.isalnum() or c.isspace()).split()
        # print(sorted(words))
        new_words = [word for word in words ]
        num_words = len(words)
        print(f"The file {file} has about {num_words} words.")
        '''
        times = contents.count(specific_word)
        print(f"{specific_word} appears about {times} times in file {file}.")

file = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\020B_pride.txt'
word = 'with ' # Add a space to prevent counting 'without' etc.
common_words(file, word)