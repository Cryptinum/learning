from plotly.graph_objs import Bar, Layout
from plotly import offline

from class_dice import Dice


def roll_same_dices(num_sides=6, dices_number=2, rolling_times=6000):
    """Make some rolls, and store their sums in a list."""
    
    # Create a D6.
    dice = Dice(num_sides)

    # Calculate the sum of dices_number times of rolling.
    results = [sum([dice.roll() for die in range(dices_number)])
               for roll_num in range(rolling_times)]

    # Analyse the frequency of the sums.
    sum_min = dices_number
    sum_max = dice.num_sides*dices_number
    frequencies = [results.count(value) for value in range(sum_min, sum_max+1)]
    return frequencies

def roll_two_diffenrent_dices(num_sides_1=6, num_sides_2=10,
                              dices_number_1=1, dices_number_2=1,
                              rolling_times=6000):
    """Roll two dices with different number"""
    # Create two dices.
    dice_1 = Dice(num_sides_1)
    dice_2 = Dice(num_sides_2)

    # Calculate the sum of dices_number times of rolling.
    results = []
    for roll_num in range(rolling_times):
        nums_1 = [dice_1.roll() for die in range(dices_number_1)]
        nums_2 = [dice_2.roll() for die in range(dices_number_2)]
        nums = nums_1 + nums_2
        result = sum(nums)
        results.append(result)

    # Analyse the frequency of the sums.
    sum_min = dices_number_1 + dices_number_2
    sum_max = num_sides_1 * dices_number_1 + num_sides_2 * dices_number_2
    frequencies = [results.count(value) for value in range(sum_min, sum_max+1)]
    return frequencies


num_sides = 8
dices_number = 2
rolling_times = 50000
result = roll_same_dices(num_sides, dices_number, rolling_times)

# Visualize the results.
dice = Dice(num_sides)
x_values = list(range(dices_number, dice.num_sides*dices_number+1))
data = [Bar(x=x_values, y=result)] # Create a bar chart.

#x_axis_config = {'title': 'Result', 'dtick': 1} # dtick=1 marks every integer.
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
title_config = f'Results of rolling {dices_number} D6 and sum them for {rolling_times} times'

my_layout = Layout(title=title_config, xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='004_result_1.html')


num_sides_1 = 6
num_sides_2 = 0
dices_number_1 = 3
dices_number_2 = 0
rolling_times = 50000
result = roll_two_diffenrent_dices(num_sides_1, num_sides_2,
                                   dices_number_1, dices_number_2, rolling_times)

sum_min = dices_number_1 + dices_number_2
sum_max = num_sides_1 * dices_number_1 + num_sides_2 * dices_number_2
x_values = list(range(sum_min, sum_max+1))
data = [Bar(x=x_values, y=result)] # Create a bar chart.

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
title_config = (f'Results of rolling {dices_number_1} D{num_sides_1} '+
                f'and {dices_number_2} D{num_sides_2} '
                f'then sum them for {rolling_times} times')

my_layout = Layout(title=title_config, xaxis=x_axis_config, yaxis=y_axis_config)
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='004_result_2.html')