import csv

from datetime import datetime
import matplotlib.pyplot as plt


filepath = 'D:\Projects\PyLearning\Exercise\data_visualization\data\sitka_weather_2018_full.csv'
with open(filepath) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Examine the data we want to use in which column.
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    dates, rainfalls = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rainfall = float(row[5])
        dates.append(current_date)
        rainfalls.append(rainfall)

# Plot the hight temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, c='blue', linewidth=1)

plt.title("Daily Rainfall - 2018 in Sitka, AK", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # Draw diagonally to prevent overlapping.
plt.ylabel("Rain or Melted Snow etc. (in)", fontsize=16)
plt.ylim([0, 2.8]) # Set limitation of y range.
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()