from utils.scraper import *

if __name__ == "__main__":
    url = "https://www.cnnbrasil.com.br/internacional/"
    data = Scraper(url)
    txt = data.scrape_website()
    for i in txt:
        print(i.get_text())