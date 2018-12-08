'''

love you stackoverflow!!!

'''

from bs4 import BeautifulSoup
import requests

url = "http://www.pgnmentor.com/files.html"
url1 = "http://www.pgnmentor.com/players/"
url2 = "http://www.pgnmentor.com/openings/"

html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
file = ""
# print(soup)
for link in soup.find_all('a', href=True):
    href = link['href']

    if any(href.endswith(x) for x in ['.zip']):
        # if any(href.endswith('.zip')):
        print("Downloading '{}'".format(href))
        if "players/" in href:
            file = url1 + href.replace("players/", "")
        elif "openings/" in href:
            file = url2 + href.replace("openings/", "")

        if file != "":
            remote_file = requests.get(file)
            with open(href.replace("players/", ""), 'wb') as f:
                for chunk in remote_file.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
