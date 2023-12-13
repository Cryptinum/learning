import csv

from datetime import datetime
import matplotlib.pyplot as plt

def find_header(header, keyword):
    """Find specific title in a list then return the index."""

    for index in range(len(header)):
        if header[index] == str(keyword):
            break
    return index

def get_temperature(filepath):
    """
    Get maximum and minimum temperature data of NOAA NCDC .csv dataset.
    function returns 3 lists in the 'date', 'high temps', 'low temps' order.
    to find data in similar format, go to https://www.ncdc.noaa.gov/cdo-web/search
    """

    with open(filepath) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        DATE = find_header(header_row, 'DATE')
        TMAX = find_header(header_row, 'TMAX')
        TMIN = find_header(header_row, 'TMIN')

        # Examine the data we want to use in which column.
        for index, column_header in enumerate(header_row):
            print(index, column_header)
    
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[DATE], '%Y-%m-%d')
            try:
                high = int(row[TMAX])
                low = int(row[TMIN])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)
    print(dates, highs, lows)
    return dates, highs, lows

filepath = 'D:\Projects\PyLearning\Exercise\data_visualization\data\death_valley_2021.csv'
dates, dv_high, dv_low = get_temperature(filepath)

filepath = 'D:\Projects\PyLearning\Exercise\data_visualization\data\\fairbanks_2021.csv'
dates, fb_high, fb_low = get_temperature(filepath)

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(dates, dv_high, c='red', alpha=0.5, linewidth=1, label='Death Valley High')
ax.plot(dates, dv_low, c='orangered', alpha=0.5, linewidth=1, label='Death Valley Low')
plt.fill_between(dates, dv_high, dv_low, facecolor='darkorange', alpha=0.1)

ax.plot(dates, fb_high, c='blue', alpha=0.5, linewidth=1, label='Fairbanks High')
ax.plot(dates, fb_low, c='royalblue', alpha=0.5, linewidth=1, label='Fairbanks Low')
plt.fill_between(dates, fb_high, fb_low, facecolor='cornflowerblue', alpha=0.1)

plt.title("Temperature Comparison between\nDeath Valley, CA and Fairbanks, AK - 2021", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # Draw diagonally to prevent overlapping.
plt.ylabel("Temperature (F)", fontsize=16)
#plt.ylim([0, 130])
plt.tick_params(axis='both', which='major', labelsize=16)
plt.legend(loc="best")

plt.show()
