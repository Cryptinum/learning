import random

digits = []
for i in range(1,21):
    digits.append(random.randint(1,100))

print(digits)
digits.sort()
print(digits)

print(f"The minimum is {min(digits)}.")
print(f"The maximum is {max(digits)}.")
print(f"The sum is {sum(digits)}.")

def integer_sum(integer_list): # Use a function.
    sums = 0
    for i in integer_list:
        sums = sums + i
    return sums
print(f"The sum is {integer_sum(digits)}.")

