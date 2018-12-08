from bs4 import BeautifulSoup
import requests

url = "http://www.pgnmentor.com/files.html"

html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")

players = open("chess/players.txt", "w")
openings = open("chess/openings.txt", "w")
for link in soup.find_all('a', href=True):
    href = link['href']

    if any(href.endswith(x) for x in ['.zip']):
        print(href)
        if "players/" in href:
            wr = href.replace("players/","")
            wr = wr.replace(".zip","")
            players.write(wr + ".pgn\n")
        elif "openings/" in href:
            wr = href.replace("openings/", "")
            wr = wr.replace(".zip", "")
            openings.write(wr + ".pgn\n")
