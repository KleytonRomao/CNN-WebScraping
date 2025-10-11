from logs.loggs import DK
import requests
from bs4 import BeautifulSoup
import logging

SITE = "ttps://www.cnnbrasil.com.br/internacional/"

class Scraper:
    def __init__(self,site=SITE):
        self.site = site
        DK().config()
    def get_html(self):
        try:
            resposta = requests.get(self.site)
            if resposta.status_code == 200:
                logging.info("Site acessado com sucesso.")
                return resposta.content
            else:
                logging.error(f"Erro ao acessar o site: {resposta.status_code}")
                return None
        except requests.RequestException as e:
            logging.error(f"Erro na requisição: {e}")
            return None

    def parse_html(self, html):
        try:
            soup = BeautifulSoup(html, 'html.parser')
            titles = soup.find_all('h2', class_='title')
            articles = [title.get_text(strip=True) for title in titles]
            logging.info(f"{len(articles)} artigos encontrados.")
            return articles
        except Exception as e:
            logging.error(f"Erro ao parsear o HTML: {e}")
            return []       
a = Scraper()
html = a.get_html()
if html:
    articles = a.parse_html(html)
    for article in articles:
        print(article)