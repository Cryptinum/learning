##### TUPLE #####

# Create.
tup = 4, 5, 6
print(tup)
tup = (4, 5, 6)
print(tup)
nested_tup = tup, (7, 8) # A nested tuple.
print(nested_tup)

new_tup = nested_tup + tup # Concatenate tuples.
print(new_tup)

tup = tup * 4 # Tuples can be 'multiplied'.
print(tup)

# Unpack.
tup = 4, 5, 6
a, b, c = tup
print(f'a={a}, b={b}, c={c}')

b, c, a = a, b, c
print(f'a={a}, b={b}, c={c}') # Swap variable easily.

values = 1, 2, 3, 4, 5
a, b, *rest = values
print(a, b, rest) # Partly unpack by using * expression.
print(a, b, *rest) # rest and *rest is not same.

seq = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
for a, b, c in seq:
    print(f'a={a}, b={b}, c={c}') # Loop through a packed tuple.

# Convert any iterator into a tuple.
s = 'test string'
print(tuple(s))
l = [1, 2, 3, 4, 's', 'o', None]
print(tuple(l))

# We can't change the elements in a tuple. (In Python layer.)
tup = tuple(['foo', [1, 2], True])
try:
    tup[2] = False
except TypeError:
    print("We can't change the elements in a tuple.")

tup[1].append(False) # But we can modify lists in a tuple
print(tup)
tup[1].pop()
print(tup)




##### DEQUES #####
from collections import deque
from pickletools import string1

deq = deque([1, 2, 3, 4, 5])
print(deq)
deq.append(7)
print(deq)
deq.appendleft(9) # append from left.
print(deq)

right = deq.pop()
print(right, deq)
left = deq.popleft() # pop from left.
print(left, deq)

deq.extend([7, 8, 9])
print(deq)
deq.extendleft([7, 8, 9]) # extend from left.
print(deq)

d = deque(maxlen=20)
for i in range(30):
    d.append(i)
print(d) # When exceed the limit, elements in the left will be deleted.




##### LISTS #####

# Sort.
a = [7, 2, 5, 1, 3]
print(a)
a.sort()
print(a)

b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key=len)
print(b) # Sort by key.

# Binary search.
import bisect
c = [1, 2, 2, 2, 3, 4, 7] # Input must be a sorted list.

print(bisect.bisect(c, 2)) # bisect() finds where to insert to keep sorted.
print(bisect.bisect(c, 5))

bisect.insort(c, 6) # insort() finds where to insert to keep sorted and insert it.
print(c)




##### DICTIONARIES #####

# Basic.
d1 = {'a' : 'some value', 'b' : [1, 2, 3, 4]}; print(d1)
d1[7] = 'an integer'; print(d1)
d1[5] = 'some value'; print(d1)
d1['dummy'] = 'another value'; print(d1)
del d1[5]; print(d1)
ret = d1.pop('dummy'); print(ret); print(d1)

print(d1['b'])
print('b' in d1)

print(list(d1.keys()))
print(list(d1.values()))

d1.update({'b' : 'foo', 'c' : 12}) # Merge a dict with another.
print(d1)

mapping = dict(zip(range(5), reversed(range(5))))
print(mapping)

# Collect into a dict.
words = ['apple', 'bat', 'bar', 'atom', 'book']
dict_by_letter = {}
for word in words:
    letter = word[0]
    if letter not in dict_by_letter:
        dict_by_letter[letter] = [word]
    else:
        dict_by_letter[letter].append(word)
print(dict_by_letter)

dict_by_letter = {}
for word in words:
    letter = word[0]
    # If key not in the dict, then add this key as default.
    dict_by_letter.setdefault(letter, []).append(word)
print(dict_by_letter)

dict_by_letter = {}
from collections import defaultdict
dict_by_letter = defaultdict(list)
for word in words:
    # Search for word[0], if not exist, then create an empty list and append.
    dict_by_letter[word[0]].append(word)
print(dict_by_letter)

# The key of a dict generally have to be an immutable object.
print(hash('string'))
print(hash((1, 2, (2, 3))))
try:
    hash((1, 2, [2, 3]))
except TypeError:
    print("This object is not hashable.")




##### SETS #####

# Set stores unique objects.
lst = [2, 2, 2, 1, 3, 3]
set1 = set(lst)
print(lst, set1)

# Logical Operators
st1 = {1, 2, 4, 6, 7, 8, 9}
st2 = {2, 3, 5, 6, 7}
print(st1, st2)
print(st1 | st2, st1.union(st2)) # Union
print(st1 & st2, st1.intersection(st2)) # Intersection
print(st1 ^ st2, st1.symmetric_difference(st2)) # Symmetric difference
print(st1 - st2, st1.difference(st2)) # Subtraction (in st1 but not in st2)

print({1, 2, 3}.issubset(st1))
print({1, 2, 3, 4, 5, 6, 7}.issuperset(st2))
print({0, 3, 5}.isdisjoint(st1))




##### Built-in functions #####

# enumerate(iterator)
# return a index-value pair of the elements in an iterator.
lst = ['foo', 'bar', 'baz']
dic = {}
for key, value in enumerate(lst):
    dic[value] = key
print(dic)

# sorted(iterator)
print(sorted([7, 1, 2, 6, 0, 3, 2]))
print(sorted('horse race'))
print(sorted(dic)) # Dictionary is unordered, so it will only sorted by key.
print(sorted(dic.items())) # This method will sorted as a tuple list.

# zip(iter1, iter2)
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)
print(list(zipped)) # Create a list of tuples. Similar as dot product.

seq3 = [False, True]
zipped2 = zip(seq1, seq2, seq3)
print(list(zipped2)) # Determined by the shortest sequence.

for i, (a, b) in enumerate(zip(seq1, seq2)):
    print(f'{i}: {a}, {b}')

pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
first_names, last_names = zip(*pitchers) # Unzip a sequence.
print(first_names, last_names)




##### Comprehension #####

# list = [expr for val in collection if condition]
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
filtered = [x.upper() for x in strings if len(x) > 2]
print(filtered)

unique_lengths = {len(x) for x in strings}
print(unique_lengths)

loc_mapping = {val : index for index, val in enumerate(strings)}
print(loc_mapping)

# nested.
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],
            ['Maria', 'Juan', 'Javier', 'Natalia', 'Pillar']]
# outer layer of the loop: loop through lists in all_data.
# inner layer of the loop: loop through strings in names (inner layer of lists).
result = [name for names in all_data for name in names if name.count('e') >= 2]
print(result)

some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
print(flattened)

listed = [[x for x in tup] for tup in some_tuples]
print(listed)