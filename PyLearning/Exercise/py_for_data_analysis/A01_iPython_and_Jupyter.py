'''
    *** Python shell

        We can use python interactive interpreter to test code. Open
    shell, cd to working dir, then type 'python' and press enter.

        * To exit this mode, press CTRL-Z or type exit() then press enter.

    *** iPython shell

        Go to Python Environments, click Use iPython interactive mode,
    then click Open in Powershell. In shell, cd to working dir first,
    then input 'ipython' and press enter, shell will run in iPython mode.

        * To exit this mode, press CTRL-D or type exit() then press enter.
        * Use %run filepath to run a python file.
        * Use %load filepath to print the content of a file.
        * Use %paste or %cpaste to run code in clipboard.

        * Type variables then enter directly can make it more readable,
          instead of print(). Especially for dictionaries.

        * Type command? or object? can show the detailed info of a command
          or an object. This is called object introspection.

        * Type package.*keyword*? to search for all available functions
          have a specific keyword.

    *** iPython special commands

        Known as %magic, add % before any command.

        Examples:
        * In [1]: %timeit np.dot(a, a)
          113 µs ± 1.45 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)

        * In [2]: import matplotlib .pyplot as plt
          In [3]: import numpy as np
          In [4]: plt.plot(np.random.randn(50).cumsum())
'''

# Object introspection
def add_numbers(a, b):
    """
    Add two numbers together
    Returns
    -------
    the_sum : type of arguments
    """
    return a + b

# List & Dictionary Comprehension
import numpy as np
data = {i : np.random.randn() for i in range(7)}
print(data)

# An object is iterable means it can be looped through.
def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

print(isiterable('a string'))
print(isiterable([1,2,3]))
print(isiterable(5))

x = 'a string'
if not isinstance(x, list) and isiterable(x):
    # Convert into a list if the object is iterable.
    # it can convert strings, tuples, or dictionaries.
    x = list(x)
print(isiterable(x))
print(x)

'''
    *** Jupyter Notebook

        We can install Jupyter package for VS, then go to shell, type
    '$ jupyter notebook' to run Jupyter in bowser.

        To create a new iPython notebook, click DropDownList 'New' 
'''