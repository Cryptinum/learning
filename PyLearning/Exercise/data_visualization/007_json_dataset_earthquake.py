import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline, colors


# Rewrite the data to a new file, make it more readable.
filepath = 'D:\Projects\PyLearning\Exercise\data_visualization\data\eq_data_30_day_m1.json'
with open(filepath) as f:
    all_eq_data = json.load(f) # Convert into a giant dictionary.

readable_file = 'D:\Projects\PyLearning\Exercise\data_visualization\data\\readable_eq_data_2.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

# Pulling the data of magnitude, longitude and latitude of an earthquake.
all_eq_dicts = all_eq_data['features'] # Take the data associated with 'features'.
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    title = eq_dict['properties']['title'] # Call title of earthquakes.
    mag = eq_dict['properties']['mag'] # Call 'mag' in 'properties'.
    lon = eq_dict['geometry']['coordinates'][0] # Call longitude.
    lat = eq_dict['geometry']['coordinates'][1] # Call latitude.
    hover_texts.append(title)
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(5*max(mags))

# Map the earthquakes.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts, # Give each marker of the scatter a tag.
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags, # Determine the value Plotly display.
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'} # Control the colorbar on the right.
        },
    }] # Create a Scattergeo chart, use key-value pair to customize.
my_layout = Layout(title='Global Earthquakes') # Configuration.

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename = '007_result_2.html')


# Find what colorscales we can use.
for key in colors.PLOTLY_SCALES.keys():
    print(key)