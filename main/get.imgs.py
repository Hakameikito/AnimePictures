from bs4 import BeautifulSoup
import requests


page = 0
base = "https://anime-pictures.net"
main = f"https://anime-pictures.net/pictures/view_posts/{page}?lang=en"

content = requests.get(main).content  # get html
soup = BeautifulSoup(content, "lxml")

# find all links and save them as (index, link) - ensure links with same index are skipped
links = []
for link in soup.find_all('a'):
    i = link.get("href")
    if "view_post" in i and i[21] != "0" and "view_posts" not in i:
        index = i[21:i.find("?")]
        if (index, i) not in links:
            links.append((index, i))

print(links)
print(len(links))