import csv
import requests
import os

# Fetch the GitHub token from environment variables
github_token = os.getenv('GITHUB_TOKEN')

if not github_token:
    raise ValueError("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")

# Your GitHub repository details
repo_owner = 'jymiller'
repo_name = 'great-questions'

# The URL for creating issues via the GitHub API
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'

headers = {
    'Authorization': f'token {github_token}',
    'Accept': 'application/vnd.github.v3+json',
}

# Function to create an issue
def create_issue(title, body):
    data = {'title': title, 'body': body}
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f'Successfully created issue "{title}"')
    else:
        print(f'Failed to create issue "{title}"')

# Read issues from CSV and create them
with open('kg_issues.csv', mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        create_issue(row['Title'], row['Body'])
