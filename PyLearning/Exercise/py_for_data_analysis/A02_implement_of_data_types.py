# Explicit changing.
def append_element(list, element):
    list.append(element)

data = [1, 2, 3]
print(data)
append_element(data, 4)
print(data)

# isinstance() function.
a = 4.5
b = 2
result_a = isinstance(a, (int, float)) # Can accept multiple types.
result_b = isinstance(b, (int, float))
print(result_a, result_b)

# Iterable object means it can be looped.
def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

s = 'a string'
l = [1, 2, 3]
i = 5
print(isiterable(s), isiterable(l), isiterable(i))

x = s
if not isinstance(x, list) and isiterable(x):
    x = list(x) # If x is an iterable object, turn it to a list.
print(x)

# We should be aware of the differences between 'is' and '=='.
a = [1, 2, 3]
b = a # Create a reference.
c = list(a) # Create a new list.
print(id(a), id(b), id(c))
print(a is b, a is c, a == c)

# Ternary expression, similar to list comprehension.
x = 5
s = 'Non-negative' if x >= 0 else 'Negative'
print(s)


##### STRINGS #####

# String is immutable in Python level.
# But we can convert it into a list then modify it.
s = 'this is a test string.'
try:
    s[10] = 'f'
except TypeError:
    print("We can't modify a string directly.")

s = list(s) # Convert to a list.
s[10] = 'f'
s = ''.join(s) # See 020 in Basic_of_Python.
print(s)

# .count()
c = """
    This is a longer string that
    spans multiple lines
    """
print(c.count('\n')) # c has 4 lines.

# .replace()
s = 'this is a test string.'
print(s)
s = s.replace('string', 'long string')
print(s)

# part of string and part of list.
s = 'python'
print(s[:3])
s = list(s)
print(s[:3])

# raw string.
s = r'this\has\no\special\characters'
s = list(s)
print(s) # one backslash turns to double backslashes.

# String format.
# See https://docs.python.org/3/library/string.html#format-string-syntax
template = '{0:.2f} {1:s} are worth US${2:d}'
s = template.format(4.5560, 'Argentine Pesos', 1)


##### BYTES #####

# decoded as a string.
val = 'español'
print(val)

# encode as different types.
val_utf8 = val.encode('utf-8')
print(val_utf8)
print(type(val_utf8)) # Turned into bytes type.

val_latin1 = val.encode('latin1')
val_utf16 = val.encode('utf-16')
val_utf16le = val.encode('utf-16le')
print(val_latin1, val_utf16, val_utf16le)
print(type(val_latin1), type(val_utf16), type(val_utf16le))

# create a byte object and decoding.
bytes_val = b'this is bytes'
print(bytes_val)
print(bytes_val.decode('utf8'))


##### BOOLEANS #####
print(True and True)
print(False and True)
print(False or True)
print(False or False)


##### NONETYPE #####
a = None
print(a is None) # None is None
b = 5
print(b is not None) # If a container has data inside, it won't be None.
ty = type(None)
print(ty) # None also have a data type for technical purpose.


##### DATETIME #####
from datetime import datetime, date, time
dt = datetime(2011, 10, 29, 20, 30, 21)
print(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
print(dt.date()) # Return a formatted date.
print(dt.time()) # Return a formatted time.

# Format a string as we want.
dt_formatted = dt.strftime('%m/%d/%Y %H:%M')
print(dt_formatted)

# Turn a formatted time into a datetime object.
dt_default = datetime.strptime(dt_formatted, '%m/%d/%Y %H:%M')
print(dt_default) # Print as default format.

# Count date difference.
dt1 = datetime(2011, 10, 29, 20, 30, 21)
dt2 = datetime(2011, 11, 15, 22, 30)
delta_t = dt2 - dt1
print(delta_t)
print(type(delta_t)) # Time difference is a datetime.timedata type of obj.