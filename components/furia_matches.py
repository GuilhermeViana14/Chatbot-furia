import requests

def get_furia_matches():
    url = "https://hltv-api.vercel.app/api/matches.json"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        matches = response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API da HLTV: {e}")
        return "Erro ao acessar os dados dos jogos. Tente novamente mais tarde."

    furia_matches = []

    for match in matches:
        team1 = match.get("team1", {}).get("name", "")
        team2 = match.get("team2", {}).get("name", "")
        date = match.get("date", "")

        if "FURIA" in team1 or "FURIA" in team2:
            furia_matches.append(f"{team1} vs {team2} em {date}")

    if furia_matches:
        return "\n".join(furia_matches)
    else:
        return "Nenhum jogo futuro encontrado para a FURIA."
