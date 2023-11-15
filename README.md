# ue19_labo09-10
Ce programme Python utilise la bibliothèque requests pour interroger le service PunAPI afin d'afficher un jeu de mot aléatoire.

# Installation
1. Assurez-vous d'avoir Python installé sur votre système. Aussi non, vous pouvez le télécharger ici (https://www.python.org/downloads/).
2. Installez la bibliothèque dans le répertoire du projet :
  ```bash
   pip install requests
3. Exécutez le script en utilisant la commande suivante :
  python lab09-10.py

# Fonctionnement
Le programme interroge l'API PunAPI. Si la requête réussit (code statut: 200), le jeu de mot est affiché. Sinon, le programme renvoie un message d'erreur avec le numéro du code statut.

Auteur : Zoé Gillet
Pour plus d'informations sur PunAPI, rendez-vous sur leur site web (https://www.punapi.rest/).
