import requests

def obtenir_jeudemot():
    response = requests.get('https://punapi.rest/api/pun')

    if response.status_code == 200:
        jeu_data = response.json()
        return jeu_data.get('pun', 'Pas de jeu de mot disponible')
    else:
        return f"Erreur. Status code: {response.status_code}"

if __name__ == "__main__":
    jeu_de_mot = obtenir_jeudemot()
    print("Jeu de mot du jour :")
    print(jeu_de_mot)
