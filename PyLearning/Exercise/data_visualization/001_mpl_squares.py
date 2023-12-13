import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Use predefined style.
print(plt.style.available)
plt.style.use('seaborn')

# subplots() can generate multi plots in the same figure.
# The variable fig represents the entire figure or collection
#   of plots that are generated.
# Format: .plot(x_axis, y_axis, linewidth=int)
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
#   axis='x', 'y' or 'both'
ax.tick_params(axis='both', labelsize=14)

plt.show()