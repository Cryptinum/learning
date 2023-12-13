import numpy as np
import warnings

# GLOBAL SETTINGS.
np.set_printoptions(suppress=True)
warnings.filterwarnings("ignore") # Suppress warnings.



##### File I/O with Arrays (Use NumPy) #####

# np.save() / np.load()
# Arrays are saved by default in an uncompressed raw binary format
#   with the file extension .npy.
arr = np.arange(10)
path = r'D:\Projects\PyLearning\Exercise\py_for_data_analysis\B04_some_array.npy'
np.save(path, arr)

arr_load = np.load(path)
print(arr_load)

# np.savez()
# Save multiple arrays, with file extension .npz.
path = r'D:\Projects\PyLearning\Exercise\py_for_data_analysis\B04_some_arrays.npz'
arr2 = np.flip(arr)
np.savez(path, a=arr, b=arr2)

arch = np.load(path)
print(arch['b'])

# np.savez_compressed()
# Save multiple arrays in compressed format, with extension .npz.
path = r'D:\Projects\PyLearning\Exercise\py_for_data_analysis\B04_compressed_arrays.npz'
np.savez_compressed(path, a=arr, b=arr2)

arch = np.load(path)
print(arch['b'])