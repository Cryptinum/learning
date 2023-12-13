import matplotlib.pyplot as plt

from class_random_walk import Randomwalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk.
    rw = Randomwalk(10000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(14, 9))

    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, s=1,
               c=point_numbers, cmap=plt.cm.rainbow,
               edgecolor='none')

    # ax.plot(rw.x_values, rw.y_values, linewidth=1)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='darkviolet', edgecolors='k', linewidth=2.5, s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
               edgecolors='k', linewidth=2.5, s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break