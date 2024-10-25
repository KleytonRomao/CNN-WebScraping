import requests
from bs4 import BeautifulSoup
import sqlite3 


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
         
        if soup is not None:
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
    def save_in_db(self, news_data):
        conn = sqlite3.connect('cnnbrasil.db')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS noticias')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS noticias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                link TEXT
            )
        ''')

        for news in news_data:
            cursor.execute('''
                INSERT INTO noticias (title, link)
                VALUES (?, ?)
            ''', (news['title'], news['link']))

        conn.commit()
        conn.close()

if __name__ == '__main__':
    link = 'https://www.cnnbrasil.com.br/internacional/'
    cnn = Cnn(link)
    news_data = cnn.get_news_titles_and_links()
    cnn.save_in_db(news_data)
