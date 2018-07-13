import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    def scrape(self, keyword):
        print("Running scrape() method")
        instances = []
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                instances.append(url)
        for x in range(0, len(instances)):
            if keyword in instances[x]:
                print(instances[x])

    def scrapeAndSave(self, keyword):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        with open("headlines.txt", "w") as f:
            for tag in soup.find_all('a'):
                url = tag.get('href')
                if url and 'html' and keyword in url:
                    print("SAVED: " + url)
                    f.write(url + '\n')
news = "https://news.yahoo.com/"

Scraper(news).scrapeAndSave("latest")
