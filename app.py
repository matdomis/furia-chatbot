from flask import Flask, render_template, request, redirect, url_for, jsonify
from scraping import extrair_json
from get_data import obter_elenco, obter_partidas_futuras, obter_partidas_passadas

import random

app = Flask(__name__, template_folder='templates', static_folder='static')

gritos_furia = [
    'Vou torcer pra Fúria ser campeão... na triboneira, meu caldeirão! 🎶',
    'Fúria, Fúria, Fúria! 🎶',
    'Eles nunca vão entender! 🗣️',
    'POROPOPOPOPO... POROPOPOPOPO... POROPOPOPOPO! 🎶\nA Fúria veio pra vencer...\nA Fúria veio pra vencer...\nA Fúria veio pra vencer, e a NaVi se F%@#! 😬🤫'
    ]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()

        message = data.get('message')
        if not message:
            return jsonify({'error': 'Não há mensagem!'}), 400

        furia_json = extrair_json()
        if not furia_json:
            error_message = render_template('partials/error.html', error='Erro ao extrair JSON!')
            return jsonify({'error': error_message}), 500

        if message == '/proximo' or message == '🔥':
            partidas_futuras = obter_partidas_futuras(furia_json)
            partidas_futuras = ''.join([f"{match['date']} - {match['team_A']} vs {match['team_B']} ({match['tournament']})" for match in partidas_futuras])
           
            rendered_message = render_template('partials/message.html', bot_message=partidas_futuras, aux_text='Aqui está a próxima partida da FURIA 🎮')
            return jsonify( { 'html': rendered_message } )
        
        elif message == '/ultimas' or message == '🗓️':
            partidas_passadas = obter_partidas_passadas(furia_json)
            partidas_passadas = ''.join([f"🕐 {match['date']} - {match['tournament']}\n⚔️ {match['team_A']} {match['score_A']} vs {match['score_B']} {match['team_B']}\n\n" for match in partidas_passadas])
           
            rendered_message = render_template('partials/message.html', bot_message=partidas_passadas, aux_text='Aqui estão as últimas partidas da FURIA 🏆')
            return jsonify( { 'html': rendered_message } )
        
        elif message == '/lineup' or message == '🤘':
            elenco = obter_elenco(furia_json)
            elenco = elenco[::-1]
            elenco = ''.join([f"🔫 {player['name']} ({player['position']})\n" for player in elenco])
           
            rendered_message = render_template('partials/message.html', bot_message=elenco, aux_text='Aqui está o lineup da FURIA ⚔️')
            return jsonify( { 'html': rendered_message } )
        
        elif message == '/grito' or message == '📢':
            random_index = random.randint(0, len(gritos_furia) - 1)
            grito = gritos_furia[random_index]
            rendered_message = render_template('partials/message.html', bot_message=grito)
            return jsonify( { 'html': rendered_message } )
        
        else:
            rendered_message = render_template('partials/message.html', bot_message='Desculpe, não entendi o comando 😬')
            return jsonify( { 'html': rendered_message } )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)