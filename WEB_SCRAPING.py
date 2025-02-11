import requests
from bs4 import BeautifulSoup

url = '#la url que quiero'
respuesta = requests.get(url)

if respuesta.status_code == 200:
    soup = BeautifulSoup (respuesta.text, 'html.parser')
    
    print