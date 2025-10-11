import requests
from bs4 import BeautifulSoup
from logs.loggs import DK


class Scraper:
    def __init__(self, url):
        self.url = url

    def scrape_website(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
    
                soup = BeautifulSoup(response.content, 'html.parser')
                articles = soup.find_all('h3', class_='text-xl font-bold')
                
                return articles
            else:
                
                return None
        except Exception as e:
            
            return None
