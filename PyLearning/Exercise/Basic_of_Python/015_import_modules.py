# Storing functions in modules.

# Storing in separate files then importing into the main program.

import testmodule # tell python to open testmodule.py
testmodule.make_pizza(16, 'pepperoni')
testmodule.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing specific functions to omit dots.
from testmodule import make_pizza, show_pizza
make_pizza(16, 'pepperoni')
show_pizza('mushrooms', 'green peppers', 'extra cheese')

# Give a function an alias.
from testmodule import make_pizza as mp
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# Give module an alias.
import testmodule as pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Importing all functions in a mudule
from testmodule import *
make_pizza(16, 'pepperoni')
show_pizza('mushrooms', 'green peppers', 'extra cheese')
