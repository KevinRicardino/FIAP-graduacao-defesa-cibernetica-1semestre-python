import requests
from bs4 import BeautifulSoup

url = "https://www.fiap.com.br"

resposta = requests.get(url)

soup = BeautifulSoup(resposta.text, "html.parser")

texto = soup.get_text()

palavras = texto.split()

print(palavras)
