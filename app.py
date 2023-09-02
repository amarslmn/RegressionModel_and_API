from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import numpy as np
import logging


logging.basicConfig(level=logging.INFO)

# Création de l'application FastAPI
app  = FastAPI()

# Définition de la classe ScoringItem qui représente les données d'entrée attendues
class ScoringItem(BaseModel):
    ENGINESIZE:float
    CYLINDERS: float
    FUELCONSUMPTION_COMB:float

# Chargement du modèle pré-entraîné et des scalers depuis des fichiers pickle
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler_x.pkl', 'rb') as f:
    scaler_x = pickle.load(f)

with open('scaler_y.pkl', 'rb') as f:
    scaler_y = pickle.load(f)

# Définition d'une route POST pour effectuer des prédictions
@app.post('/')
async def scoring_endpoint(item:ScoringItem):
    logger = logging.getLogger(__name__)

    logger.info(f"Received input : {item}")
    
    # Transformation des données d'entrée en un tableau Numpy pour la prédiction
    new_data = np.array([item.ENGINESIZE, item.CYLINDERS, item.FUELCONSUMPTION_COMB]).reshape(1,-1)
    logger.info(f"Data tansformed into an np array : {new_data}")
    
    # Standardisation des données d'entrée en utilisant le scaler_x
    X = scaler_x.transform(new_data)
    logger.info(f"Data standardized : {X}")
   
    # Prédiction des données standardisées à l'aide du modèle
    yhat= model.predict(X)
    logger.info(f"Predictions made (scaled) : {yhat}")

    # Inversion de la transformation pour obtenir les prédictions à l'échelle d'origine
    yhat = scaler_y.inverse_transform(yhat.reshape(-1,1))
    logger.info(f"Predictions made (original scale): {yhat}")
    # Retour des prédictions au format JSON
    return {"prediction": float(yhat)}
