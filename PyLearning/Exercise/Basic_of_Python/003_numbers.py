import math

print("1. 2+3=%d"%(2+3))
print("2. 3-2=%d"%(3-2))
print("3. 2*3=%d"%(2*3))
print("4. 3/2=%.1f"%(3/2))
print("5. 3**2=%d"%(3**2))
print("6. 3**3=%d"%(3**3))
print("7. 10**6=%d"%(10**6))

universe_age = 14_000_000_000
print(universe_age)

x, y, z = 0, 0, 0
MAX_CONNECTIONS = 5000 # Use all capitals to indicate a constant variable.
print(type(MAX_CONNECTIONS))

# isinstance() can accept several data types.
x, y = 5, 2.5
print(isinstance(x, (int, float)))
print(isinstance(y, (int, float)))