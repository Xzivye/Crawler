from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

class Spidey:

    def __init__(self, urls=[]):
        self.visited = []
        self.visit = urls

    def download(self, url):
        return requests.get(url).text
 
    def get_links(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                self.path = urljoin(url, path)
            yield path

    def write(self, url):
        with open('crawl.txt', 'a') as f:
            f.write(url+"\n")
            
        f.close()

    def add_visit(self, url):
            if url not in self.visited and url not in self.visit:
                self.visit.append(url)
                self.write(url)

    def log(self, url):
       html = self.download(url)
       for url in self.get_links(url, html):
           self.add_visit(url)

    def run(self):
        while self.visit:
                url = self.visit.pop(0)
                try:
                    self.log(url)
                except:
                    self.visited.append(url)

if __name__ == '__main__':
    Spidey(urls=['https://www.example.com/']).run()