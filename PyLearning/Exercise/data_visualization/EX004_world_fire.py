import csv

from datetime import datetime
from multiprocessing.connection import wait
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline, colors
import matplotlib.pyplot as plt

def find_header(header, keyword):
    """Find specific title in a list then return the index."""

    for index in range(len(header)):
        if header[index] == str(keyword):
            break
    return index

def get_fire(filepath):
    """
    Get maximum and minimum temperature data of NOAA NCDC .csv dataset.
    function returns 3 lists in the date, high temps, low temps order.
    find data in similar format, go to https://www.ncdc.noaa.gov/cdo-web/search
    """

    with open(filepath) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        latitude = find_header(header_row, 'latitude')
        longitude = find_header(header_row, 'longitude')
        acq_date = find_header(header_row, 'acq_date')
        acq_time = find_header(header_row, 'acq_time')
        brightness = find_header(header_row, 'brightness')

        # Examine the data we want to use in which column.
        for index, column_header in enumerate(header_row):
            print(index, column_header)
    
        dates, latitudes, longitudes, brightnesses = [], [], [], []
        for row in reader:
            temp_date = row[acq_date]+row[acq_time]
            current_date = datetime.strptime(temp_date, '%Y-%m-%d%H%M')
            try:
                lat = float(row[latitude])
                lon = float(row[longitude])
                bri = float(row[brightness])
            except ValueError:
                print(f"Missing data for {current_date}")
            else:
                dates.append(current_date)
                latitudes.append(lat)
                longitudes.append(lon)
                brightnesses.append(bri)
        # print(dates)
    return dates, latitudes, longitudes, brightnesses

filepath = 'D:\Projects\PyLearning\Exercise\data_visualization\data\world_fires_1_day.csv'
dates, latitudes, longitudes, brightnesses = get_fire(filepath)

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': longitudes,
    'lat': latitudes,
    'text': dates, # Give each marker of the scatter a tag.
    'marker': {
        'size': [30*bri/max(brightnesses) for bri in brightnesses],
        'color': brightnesses, # Determine the value Plotly display.
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Brightness'} # Control the colorbar on the right.
        },
    }] # Create a Scattergeo chart, use key-value pair to customize.
my_layout = Layout(title='Global Fires') # Configuration.

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = 'EX004_result.html')


# Find what colorscales we can use.
for key in colors.PLOTLY_SCALES.keys():
    print(key)