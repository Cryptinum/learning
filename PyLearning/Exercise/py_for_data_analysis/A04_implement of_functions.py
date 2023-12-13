##### Global and Local variable. #####
def func():
    a = []
    for i in range(5):
        a.append(i)
func() # Execute the function first.
try:
    print(a)
except NameError:
    print("'a' is not defined.")
    
def func():
    global a
    a = []
    for i in range(5):
        a.append(i)
func() # Execute the function first.
try:
    print(a)
except NameError:
    print("'a' is not defined.")




##### Function are objects. #####
# Data washing
states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
          'south carolina##', 'West virginia?']
import re
from typing import final
def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip() # Remove spaces and tabs.
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result
result = clean_strings(states)
print(result)

def remove_punctuation(value):
    return re.sub('[!#?]', '', value)
clean_ops = [str.strip, remove_punctuation, str.title]

def clean_strings(strings, operators):
    result = []
    for value in strings:
        for function in operators:
            value = function(value)
        result.append(value)
    return result
result = clean_strings(states, clean_ops)
print(result)

for x in map(remove_punctuation, states):
    print(x)




##### Anonymous function. #####

# We need not to define a function in standard format if it is simple enough.
def short_function(x):
    return x * 2
# It is equivalent as the expression below:
equiv_anon_func = lambda x: x ** 2

ints = [4, 0, 1, 5, 6]
squared1 = [equiv_anon_func(x) for x in ints]
print(squared1)

# For tidier format:
squared2 = map(lambda x: x ** 2, ints)
print(list(squared2))

# Tidiest:
squared3 = [x ** 2 for x in ints]
print(squared3)

# More example.
# Sort by the number of distinct letters.
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x: len(set(list(x))))
print(strings)




##### Partial argument application #####
def add_numbers(x, y):
    return x + y

# Essentially, we define a new function called add_five.
add_five = lambda y: add_numbers(5, y) # Equivalent to the function below.
def add_five_equiv(y):
    return add_numbers(5, y)
print(add_five(9))
print(add_five_equiv(9))

# Simplify.
from functools import partial
add_five_simp = partial(add_numbers, 5)
print(add_five_simp(9))




##### Generators #####
some_dict = {'a': 1, 'b': 2, 'c': 3}
for key in some_dict:
    print(key)

# The process above, precisely, in 'for key in some_dict'
dict_iterator = iter(some_dict) # Create an iterator.
# An iterator is any object that will yield objects to the Python
#   interpreter when used in a context like a for loop.

print(dict_iterator)
print(list(dict_iterator))

# Create a generator.
def squares(n=10):
    print(f'Generating squares from 1 to {n ** 2}')
    for i in range(1, n + 1):
        yield i ** 2 # Use yield instead of return.

gen = squares()
print(gen)
# print(list(gen)) # Include print() inside the function. gen = list(gen)

for i in gen:
    print(i, end=' ') # Default as end='\n'
print('\n')

# Generator expressions.
# Similar to list comprehensions, but we use parentheses instead.
# *** BECAUSE THERE IS NO 'TUPLE COMPREHENSION'. ***
gen = (x ** 2 for x in range(100))
print(gen)

sum1 = sum(x ** 2 for x in range(100)) # Generator method.
print(sum1)
sum2 = sum([x ** 2 for x in range(100)]) # List comprehension method.
print(sum2)

dict1 = dict((i, i**2) for i in range(5))
print(dict1)
dict2 = {i:i**2 for i in range(5)} # Same.
print(dict2)

# itertools module.
import itertools
first_letter = lambda x: x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names)) # Names is a generator.




##### TRY BLOCK #####

# finally block
try:
    float('string')
except:
    print('Error.')
else:
    print('Success.')
finally:
    print('End.')




##### FILES #####

# with list comprehension.
path = r'D:\Projects\PyLearning\Exercise\py_for_data_analysis\A04A_pride.txt'
lines = [x.rstrip() for x in open(path)]

f1 = open(path)
print(f1.read(100))
print(f1.tell())
f1.close()

f2 = open(path, 'rb') # Open as binary mode.
print(f2.read(100))
print(f2.tell()) # Bytes read.
f2.close()

# Byte and Unicode.
import sys
path = r'D:\Projects\PyLearning\Exercise\py_for_data_analysis\A04A_pride.txt'
with open(path) as f:
    coding = sys.getdefaultencoding() # Return coding method.
    print(coding)

with open(path, 'rb') as f:
    data = f.read(100)
    print(data)

# functions.
'''
    read([size])
    readlines([size])
    write(str)
    writelines(str)
    close()
    flush()
    seek([int: position])
    tell()
    closed
'''