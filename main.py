from utils.scraper import Scraper
from db.database import *

if __name__ == "__main__":
    scraper = Scraper("https://www.cnnbrasil.com.br/internacional/")
    articles = scraper.scrape_website()
    if articles:
        for article in articles:
            result = (article.get_text(strip=True))
            result = noticias.create(conteudo=result)
        
