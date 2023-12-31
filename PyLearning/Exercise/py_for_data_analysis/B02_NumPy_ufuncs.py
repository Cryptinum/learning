import numpy as np
import warnings
from timebudget import timebudget

# GLOBAL SETTINGS.
np.set_printoptions(suppress=True)
warnings.filterwarnings("ignore") # Suppress warnings.


##### UFUNCS #####
arr = np.arange(1,11).reshape(2,5)
arr2 = np.empty((2,5))
print('Original array:', arr, arr2, sep='\n')


sqrt = np.around(np.sqrt(arr), 3)
print('\nnp.sqrt(arr):', sqrt, sep='\n') # np.sqrt()
exp = np.around(np.exp(arr, arr2), 3)
print('\nnp.exp(arr):', exp, sep='\n') # np.exp()


print('\nWe give an optional out argument to np.exp(), output as arr2', 'arr2=',
      np.around(arr2, 3), sep='\n') # ufunc has optional out argument.


x = np.random.randint(-10, 10, (2,4))
y = np.random.randint(-10, 10, (2,4))
print('\nOriginal:', 'x=', x, 'y=', y, 'Maximum by element (np.maximum(arr)):', 
      np.maximum(x, y), sep='\n') # np.maxinum(), element-wise


arr = np.random.randn(5) * 10
remainder, whole_part = np.modf(arr) # np.modf(), return a tuple.
print('\nOriginal array generated by std-norm distribute:', np.around(arr, 2),
      'Decimal part:', np.around(remainder, 2),
      'Integer part:', whole_part, sep='\n') # Split into decimal & integral part.


# List of unary ufuncs.
arr = np.arange(-5,7).reshape((2,6)).astype('f')
arr[1, 2] = -3.2
print('\n\nOriginal array:', arr, sep='\n')

print('\nnp.abs():', np.abs(arr), sep='\n')
print('np.sqrt():', np.around(np.sqrt(arr), 3), sep='\n')
print('np.square():', np.around(np.square(arr), 3), sep='\n')

print('\nnp.log():', np.around(np.log(arr), 3), sep='\n')
print('np.log10():', np.around(np.log10(arr), 3), sep='\n')
print('np.log2():', np.around(np.log2(arr), 3), sep='\n')
print('np.log1p(x)=log(1+x):', np.around(np.log1p(arr), 3), sep='\n')

print('\nnp.sign():', np.around(np.sign(arr), 3), sep='\n')
print('np.ceil():', np.around(np.ceil(arr), 3), sep='\n')
print('np.floor():', np.around(np.floor(arr), 3), sep='\n')

# Round to the nearest integer, preserving the dtype.
print('\nnp.rint():', np.around(np.rint(arr), 3), sep='\n')

print('\nnp.isnan():', np.isnan(np.log(arr)), sep='\n')
# Neither inf nor nan.
print('np.isfinite():', np.isfinite(np.log(arr)), sep='\n')
print('np.isinf():', np.isinf(np.log(arr)), sep='\n')
print('np.logical_not():', np.logical_not(arr), sep='\n')

print('# Regular and hyperbolic trigonometric functions')
print('\nnp.cos():', np.around(np.cos(arr), 3), sep='\n')
print('np.cosh():', np.around(np.cosh(arr), 3), sep='\n')
print('np.sin():', np.around(np.sin(arr), 3), sep='\n')
print('np.sinh():', np.around(np.sinh(arr), 3), sep='\n')
print('np.tan():', np.around(np.tan(arr), 3), sep='\n')
print('np.tanh():', np.around(np.tanh(arr), 3), sep='\n')

print('# Inverse trigonometric functions')
print('\nnp.arccos():', np.around(np.arccos(arr), 3), sep='\n')
print('np.arccosh():', np.around(np.arccosh(arr), 3), sep='\n')
print('np.arcsin():', np.around(np.arcsin(arr), 3), sep='\n')
print('np.arcsinh():', np.around(np.arcsinh(arr), 3), sep='\n')
print('np.arctan():', np.around(np.arctan(arr), 3), sep='\n')
print('np.arctanh():', np.around(np.arctanh(arr), 3), sep='\n')


# List of binary ufuncs.
arr = np.random.randint(-10,10,(2,6))
arr2 = np.random.randint(-10,10,(2,6))

print('\n\nOriginal array:', arr, arr2, sep='\n')

print('\nnp.add(array1, array2, out):', np.add(arr, arr2), sep='\n')
print('np.subtract(array1, array2, out):', np.subtract(arr, arr2), sep='\n')
print('np.multiply(array1, array2, out):', np.multiply(arr, arr2), sep='\n')
print('np.divide(array1, array2, out):',
      np.around(np.divide(arr, arr2), 3), sep='\n')
print('np.power(array1, array2, out):', np.power(arr, 3), sep='\n')

print('\nnp.maximum(array1, array2, out):', np.maximum(arr, arr2), sep='\n')
print('np.minimum(array1, array2, out):', np.minimum(arr, arr2), sep='\n')
print('np.fmax(array1, array2, out): (ignore NaN)', np.fmax(arr, arr2), sep='\n')
print('np.fmin(array1, array2, out): (ignore NaN)', np.fmin(arr, arr2), sep='\n')

print('\nnp.mod(array1, array2, out):', np.mod(arr, arr2), sep='\n')

# Take signal of the second array to the first array.
print('\nnp.copysign(array1, array2, out):', np.copysign(arr, arr2), sep='\n')

# greater, greater_equal (>, >=)
# less, less_equal (<, <=)
# equal, not_equal (==, !=)

# logical_and, logical_or, logical_nor (&, |, ^)



# ufunc methods.
arr = np.arange(10)
print('', 'Original array:',
      'arr.sum():', arr.sum(),
      'np.add.reduce(arr):', np.add.reduce(arr), 
      sep='\n')

print()
arr = np.random.randint(-50,50,(5,5))
print(arr)
arr[::2].sort(1) # sort rows with indices 0,2,4,6...
print(arr)
boolean = arr[:, :-1] < arr[:, 1:]
print(boolean) # row 0,2,4 will be all True.
boolean_1d = np.logical_and.reduce(boolean, axis=1)
print(boolean_1d)
print(boolean.all(axis=1)) # Same as above.

arr = np.random.randint(-10,10,5)
arr2 = np.random.randint(-10,10,5)

print('\n\nOriginal array:', arr, arr2, sep='\n')
print('\nnp.inner(array1, array2):', np.inner(arr, arr2), sep='\n')
print('np.outer(array1, array2) (Default as multiply):', np.outer(arr, arr2), sep='\n')
print('np.multiply.outer(array1, array2) (ufunc method):', np.multiply.outer(arr, arr2), sep='\n')
print('np.add.outer(array1, array2) (ufunc method):', np.add.outer(arr, arr2), sep='\n')
print('np.subtract.outer(array1, array2) (ufunc method):', np.subtract.outer(arr, arr2), sep='\n')
print('np.maximum.outer(array1, array2) (ufunc method):', np.maximum.outer(arr, arr2), sep='\n')

arr = np.random.randint(-10,10,(5,5))
print('\n\nOriginal array:', arr, sep='\n')
print('\nnp.add.accumulate(array, axis=0):', np.add.accumulate(arr, axis=0), sep='\n')
print('np.add.accumulate(array, axis=1):', np.add.accumulate(arr, axis=1), sep='\n')
print('np.multiply.accumulate(array, axis=0):', np.multiply.accumulate(arr, axis=0), sep='\n')
print('np.multiply.accumulate(array, axis=1):', np.multiply.accumulate(arr, axis=1), sep='\n')




##### CUSTOM UFUNCS #####

# np.frompyfunc()
def add_elements(x, y):
    return x + y

add_them = np.frompyfunc(add_elements, 2, 1)
added = add_them(np.arange(8), np.arange(8))
print('\nAdded:', added, sep='\n')

add_them = np.vectorize(add_elements, otypes=[np.float64])
added = add_them(np.arange(8), np.arange(8))
print('\nAdded:', added, sep='\n')

arr = np.random.randn(1000000)
with timebudget("Python method is very slow."):
    add_them(arr, arr)
with timebudget("C method is much more fast."):
    np.add(arr, arr)