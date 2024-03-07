import csv
import requests
import os

# Function to fetch environment variable or raise error if not found
def get_env_variable(var_name):
    value = os.getenv(var_name)
    if value is None:
        raise ValueError(f"{var_name} environment variable not found. Please set the {var_name}.")
    return value

# Fetch necessary values from environment variables
github_token = get_env_variable('GITHUB_TOKEN')
data_directory = get_env_variable('DATA_DIR')
file_name = get_env_variable('FILE_NAME')
repo_owner = get_env_variable('REPO_OWNER')
repo_name = get_env_variable('REPO_NAME')

# Construct the file path for the CSV
file_path = os.path.join(data_directory, file_name)

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
        print(f'Failed to create issue "{title}" with response: {response.json()}')

# Read issues from CSV and create them
with open(file_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        create_issue(row['Title'], row['Body'])