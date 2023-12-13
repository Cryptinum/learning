import requests
import json

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    # Add link in the bars and make them clickable.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    # FORMAT: <a href='URL'>link text</a>
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>" # Make x label clickable.
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Add tooltips for each bars.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}" # Use HTML return method.
    labels.append(label)

# Make visualization, use dictionary approach.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels, # Add tooltips for each bars.
    'marker': {
        'color': 'rgb(60, 100, 150)', # A specified blue color.
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'} # Outline the bar grey.
        },
    'opacity': 0.6,
    }]
my_layout = { # Prevent using Layout class.
    'title': 'Most-Starred Python Projects on GitHub',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
        },
    }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='009_python_repos.html')