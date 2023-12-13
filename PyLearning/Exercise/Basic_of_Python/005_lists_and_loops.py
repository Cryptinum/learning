# While structure

magicians =['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!\n")



'''
for num in range(10,20):
    for i in range(2,num):
        if num%i == 0:
            j=num/i
            print(f"{num} = {i} * {int(j)}")
            break
    else:
        print(f"{num} is a prime number.")
'''

# range() function: range(start, end, step)
for value in range(5):
    print(value)
print()

for value in range(0,5):
    print(value)
print()

numbers = list(range(1,6))
print(numbers)

numbers = list(range(2,11,2)) # Start/end at 2/10, length is 2.
print(numbers)
print()

squares = []
for value in range(1,11):
    squares.append(value ** 2) # Append values in empty list.
print(squares)

squares = [value**2 for value in range(1,11)] # Compress in one line.
print(squares)



# Exercises
print("\nExercises:")
numbers  = [i for i in range(1,21)]
print(numbers)

numbers  = [i for i in range(1,1000001)]
def integer_sum(integer_list): # Use a function.
    sums = 0
    for i in integer_list:
        sums = sums + i
    return sums
print(integer_sum(numbers))

print(min(numbers))
print(max(numbers))
print(sum(numbers))

numbers = [i for i in range(1,21,2)]
print(numbers)
numbers = [i for i in range(3,31,3)]
print(numbers)
numbers = [i**3 for i in range(1,11)]
print(numbers)