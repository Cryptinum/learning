import requests
import json

# Make an API call and store the response.
# Argument url saves the url of the API.
# Argument headers saves the API version we want to call.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers) # Make a call.
print(f"Status code: {r.status_code}") # If success, return 200 as status code.

# Store API response in an variable then save to a temp file.
response_dict = r.json()
filepath = 'D:\Projects\PyLearning\Exercise\data_visualization\data\most_starred_py_github.json'
with open(filepath, 'w') as f:
    json.dump(response_dict, f, indent=4)

# Process results.
print(f"Total repositories: {response_dict['total_count']}")
# ↓ Same as line 31-33
# print('\nAvailable keys:')
# for key in response_dict['items'][0].keys():
#     print(key)

# Save items to a list of dictionaries.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}") # Total repos we called.

# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()): # Examine the keys of each repos.
    print(key)

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")