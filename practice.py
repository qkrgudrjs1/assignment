import time
import requests
from bs4 import BeautifulSoup

# User-Agent:
# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
for n in range(4):
    request = requests.get(f"https://genie.co.kr/chart/top200?ditc=D&ymd=20240520&hh=14&rtm=Y&pg={n+1}", headers=header)
    soup = BeautifulSoup(request.text)
    info = soup.find("tbody")
    numbers = info.findAll("td", {"class": "number"})
    titles = info.findAll('a', {"class": "title ellipsis"})
    artists = info.findAll('a', {"class": "artist ellipsis"})
    time.sleep(1)

    for i, (n, t, a) in enumerate(zip(numbers, titles, artists)):
        number = n.next.strip()
        title = t.text.strip()
        artist = a.text.strip()
        print("{0:s}위. {1:s} - {2:s}".format(number, title, artist))
    
