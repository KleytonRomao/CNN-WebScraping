import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

def scrape_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta erro para respostas ruins
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all(class_="title")
        return titles
    except requests.RequestException as e:
        logger.error(f"Error fetching {url}: {e}")
        return None