import requests
from bs4 import BeautifulSoup


class Cnn:
    def __init__(self, link):
        self.link = link

    def request(self):
        response = requests.get(self.link)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup
        else:
            return None

    def get_news_titles_and_links(self):
        soup = self.request()
        if soup:
            news_data = []
            titles = soup.find_all('h3', class_='news-item-header__title')

            for title in titles:
        
                news_title = title.get_text(strip=True)
                link = title.find_parent('a')

                if link:
                    news_link = link.get('href')
                else:
                    news_link = "Sem link"

                news_data.append({'title': news_title, 'link': news_link})

            return news_data
        return []


ext = Cnn('https://www.cnnbrasil.com.br/internacional/')
news_data = ext.get_news_titles_and_links()

# Imprime os títulos das notícias e os links encontrados
for news in news_data:
    print(f"Title: {news['title']}")
    print(f"Link: {news['link']}")
    print("-" * 40)
