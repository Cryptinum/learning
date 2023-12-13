# Slicing the lists into slices.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print(players[0:3]) # Print indices [0,1,2]
print(players[1:4]) # Print indices [1,2,3]
print(players[ :4]) # Print indices by the end of 3
print(players[2: ]) # Print indices by the start of 2
print(players[-3:]) # Print the last 3 indices.
print(players[::2]) # Step by 2
print(players[::-1]) # Reverse the list.

print("\nHere are the first 3 players in my team:")
for player in players[:3]:
    print(player.title())



# List copying: Use a slice

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] # Omitting both indices to copy the entire list.

'''
Attention: If we simply set 'friend_foods = my_foods',
           we only made a 'reference' of 'my_foods',
           since variables in python are based on memory addresses,
           which makes variables in python resemble pointers in C.
           To prove this, let 'friend_foods_test = my_foods'
           and search the ids of these lists.
'''

friend_foods_test = my_foods
if id(my_foods)!=id(friend_foods):
    is_equal = "!="
else:
    is_equal = "=="
if id(my_foods)!=id(friend_foods_test):
    is_equal_test = "!="
else:
    is_equal_test = "=="
print(f"\n{id(my_foods)} {is_equal} {id(friend_foods)}")
print(f"{id(my_foods)} {is_equal_test} {id(friend_foods_test)}")


print(f"\nMy favorite foods are: {my_foods}")
print(f"My friend's' favorite foods are: {friend_foods}")

my_foods.append('cannoli')
friend_foods.append('ice cream')
print(f"\nMy favorite foods are: {my_foods}")
print(f"My friend's' favorite foods are: {friend_foods}")