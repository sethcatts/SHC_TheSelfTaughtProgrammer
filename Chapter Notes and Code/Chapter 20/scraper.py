import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
    def scrape(self):
        print("Running scrape() method")
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            #print(url)
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

news = "https://news.yahoo.com/"

Scraper(news).scrape()

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        response = urllib.request.urlopen(self.site)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        with open("output.txt", "w") as f:
            for tag in soup.find_all('a'):
                url = tag.get('href')
                if url and 'html' in url:
                    print("\n" + url)
                    f.write(url + "\n")
