# Simulador de Conversa da FURIA

Uma SPA (Single-Page Application) simples para simular um chatbot da equipe FURIA Esports.

![image.png](https://i.imgur.com/GrRz08c.png)


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