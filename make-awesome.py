
import requests
import re
from bs4 import BeautifulSoup
awesome_list = "# Awesome Technostructure(s)\n\n"

with open("source.txt", "r") as f:
    urls = [line.strip() for line in f]
    for url in urls:
        
        response = requests.get(url)
    # url = "https://github.com/stars"
    # response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        awesome_list+= f"## {url}\n\n"
    # Get the list of repository URLs
        repos = []
        for repo in soup.select('h3 a'):
            name = (repo.text).replace(' / ', '/').replace('\n      ','').strip('\n').replace(' / ', '/')
            repos.append(name)

        # Create the "awesome" list in markdown format
        for index, repo in enumerate(repos, start=1):
            # awesome_list += f"- {repo}\n"
            awesome_list += f"- [{repo}](https://github.com/{repo})\n"

# Save the output to a markdown file
with open('README.md', 'w') as f:
    f.write(awesome_list)

print("Awesome list of GitHub repositories has been created!")