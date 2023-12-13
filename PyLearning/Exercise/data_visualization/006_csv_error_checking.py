import csv

from datetime import datetime
import matplotlib.pyplot as plt


filepath = 'D:\Projects\PyLearning\Exercise\data_visualization\data\death_valley_2018_simple.csv'
with open(filepath) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Examine the data we want to use in which column.
    for index, column_header in enumerate(header_row):
        print(index, column_header)

    # Get TMAX (index 5).
    # for will loop the row one by one and save row as a list temporarily.
    # Use int() to convert data string to integer.
    dates, high_temps, low_temps, diffs = [], [], [], []
    #ave_temps = 
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            #ave = int(row[4])
            low = int(row[5])
        except ValueError: # Pass the dates with error data.
            print(f"Missing data for {current_date}")
        else:
            diff = high - low
            dates.append(current_date)
            high_temps.append(high)
            #ave_temps.append(ave)
            low_temps.append(low)
            diffs.append(diff)

    '''
    #high_temps = [int(row[5]) for row in reader]
    #low_temps = [int(row[6]) for row in reader]
    #print(dates)
    #print(high_temps)
    #print(ave_temps)
    #print(low_temps)
    #print(diffs)
    ''' # Experiment codes.

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
plt.title("Daily high & low temperatures - 2018\nin Death Valley, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # Draw diagonally to prevent overlapping.
plt.ylabel("Temperature (F)", fontsize=16)
plt.ylim([0, 130]) # Set limitation of y range.
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()