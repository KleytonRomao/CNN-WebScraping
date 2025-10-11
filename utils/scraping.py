from bs4 import BeautifulSoup
from utils.feteched import Status_Site
from utils.feteched import SITE
import logging
from logs.loggs import DK

class Scraping:
    def __init__(self):
        DK().config()
    def parse(self):
        conteudo = Status_Site(SITE).get()
        print(conteudo)
        if conteudo: