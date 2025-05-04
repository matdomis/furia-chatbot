# Simulador de Conversa da FURIA

Uma SPA (Single-Page Application) simples para simular um chatbot da equipe FURIA Esports.

![image.png](https://img.notionusercontent.com/s3/prod-files-secure%2Fa377f419-6661-4a13-80ec-ca572a5e7b2f%2Fe39dd4c8-7208-405e-9bcc-a439a9b3774b%2Fimage.png/size/w=2000?exp=1746392810&sig=_R4eXeLbciyRCDEfaUKiznaffiSdcZXbpWs_enn6Vj8&id=1e99afbe-e3cb-80e0-883f-c5db549b6cd2&table=block&userId=9d7bd480-3d5a-47cd-8ef7-fc37edc8b67a)


Para acessar o ChatBot, acesse o [*RailWay App*](https://furia-chatbot-production-9d04.up.railway.app/) do programa.



## 📦 Tecnologias

- Python 3.10+
- Flask
- BeautifulSoup4
- HTML/CSS/JavaScript

## 👨‍💻 Instalando o Projeto Localmente (Ambiente Linux/WSL)

→ Primeiro, clone o projeto:

`git clone git@github.com:matdomis/furia-chatbot.git`

→ Crie um ambiente virtual para instalar as dependências:

`cd furia-chatbot`

`python3 -m venv env`

→ Ative o ambiente virtual e instale as dependências:

`source env/bin/activate`

`pip install -r requirements.txt`

→ Agora, dentro da pasta do projeto, execute o arquivo principal:

`python3 app.py`

→ Pronto! O programa está rodando, e aberto em seu [`localhost`](http://localhost)  💪

## 🕷️ Scraping

Este projeto realiza scraping de dados públicos da plataforma [Draft55.gg](http://Draft55.gg) utilizando a biblioteca `requests` e `BeautifulSoup`.

Foram coletadas informações objetivas para extrair:

- Nome dos jogadores atuais da Fúria
- Partida futuras
- Partidas passadas com resultado
- Campeonatos

Em caso de erro ao executar o programa, ou mensagem de erro do Bot. Uma manutenção no Scraping terá que ser realizada. 🔨