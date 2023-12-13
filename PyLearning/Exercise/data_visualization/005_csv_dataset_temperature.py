import csv

from datetime import datetime
import matplotlib.pyplot as plt


filepath = 'D:\Projects\PyLearning\Exercise\data_visualization\data\sitka_weather_2018_simple.csv'
with open(filepath) as f:
    reader = csv.reader(f) # print reader will only get the memory address.
    header_row = next(reader) # get the first line of the .csv file.

    # enumerate() returns both the index and the value.
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get TMAX (index 5).
    # for will loop the row one by one and save row as a list temporarily.
    # Use int() to convert data string to integer.
    dates, high_temps, low_temps, diffs = [], [], [], []
    #ave_temps = 
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        #ave = int(row[4])
        low = int(row[6])
        diff = high - low
        dates.append(current_date)
        high_temps.append(high)
        #ave_temps.append(ave)
        low_temps.append(low)
        diffs.append(diff)
    #high_temps = [int(row[5]) for row in reader]
    #low_temps = [int(row[6]) for row in reader]
    print(dates)
    print(high_temps)
    #print(ave_temps)
    print(low_temps)
    print(diffs)

# Plot the hight temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
# alpha controls transparency.
ax.plot(dates, high_temps, c='red', alpha=0.5, linewidth=1)
#ax.plot(ave_temps, c='green')
ax.plot(dates, low_temps, c='blue', alpha=0.5, linewidth=1)
ax.plot(dates, diffs, c='green', alpha=0.5, linewidth=1)

# Format plot.
plt.fill_between(dates, high_temps, low_temps, facecolor='purple', alpha=0.1)
plt.fill_between(dates, 0, diffs, facecolor='green', alpha=0.1)
plt.title("Daily high & low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # Draw diagonally to prevent overlapping.
plt.ylabel("Temperature (F)", fontsize=16)
plt.ylim([0, 75]) # Set limitation of y range.
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()