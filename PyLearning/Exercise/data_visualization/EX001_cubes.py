import matplotlib.pyplot as plt
import numpy as np

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['Helvetica']

fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=1,
           c=y_values, cmap=plt.cm.Wistia)

ax.set_title('Cube Numbers', color='black', fontsize=20)
ax.set_xlabel('Value', color='black', fontsize=16)
ax.set_ylabel('Cube of Value', color='black', fontsize=16)
ax.axis([-50, 5050, -2e9, 1.28e11])

ax.tick_params(axis='both', which='major', width=2, length=5, pad=5,
               colors='black', labelsize=12,
               top=False, right=False, labeltop=False, labelright=False)

fig.tight_layout()
plt.show()