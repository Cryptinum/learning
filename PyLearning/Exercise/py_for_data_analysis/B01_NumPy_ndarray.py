from timebudget import timebudget

import numpy as np


np.set_printoptions(suppress=True)


# NumPy is an efficient package to process large data.
my_arr = np.arange(100000)
my_list = list(range(100000))
with timebudget("Use NumPy array"):
    for _ in range(10):
        my_arr2 = my_arr * 2
with timebudget("Use list"):
    for _ in range(10):
        my_list2 = [x * 2 for x in my_list]




##### NDARRAY #####

# ndarray is abbr. of N-dimensional array.
data = np.random.randn(2, 3)
print(data) # ndarray will be printed in a neat format.

data2 = data * 10
data3 = data + data/2
print(data2, data3, sep='\n') # NumPy batch computation on ndarray.

# All the data in a ndarray should be the same type.
data_test = np.random.randn(2, 3)
data_test[0, 0] = 4 # Index start from zero.
print(data_test)
try:
    data_test[1, 1] = 'string'
except ValueError:
    print('Error. All the data in a ndarray should be the same type!')

# Basic functions.
print('\n\n########## Functions ##########')
print(data.ndim) # Dimensions of a ndarray object (return a integer).
print(data.shape) # Size of each dimension of the matrix (return a tuple).
print(data.dtype) # Type of data stored in the ndarray.
print(data.strides) # Strides of each dimensions.
print(data.astype(np.int32)) # Change array type.

print(data.reshape((3, 2), order='F')) # order='C is row major, 'F' is column major.
print(data.flatten()) # Flatten
print(data.ravel()) # Flatten

'''
    A ndarray object internally consist following properties:

    1. A pointer to data, which stores data.
    2. The data type (dtype), describing fixed value cells in the array.
    3. The array's shape (shape), a tuple describing the fixed shape.
    4. Strides of each dims (strides), a tuple stores how many bytes to stride
       to loop through the whole array.

'''
# For example, every value in a float64 array take up 8-bytes long RAM
#   space, so we stride 8 bytes to loop through the 1st dim.
# Similarly, because the length of the 1st dim is 5, so we stride 5 values
#   to loop through the 2nd dim.
# Then we stride 4*5=20 values, which is 160 bytes in total.
print(np.ones((3, 4, 5), dtype=np.float64).strides) # Return (160, 40, 8)

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print(np.concatenate([arr1, arr2], axis=0)) # Concatenate 2 arrays up to down.
print(np.vstack((arr1, arr2))) # Same as above.
print(np.concatenate([arr1, arr2], axis=1)) # Concatenate 2 arrays left to right.
print(np.hstack((arr1, arr2))) # Same as above.

arr = np.arange(6)
arr1 = arr.reshape((3, 2))
arr2 = np.random.randn(3, 2)
print(np.r_[arr1, arr2])
print(np.c_[np.r_[arr1, arr2], arr]) # Stack more concisely.

arr = np.arange(3)
print(arr, arr.repeat(3)) # Repeat the array by element.
print(arr, np.tile(arr, 3)) # Repeat the whole array.
print(arr, np.tile(arr, (3, 2)))
print(arr, arr.repeat([2, 3, 4])) # Repeat the array in custom times.


# dtype changing.
print('\n\n########## dtype ##########')
arr = np.array([1, 2, 3, 4, 5])
print(arr.dtype)
float_arr = arr.astype(np.float64) # Use arr.astype(type) to cast to another dtype.
print(float_arr)

arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
print(arr.dtype)
int_arr = arr.astype(np.int32)
print(arr, int_arr, sep='\n') # It omits the digits after the decimal point.

empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32)

# sub-dtype.
ints = np.ones(10, dtype=np.uint16)
floats = np.ones(10, dtype=np.float32)
print(np.issubdtype(ints.dtype, np.integer))
print(np.issubdtype(floats.dtype, np.floating))
print(np.float64.mro()) # All the parent dtypes of float64.


### Create ndarrays.
print('\n\n########## Create ndarrays ##########')
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1) # Use .array to turn into a ndarray object.
print(data1)
print(arr1) # Formatted neatly.

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]] # For multi-dimensional data.
arr2 = np.array(data2)
print(data2)
print(arr2) # Formatted neatly as well.

print(arr1.dtype) # .array will find a good data type automatically.
print(arr2.dtype)

zeros1 = np.zeros(10, dtype=np.int16) # Use .zeros to create an 'empty' array.
# For multi-dimension.
# ATTENTION: numbers in the tuple from left to right is higher to lower
#            for the dimensions which higher than 2. So (2,3,4) means
#            the size of the 3rd dimension is 2, while the size of the
#            1st and 2nd dimensions are 3 by 4 for row and column.
zeros2 = np.zeros((2,3,4), dtype=np.int16)
print(zeros1, zeros2, sep='\n')

ones1 = np.ones((4,5), dtype=np.int16) # Use .ones to create 
print(ones1)

empty1 = np.empty((3,4), dtype=np.int16) # Use .empty to create an empty array.
print(empty1) # Not recommended, maybe generate nonsense values.

range1 = np.arange(15) # Use .arange to create a array similar to a list.
print(range1)

full1 = np.full((5,6), 'A string whose length is 28.') # Use .full to fill array.
print(full1.dtype)

eye1 = np.eye(5, dtype=np.int16)
id1 = np.identity(4, dtype=np.int16)
print(eye1, id1, sep='\n') # Use .eye or .identity to create an identity matrix.


### Arithmetic with NumPy Arrays.
arr = np.array([[1., 2., 3.], [4., 5., 6.]])
arr2 = np.array([[0., 4., 1.], [7., 2., 12.]])

print('\n\n########## Arithmetic ##########')
print(arr)
print(arr * arr) # Multiply by positional corresponding elements.
print(arr - arr)
print(1 / arr)
print(arr ** .5)

print(arr2 > arr) # Comparison, should be of same shape.


### Indexing and Slicing.
arr = np.arange(10)

print('\n\n########## Indexing and Slicing ##########')
print(arr)
print(arr[5])
print(arr[5:8])
print(arr[:])

arr[5:8] = 12 # Batch edit.
print(arr)

arr_slice = arr[5:8]
print(arr)
arr_slice[1] = 12345
print(arr) # A slice of an array is only a view, it will not create new array.
arr_sliced = arr[5:8].copy() # It will copy the sliced array explicitly.

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2]) # 2nd row.
print(arr2d[0][2])
print(arr2d[0,2])
print(arr2d[:2, 1:]) # First 2 rows, end 2 columns.
print(arr2d[1, :2]) # 2nd row, first 2 columns.
print(arr2d[:2, 2]) # First 2 rows, 3rd column.
print(arr2d[:2, 2:]) # First 2 rows, 3rd column, but in higher dimension.

arr2d[:2, 1:] = 0
print(arr2d)

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[0])
print(arr3d)
arr3d_copy = arr3d.copy()
arr3d_copy[0] = [1, 2, 3]
print(arr3d_copy) # It will change every row.

# Boolean indexing.
print('\n\n########## Boolean indexing ##########')
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randint(-10, 10, (7,4))

print(names, data, sep='\n')
print(names == 'Bob')
# Print rows which names == 'Bob' is True.
# ATTENTION: length of boolean array and indexing array must be the same.
print(data[names=='Bob'])
print(data[~(names=='Bob')]) # Reversed.
print(data[names=='Bob', 2:]) # Mixed indexing.

mask = (names == 'Bob') | (names == 'Will')
print(data[mask]) # Bob or Will.
print(data[~mask]) # Reversed.

data[data < 0] = 0
print(data)
data[names != 'Joe'] = 999
print(data)

# Fancy indexing.
print('\n\n########## Fancy indexing ##########')

arr = np.empty((8, 4))
for i in range(8):
    arr[i] = (i+1) * 2
int_arr = arr.astype('I')
print(int_arr)

print(int_arr[[4, 3, 0, 6]]) # Select in desired order.
print(int_arr[[-3, -5, -7]]) # Negative indices works as well.

arr = np.arange(1,33).reshape((8,4))
print(arr)
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]]) # Intersections.
print(arr[[1, 5, 7, 2]][:,[0, 3, 1, 2]]) # In wished order.

arr = np.arange(10) * 100
inds = [7, 1, 2, 6]
print(arr[inds]) # It can also call from objects.
print(arr.put(inds, 42)) # Replace by custom value.
print(arr.put(inds, [40, 41, 42, 43])) # Replace by custom order.

inds = [2, 0, 2, 1]
arr = np.random.randn(2, 4)
print(arr)
print(arr.take(inds, axis=1)) # Take row (axis=1) 2/0/2/1 as a new array.


### Transposing Arrays and Swapping Axes
print('\n\n########## Transposing Arrays and Swapping Axes ##########')

arr = np.arange(15).reshape((3, 5))
print(arr)
print(arr.T) # Transpose.

ortho = np.dot(arr.T, arr) # A^TA
print(ortho)

arr = np.arange(16).reshape((2,2,4)) # For higher dimensions.
print(arr)
print(arr.transpose(1,0,2)) # Reorder the axis, swap 1st & 3rd dims.
print(arr.swapaxes(1,2)) # Swap 1st & 2nd dims.
print(arr.transpose(0,2,1)) # Same as above.


### Array Broadcasting.
print('\n\n########## Array Broadcasting ##########')
arr = np.arange(4).repeat(3).reshape((4, 3))
arr2 = np.array([1, 2, 3])
print(arr)
print(arr2)
print(arr + arr2) # arr2 will repeat downwards.

# row mean and column mean.
arr = np.random.randint(-10, 10, (4, 5))
mean = arr.mean(axis=0)
demeaned = arr - mean
print('', arr, mean, demeaned, demeaned.mean(axis=0), sep='\n')

arr = np.random.randint(-10, 10, (4, 5))
mean = arr.mean(axis=1).reshape((4, 1)) # reshape to corresponding column
demeaned = arr - mean
print('', arr, mean, demeaned, demeaned.mean(axis=1), sep='\n')

# reshape a plate into higher dimension plane.
arr = np.zeros((4, 4))
arr_3d = arr[:, np.newaxis, :] # reshape to x-z plane.
print('', arr, arr_3d, arr_3d.shape, sep='\n')

arr = np.random.randint(-10, 10, (3, 4, 5))
depth_means = arr.mean(axis=2) # it returns a (3,4) array.
demeaned = arr - depth_means[:,:,np.newaxis] # turn it to (3,4,5)
print('', arr, depth_means, demeaned, demeaned.mean(axis=2), sep='\n')

def demean_axis(arr, axis=0):
    means = arr.mean(axis)

    # This generalizes things like [:, :, np.newaxis] to N dimensions
    indexer = [slice(None)] * arr.ndim
    indexer[axis] = np.newaxis
    return arr - means[indexer]