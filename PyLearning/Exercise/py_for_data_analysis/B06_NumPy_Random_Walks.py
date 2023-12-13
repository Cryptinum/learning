import numpy as np
import random as rd
import matplotlib.pyplot as plt
import warnings

# GLOBAL SETTINGS.
np.set_printoptions(suppress=True)
warnings.filterwarnings("ignore") # Suppress warnings.



##### 1D Random Walk #####

# Ordinary method
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if rd.randint(0, 1) else -1
    position += step
    walk.append(position)

plt.plot(walk[:100], label='Ordinary')

# Use array.
nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws>0, 1, -1)
walk2 = steps.cumsum()

print(walk2.min(), walk2.max())
print((np.abs(walk2) >= 10).argmax()) # First time walk 10 units away.

plt.plot(walk2[:100], label='Use array')
plt.legend(loc="best")
plt.show()

# Simulating Several Random Walks at Once.
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size=(nwalks, nsteps)) # Generate 0 or 1.
steps = np.where(draws>0, 1, -1) # =1 if 1 else =-1.
walks = steps.cumsum(1) # Cumulative add by row.

print(walks)
print(walks.min(), walks.max())

hits30 = (np.abs(walks)>=30).any(1) # First time walk 30 units away.
print(hits30.sum()) # Number of walks hits +-30.

crossing_times = (np.abs(walks[hits30])>=30).argmax(1)
print(crossing_times.mean())