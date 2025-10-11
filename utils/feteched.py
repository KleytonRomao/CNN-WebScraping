import requests
from logs.loggs import DK
import logging

SITE = "https://www.cnnbrasil.com.br/internacional/"

class Status_Site:
    
    def __init__(self,site):
        self.site = site
        DK().config()

    def get(self):
        try:
            resposta = requests.get(self.site)
            if resposta.status_code == 200:
                return resposta.content, logging.info(f"O site {self.site} está acessível.")
            else:
                return None, logging.error(f"O site {self.site} não está acessível. Status code: {resposta.status_code}")
        except ConnectionError as e:
            return None, logging.error(f"Erro de conexão ao acessar {self.site}: {e}")

a = Status_Site(SITE)
a.get()