import json
import os
import datetime 

def obter_elenco(json_data=None):
    """
        Extrai o elenco da FURIA no json_data e retorna uma lista de dicionários com o nome e a posição dos jogadores.
    """

    dados = json_data

    elenco = []
    players_section = dados['props']['pageProps']['data']['playerData']

    for player in players_section:
        player_name = player['playerNickname']
        player_position = player['playerHistory'][0]['status']

        elenco.append({
            'name': player_name,
            'position': player_position
        })

    # Ordena o elenco pela posição
    elenco = sorted(elenco, key=lambda x: x['position'])
    
    return elenco

def obter_partidas_futuras(json_data=None):
    """
        Extrai as partidas futuras da FURIA no data.json e retorna uma lista de dicionários com a data, os times e o torneio.
        A data é formatada para o padrão brasileiro (dd/mm/aaaa hh:mm).
    """

    dados = json_data

    partidas_futuras = []
    matches_section = dados['props']['pageProps']['matches']

    for match in matches_section:
        match_date = match['matchDate']
        match_date = datetime.datetime.fromtimestamp(match['matchDate'])     # Converte o timestamp para datetime
        match_date = match_date.strftime('%d/%m/%Y %H:%M')                   # Formata a data para o padrão BR
       
        match_team_A = match['teamA']['teamName']
        match_team_B = match['teamB']['teamName']
        match_tournament = match['tournament']['tournamentName']

        partidas_futuras.append({
            'date': match_date,
            'team_A': match_team_A,
            'team_B': match_team_B,
            'tournament': match_tournament
        })

    return partidas_futuras

def obter_partidas_passadas(json_data=None):
    """
        Extrai as partidas passadas da FURIA no data.json e retorna uma lista de dicionários com a data, os times, o torneio e o placar.
        A data é formatada para o padrão brasileiro (dd/mm/aaaa hh:mm).  
    """

    dados = json_data

    ultimas_partidas = []
    matches_section = dados['props']['pageProps']['results']

    for i in range(5):
        match = matches_section[i]

        match_date = match['matchDate']
        match_date = datetime.datetime.fromtimestamp(match['matchDate'])     # Converte o timestamp para datetime
        match_date = match_date.strftime('%d/%m/%Y %H:%M')                   # Formata a data para o padrão BR
       
        match_team_A = match['teamA']['teamName']
        match_team_B = match['teamB']['teamName']
        match_tournament = match['tournament']['tournamentName']

        match_score_team_A = match['seriesScoreA']
        match_score_team_B = match['seriesScoreB']

        ultimas_partidas.append({
            'date': match_date,
            'team_A': match_team_A,
            'team_B': match_team_B,
            'score_A': match_score_team_A,
            'score_B': match_score_team_B,
            'tournament': match_tournament
        })

    return ultimas_partidas