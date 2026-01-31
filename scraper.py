import requests
from bs4 import BeautifulSoup

class NewsScraper:
    def __init__(self, sources):
        self.sources = sources

    def scrape(self):
        articles = []
        for source in self.sources:
            if source == 'kontan':
                articles.extend(self.scrape_kontan())
            elif source == 'bisnis':
                articles.extend(self.scrape_bisnis())
            elif source == 'investor_id':
                articles.extend(self.scrape_investor_id())
        return articles

    def scrape_kontan(self):
        url = 'https://www.kontan.co.id/'  # Example URL
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = []
        for item in soup.find_all('article'):
            title = item.find('h2').text
            link = item.find('a')['href']
            articles.append({'title': title, 'link': link})
        return articles

    def scrape_bisnis(self):
        url = 'https://www.bisnis.com/'  # Example URL
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = []
        for item in soup.find_all('article'):
            title = item.find('h2').text
            link = item.find('a')['href']
            articles.append({'title': title, 'link': link})
        return articles

    def scrape_investor_id(self):
        url = 'https://investor.id/'  # Example URL
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        articles = []
        for item in soup.find_all('article'):
            title = item.find('h2').text
            link = item.find('a')['href']
            articles.append({'title': title, 'link': link})
        return articles

if __name__ == '__main__':
    sources = ['kontan', 'bisnis', 'investor_id']
    scraper = NewsScraper(sources)
    news_articles = scraper.scrape()
    for article in news_articles:
        print(article)