import csv
from datetime import datetime


def find_header(header, keyword):
    """Find specific title in a list then return the index."""

    for index in range(len(header)):
        if header[index] == str(keyword):
            break
    return index

def get_temperature(filepath):
    """
    Get maximum and minimum temperature data of NOAA NCDC .csv dataset.
    function returns 3 lists in the date, high temps, low temps order.
    find data in similar format, go to https://www.ncdc.noaa.gov/cdo-web/search
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