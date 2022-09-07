import requests
import json

CONFIG = {}


def setup_planning():
    print("======== PLANNING MYEFREI ========")
    print("Veuillez vous rendre sur votre planning MyEfrei (https://www.myefrei.fr/portal/student/planning)")
    print("Et cliquer sur le bouton \"COPIER URL PLANNING (ICAL)\"")
    CONFIG["agenda_url"] = input("Puis collez le lien ici : ").strip().replace("webcal://", "https://")
    r = requests.get(CONFIG["agenda_url"])
    if r.status_code != 200:
        print("Erreur : Le lien que vous avez entré n'est pas valide.")
        setup_planning()
    print(" ")


def setup_discord():
    print("======== DISCORD RPC ========")
    print("Veuillez choisir les données que vous souhaitez afficher sur votre profil Discord.")
    print("1. Nom du cours")
    print("2. Nom du professeur")
    print("3. Salle")
    CONFIG["first_key"] = ["nom_cours", "nom_prof", "salle"][int(input("1ère ligne : ").strip()) - 1]
    CONFIG["second_key"] = ["nom_cours", "nom_prof", "salle"][int(input("2ème ligne : ").strip()) - 1]
    print(" ")
    print("Veuillez choisir l'icône que vous souhaitez afficher sur votre profil Discord.")
    print("1. Efrei blanc")
    print("2. Efrei blanc sur fond noir")
    print("3. Efrei noir")
    print("4. Efrei noir sur fond blanc")
    print("5. Efrei couleur")
    print("6. Efrei couleur sur fond blanc")
    CONFIG["large_icon"] = ["efrei_white", "efrei_white_bg", "efrei_black", "efrei_black_bg", "efrei_color", "efrei_color_bg"][int(input("Icône : ").strip()) - 1]
    CONFIG["large_icon_text"] = input("Texte de l'icône : ").strip()
    print(" ")


print("Bienvenue sur Efrei Discord RPC !")
print("Il semble que ce soit la première fois que vous lancez EfreiRPC.")
print("La configuration va maintenant commencer.")
print(" ")
setup_planning()
setup_discord()
print("Configuration terminée !")
print(" ")
with open("config.json", "w") as f:
    json.dump(CONFIG, f)