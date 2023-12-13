import numpy as np
import matplotlib.pyplot as plt
import warnings

# GLOBAL SETTINGS.
np.set_printoptions(suppress=True)
warnings.filterwarnings("ignore") # Suppress warnings.



##### Create Large Grids. #####

# Start from a little grid.
X = np.array([[0, 0.5, 1],[0, 0.5, 1]])
print("X的维度:{},shape:{}".format(X.ndim, X.shape))
Y = np.array([[0, 0, 0],[1, 1, 1]])
print("Y的维度:{},shape:{}".format(Y.ndim, Y.shape))

plt.plot(X, Y, 'o--')
plt.grid(True)
#plt.show()

# np.meshgrid()
# Create a (-5, 5) axis, length of each unit is 0.01, total as 1000.
points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)

# Evaluate function sqrt(x^2+y^2) across a regular grid of values.
z = np.sqrt(xs**2 + ys**2)
print(z)

plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
#plt.show()



##### Conditional Logic as Array Operations. #####

# Start from a little data.
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

# Take a value from x if corresponding value in cond is True.
# This method has several problems:
#   1. slow for large arrays.
#   2. not work with multidimensional arrays.
result = [(x if c else y) for x, y, c in zip(xarr, yarr, cond)]
print('\n', result, sep='\n')

# np.where()
# 2nd & 3rd argument don't need to be arrays.
result = np.where(cond, xarr, yarr) # Same as above, but more concisely and tidy.
print(result)

arr = np.random.randint(-10, 10, (4,4))
positive = np.where(arr < 0, -2, arr) # Replace only negative values.
negative = np.where(arr > 0, 2, arr) # Replace only positive values.
all = np.where(arr < 0, -2, 2) # Replace all values
print('', arr, positive, negative, all, sep='\n')



##### Mathematical & Statistical Methods. #####
print('\n\n\n########## Mathematical & Statistical Methods ##########\n')

arr = np.random.randint(-10, 10, (6,3))

print('Original array:', '\n', arr, '\n',
      'arr.mean()/np.mean(arr) (Average of the array):', '\t',
      np.round(arr.mean(), 3), '\n',
      'arr.mean(axis=1) (Average of each row/2nd dim):', '\t',
      np.round(arr.mean(axis=1), 3), '\n',
      'arr.sum() (Sum of the array):', '\t',
      arr.sum(), '\n',
      'arr.sum(axis=0) (Sum of each column/1st dim):', '\t',
      arr.sum(axis=0), '\n',
      'arr.cumsum(axis=0) (Cumulative sum):', '\n',
      arr.cumsum(axis=0), '\n',
      'np.add.accumulate(arr, axis=0) (Cumulative sum) (Result same as above):', '\n',
      np.add.accumulate(arr, axis=0), '\n',
      'arr.cumprod(axis=0) (Cumulative product):', '\n',
      arr.cumprod(axis=0), '\n',
      'arr.std() (Standard deviation of the array):', '\t',
      np.round(arr.std(), 3), '\n',
      'arr.std(axis=1) (Standard deviation of each row/2nd dim):', '\t',
      np.round(arr.std(axis=1), 3), '\n',
      'arr.var()=arr.std()**2 (Variance of the array):', '\t',
      np.round(arr.var(), 3), '\n',
      'arr.var(axis=1)=arr.std(axis=1)**2 (Variance each row/2nd dim):', '\t',
      np.round(arr.var(axis=1), 3), '\n',
      'arr.min()/arr.argmin() (Minimum of the array, and its index):', '\t',
      f'{arr.min()}, {arr.argmin()}', '\n',
      'arr.max()/arr.argmax() (Maximum of the array, and its index):', '\t',
      f'{arr.max()}, {arr.argmax()}',
      sep='')



##### Boolean Arrays. #####
print('\n\n\n########## Boolean Arrays ##########\n')

# True is 1, False is 0.
arr = np.random.randn(12)
positive_bool = arr > 0
positive = (arr>0).sum()
print(np.around(arr, 2), positive_bool,
      f'Number of positive value: {positive}', sep='\n')

# Additional method.
print(f"Does this boolean array have any value 'True'?\t{positive_bool.any()}",
      f"Is all the value in this boolean array is 'True'?\t{positive_bool.all()}",
      sep='\n')



##### Sorting. #####
print('\n\n\n########## Sorting ##########\n')

# Just like python built-in method.
arr = np.random.randint(-10, 10, 10)
print(f'Original:\t{arr}')
sorted = np.sort(arr) # Same as arr.sort, but sorted permanently.
print(f'Sorted arr:\t{sorted}')

arr = np.random.randint(-10, 10, (3, 6))
print('Original:', arr, sep='\n')
sorted = np.sort(arr, 1)
print('Sorted arr (by row):', sorted, sep='\n')

# Approximately find quantile.
quantile = 0.05 # 5% quantile.
large_arr = np.random.randn(1000)
large_arr.sort()
q_quantile = large_arr[int(quantile * len(large_arr))]

print('', f'{100*quantile}% quantile is {q_quantile}.',
     'Fraction of original large arr:',
      np.around(large_arr[0:8], 3),
      np.around(large_arr[496:504], 3),
      np.around(large_arr[992:], 3), sep='\n')



##### np.unique() and Other Set Logic. #####
print('\n\n\n########## Other Set Logic ##########\n')

# np.unique(), similar to a set.
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print(np.unique(names))

ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
print(np.unique(ints))

# np.in1d()
values = np.array([6, 0, 0, 3, 2, 5, 6])
boolean = np.in1d(values, [2, 3, 6]) # Check whether in values.
print(boolean)

# np.intersect1d(x, y)
x = np.random.randint(-10, 10, 10)
y = np.random.randint(-10, 10, 10)
print('\nOriginal:')
print(np.sort(x), np.sort(y))
print('Common Values\t-->\t', np.intersect1d(x, y))
print('All Values\t-->\t', np.union1d(x, y))
print('x - y\t\t-->\t', np.setdiff1d(x, y))
print('x XOR y\t\t-->\t', np.setxor1d(x, y))

