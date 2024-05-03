
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
            link = (repo.text).replace(' / ', '/').replace('\n      ','').strip('\n').replace(' / ', '/')
            
            repos.append(link)
            descs = []

        for repo in repos:
            response = requests.get("https://github.com/"+repo)
            soup = BeautifulSoup(response.text, 'html.parser')
            desc = soup.select('title')[0].text
            desc= desc.replace(f'GitHub - ', '').strip('\n')
                # print(f"{repo}: {desc}")
            descs.append(desc)
            item=""
            item=f"- [{repo}](https://github.com/{repo}): {desc}\n"
            awesome_list += item
            print(item)

        # Create the "awesome" list in markdown format{
            # awesome_list += f"- {repo}\n"

# Save the output to a markdown file
with open('README.md', 'w') as f:
    f.write(awesome_list)

print("Awesome list of GitHub repositories has been created!")