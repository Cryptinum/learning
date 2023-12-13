from operator import itemgetter

import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/item/31820635.json'
r = requests.get(url) # Make a call.
print(f"Status code: {r.status_code}") # If success, return 200 as status code.

# Store API response in an variable then save to a temp file.
response_dict = r.json()
filepath = 'D:\Projects\PyLearning\Exercise\data_visualization\data\hacker_news_31820635.json'
with open(filepath, 'w') as f:
    json.dump(response_dict, f, indent=4)


tops = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(tops) # Make a call.
print(f"Status code: {r.status_code}") # If success, return 200 as status code.

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separates API call for each submission.
    try:
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        print(f"id: {submission_id}\tstatus: {r.status_code}")
        response_dict = r.json()

        # Build a dictionary for each article.
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
            }
        submission_dicts.append(submission_dict)
    except TypeError:
        print('操你妈')
    except KeyError:
        print(f'Some keys are lost in thread {submission_id}.')

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse = True)

filepath = 'D:\Projects\PyLearning\Exercise\data_visualization\data\top_hackernews.json'
with open(filepath, 'w') as f:
    json.dump(submission_dicts, f, indent=4)
