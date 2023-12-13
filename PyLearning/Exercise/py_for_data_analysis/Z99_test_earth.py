import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import pandas_profiling
import plotly
import plotly.graph_objects as go
from plotly.offline import plot
from sklearn.preprocessing import MinMaxScaler
import colorlover as cl
from IPython.display import HTML

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
import warnings
warnings.filterwarnings("ignore")
# %matplotlib inline

import urllib.request, json
# url = "http://maps.googleapis.com/maps/api/geocode/json?address=google"
# url = "https://raw.githubusercontent.com/Nov05/playground-fireball/master/data/earth.json"
# response = urllib.request.urlopen(url)
filepath = r'D:\Projects\PyLearning\Exercise\py_for_data_analysis\datasets\earth.json'
with open(filepath) as f:
    json_data = json.load(f)

# 纬线 Parallels
x0 = json_data['data'][0]['x']
y0 = json_data['data'][0]['y']
z0 = json_data['data'][0]['z']
len(x0)

# 经线 Meridians
x1 = json_data['data'][1]['x']
y1 = json_data['data'][1]['y']
z1 = json_data['data'][1]['z']
len(x1)

# blue base (dots)
x2 = json_data['data'][2]['x']
y2 = json_data['data'][2]['y']
z2 = json_data['data'][2]['z']
len(x2)

# white continents (lines)
x3 = json_data['data'][3]['x']
y3 = json_data['data'][3]['y']
z3 = json_data['data'][3]['z']
len(x3)

# rivers (not in use)
x4 = json_data['data'][4]['x']
y4 = json_data['data'][4]['y']
z4 = json_data['data'][4]['z']
len(x4)

# not in use
x5 = json_data['data'][5]['x']
y5 = json_data['data'][5]['y']
z5 = json_data['data'][5]['z']
len(x5)

from IPython.display import HTML 
colors = ["rgb(0,0,255)", 
          "rgb(255, 255, 255)", 
          "rgb(12, 52, 61)", 
          "rgb(106, 168, 79)",
          "rgb(229.5,229.5,25.5)", 
          "rgb(106, 168, 79)", 
          "rgba(31, 119, 180, 0.34)",
          "rgb(31, 119, 180)" # 7 
         ]
HTML(cl.to_html(colors))

color_background = 'black'
color_lines = 'darkblue' # Parallels and Meridians
color_base = 'darkblue'
color_land = 'whitesmoke'
opacity_base = 0.1
opacity_land = 0.8
size_lines = 1

# Parallels 
trace0 = go.Scatter3d(
    x=x0,
    y=y0,
    z=z0,
    mode='lines',
    marker=dict(
        size=size_lines,
        color=color_lines, # set color to an array/list of desired values 
        opacity=opacity_base,
        showscale=False,
        line=dict(
            width=size_lines, 
            color=color_base)
        ),
    showlegend=False,
    name='Parallel'
    )
# Meridians
trace1 = go.Scatter3d(
    x=x1,
    y=y1,
    z=z1,
    mode='lines',
    marker=dict(
        size=size_lines,
        color=color_lines,  
        opacity=opacity_base,
        showscale=False,
        line=dict(
            width=size_lines, 
            color=color_base,)
        ),
    showlegend=False,
    name='Meridian'
    )
# base surface (dots)
trace2 = go.Scatter3d(
    x=x2,
    y=y2,
    z=z2,
    mode='markers',
    marker=dict(
        size=2,
        color=color_base,  
        opacity=opacity_base,
        showscale=False,
        line=dict(width=1, color=color_base)
        ),
    showlegend=False,
    name='by Wenjing Liu',
    )
# land
trace3 = go.Scatter3d(
    x=x3,
    y=y3,
    z=z3,
    mode='lines',
    marker=dict(
        size=1,
        color=color_land,  
        opacity=opacity_land,
        showscale=False,
        line=dict(width=1, color=color_land)
        ),
    showlegend=False,
    name='land'
    )
data = [trace0, trace1, trace2, trace3]

layout = go.Layout(
    autosize=False,
    width=1300,
    height=800,
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    ),
    title=dict(
        text='title',
        x=0.015, y=0.95),
    scene=dict(
        xaxis=dict(
            title="x axis",
            color=color_background,
            backgroundcolor=color_background,
            showaxeslabels=False,
            showline=False,
            showgrid=False,
            zeroline=False,
            ),
        yaxis=dict(
            title="y axis",
            color=color_background,
            backgroundcolor=color_background,
            showaxeslabels=False,
            showline=False,
            showgrid=False,
            zeroline=False,
            ),
        zaxis=dict(
            title="z axis",
            color=color_background, 
            backgroundcolor=color_background,
            showaxeslabels=False,
            showline=False,
            showgrid=False,
            zeroline=False,
            ),
        ),
    paper_bgcolor=color_background,
    plot_bgcolor=color_background,
)
fig = go.Figure(data=data, layout=layout)
fig.show()

# download plot to HTML
plot(fig, filename='2019-10-20 3d globe.html', auto_open=False)