# Prédiction des Émissions de CO2 - Modèle de Régression et API

Ce projet contient un modèle de régression linéaire pour prédire les émissions de CO2 en fonction de plusieurs caractéristiques du véhicule, notamment la taille du moteur, le nombre de cylindres et la consommation de carburant. Le modèle est exposé via une API FastAPI, ce qui vous permet de faire des prédictions en temps réel à partir de nouvelles données.

## Comment utiliser ce répertoire

1. Clonez ce répertoire sur votre machine locale en utilisant la commande suivante :

    ```shell
        git clone https://github.com/your-username/predicting-co2-emissions.git

2. Installation des dépendances

    ```shell
        pip install -r requirements.txt

3. Entraînez le Modèle et Créez les Scalaires

Avant d'exécuter l'API, vous devez entraîner le modèle de régression et créer les scalaires. Ouvrez le cahier Jupyter model.ipynb et suivez les instructions pour entraîner le modèle. Cela générera les fichiers de modèle et de scalaires utilisés par l'API.

4. Lancement de l'API Démarrez l'API FastAPI en exécutant le fichier app.py :

    ```shell
       uvicorn app:app --reload

5. Exemple de Requête API

Vous pouvez utiliser des outils tels que curl ou Postman pour envoyer des requêtes à l'API. Voici un exemple de requête en utilisant Postman :

Ouvrez Postman et créez une nouvelle requête POST.

Définissez l'URL de la requête à localhost:8000.

Dans l'onglet "Body", sélectionnez "raw" et choisissez "JSON (application/json)".

Utilisez le format JSON suivant pour envoyer les caractéristiques du véhicule à prédire :

    ```json

        {
            "ENGINESIZE": 2,
            "CYLINDERS": 4,
            "FUELCONSUMPTION_COMB": 8.5
        }

Cliquez sur "Send" pour envoyer la requête, et vous recevrez une réponse JSON contenant les émissions de CO2 prédites pour les caractéristiques du véhicule fournies.