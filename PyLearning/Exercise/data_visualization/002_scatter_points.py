import matplotlib.pyplot as plt


x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
# Change the font style.
plt.rcParams['font.sans-serif'] = ['Bookman old style']

fig, ax = plt.subplots()

# Set size and color.
# Format: .scatter(x, y, size->int, color->str/tuple/list)
# ax.scatter(x_values, y_values, s=2, c='red')
# ax.scatter(x_values, y_values, s=2, c=(1, 0.1, 0.1))
ax.scatter(x_values, y_values, s=2,
           c=y_values, cmap=plt.cm.plasma, edgecolor='none') # Colormap method

# Set chart title and label axes.
ax.set_title("Square Numbers", color='black', fontsize=24)
ax.set_xlabel("Value", color='black', fontsize=14)
ax.set_ylabel("Square of Value", color='black', fontsize=14)

# Set the range for each axis.
# .axis([x_min, x_max, y_min, y_max])
ax.axis([-10, 1010, -10000, 1010000])

# Set size of tick labels.
# which='major', 'minor' or 'both' defines the scale line.
ax.tick_params(axis='both', which='major', width=0, length=0, pad=5,
               colors='black', labelsize=14,
               top=False, right=False, labeltop=False, labelright=False)

# Tight the figure in the drawing box.
fig.tight_layout()
plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')