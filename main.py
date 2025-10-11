from utils.scraper import *

if __name__ == "__main__":
    url = "https://www.cnnbrasil.com.br/internacional/"
    data = scrape_website(url)
    print(data)