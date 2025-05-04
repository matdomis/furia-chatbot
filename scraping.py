import requests
from bs4 import BeautifulSoup
import re
import json

ERROR = 0

def extrair_json(url=None):
    """
        Retorna o JSON da página da FURIA no Draft5.
    """

    # URL Scrapper
    url = 'https://draft5.gg/equipe/330-FURIA'
    response = requests.get(url)

    response.raise_for_status()  
    if response.status_code != 200:
        print(f"Erro ao acessar a página: {response.status_code}")
        return ERROR

    # Pega HTML da página e salva em um arquivo 'page.html' -- para debug.
    soup = BeautifulSoup(response.text, 'html.parser')

    # Pega o conteúdo da tag <script id="__NEXT_DATA__">
    script_tag = soup.find('script', id='__NEXT_DATA__')

    if not script_tag:
        print("Script __NEXT_DATA__ não encontrado.")
        return ERROR

    json_data = json.loads(script_tag.string)
    print('JSON criado com sucesso!')

    return json_data


extrair_json()