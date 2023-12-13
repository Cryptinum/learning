# Work with files and saving data.

# Python looks for file in open() then returns an object representing the file.
# By assigning it as file_object, we can work with it later in the program.

# By 'with' structure, we can prevent writing open() function,
#   all of our code in the 'with' structure will be executed,
#   after python pass all the code in 'with' structure,
#   the file will also be closed by python automatically.

# Use read() method to read and store it in 'contents'.
# read() will return an empty string when reaches the end of the file.

##### Read files #####

# Use rstrip() method to remove extra blank line.
with open('D:/Projects/Pylearning/Exercise/Basic_of_Python/019A_pi_30.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# Custom absolute file path.
# Use forward slash for displaying file paths in python.
file_path = 'D:/Projects/Pylearning/Exercise/Basic_of_Python/019A_pi_30.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# Reading text file line by line.
# This method will make extra blank lines, using rstrip() to remove them.
file_path = 'D:/Projects/Pylearning/Exercise/Basic_of_Python/019A_pi_30.txt'
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

# Making a list of lines from a file.
# Use readlines() method to read every lines and assign as a list.
file_path = 'D:/Projects/Pylearning/Exercise/Basic_of_Python/019A_pi_30.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print(lines)



# Working with a file's contents.
file_path = 'D:/Projects/Pylearning/Exercise/Basic_of_Python/019A_pi_30.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip() # save contents into pi_string without spaces.

print(pi_string)
print(len(pi_string))

# Open and copy a big file.
file_path = 'D:/Projects/Pylearning/Exercise/Basic_of_Python/019B_pi_1m.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:53]}...") # Print first 50 digits of pi.
print(len(pi_string))

# Check if a specific number in pi.
file_path = 'D:/Projects/Pylearning/Exercise/Basic_of_Python/019B_pi_1m.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = '102198'
if birthday in pi_string: # 直接一个in，十分暴力
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")





##### Write to files #####

# Use 'w' option to open a file in write mode.
# Caution: Use empty file to do experiments.
### 'r': read mode; 'w': write mode; 'a': append mode
### 'r+': read & write mode
### read-only mode by default
filepath = 'D:\\Projects\\PyLearning\\Exercise\\Basic_of_Python\\019C_write_file.txt'

''' The code below will sweep away everything in your file.
with open(filepath, 'w') as file_object:
    pass
'''

# Use write mode.
with open(filepath, 'w') as file_object:
    file_object.write("I love programming.\n") # Use new line character.
    file_object.write("I love creating new games.\n")

# Use append mode.
with open(filepath, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")





##### Exercise #####
print()

# 1. Create a file, then read and print it in a specific format.
exercise = 'D:/Projects/Pylearning/Exercise/Basic_of_Python/019M_excercise_1.txt'
with open(exercise) as file:
    lines = file.readlines()

print(lines[0].strip()) # Print Line 1
for line in lines[1:]: # Print other lines in a specific format.
    print(f" - {line.strip()}")

# 2. replace() method - It is temporary.
print(lines[0].replace('Python', 'C').strip()) # Change 'Python' to 'C'
for line in lines[1:]:
    print(f" - {line.strip()}")

# 3. Save username in a file.
filepath = 'D:/Projects/Pylearning/Exercise/Basic_of_Python/019N_excercise_3.txt'
with open(filepath, 'a') as file:
    active = 'n'
    while active != 'y':
        username = input("Please input your username: ")
        print(f"Have a nice day, {username.title()}")
        file.write(username+'\n')
        active = input("Quit? (y/n) ")