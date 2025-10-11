import requests
from bs4 import BeautifulSoup
import logging
from logs.loggs import DK


class Scraper:

    def __init__(self,url):
        self.url = url

    def scrape_website(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                logging.info("200 OK - site acessível")
                soup = BeautifulSoup(response.content, 'html.parser')
                articles = soup.find_all('h3', class_='text-xl font-bold')
                logging.info(f"{len(articles)} artigos encontrados.")
                return articles
            else:
                logging.warning(f"Status code {response.status_code} para {url}")
                return None
        except Exception as e:
            logging.error(f"Erro ao acessar {url}: {e}")
            return None
