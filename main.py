
import os
import sys
import pandas as pd


# Esto asegura que 'src' sea visible sin importar desde dónde se ejecute el script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.clean_fi import rename_cols, feature_ing
from src.utils import save_csv


from src.model import (
    split_data,
    train_model,
    predict_model
)

from src.metrics import evaluate_model

def pipeline():
    """
    Ejecuta todo el flujo de ETL y de entrenamiento del modelo
    """
    #1. Cargar y guardar los datos desde la fuente oficial
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00601/ai4i2020.csv"
    df = pd.read_csv(url)
    save_csv(df, "data/raw/data_raw.csv")
    print("DataFrame Crudo Cargado y almacenado Correctamente")

    #2. Renombrar columnas al español 
    df = rename_cols(df)
    print("Columnas renombradas Correctamente")

    #3. Crear variables adicionales 
    df = feature_ing(df)
    print("Ingeniería de caracteristicas Finalziada correctamente")

    #4. Guardar DataFrame limpio y procesado
    save_csv(df, "data/clean/data_clean.csv")
    print("datos procesados correctamente")

    #Hacer Split de entrenamiento y prueba
    print("Iniciando entrenamiento del modelo")
    # Separamos los predictores de la variable objetivo

    features = [
    'Temp_Aire_K',
    'Temp_Proceso_K',
    'Velocidad_Rotacion_RPM',
    'Torque_Nm',
    'Desgaste_Herramienta_min',
    'Potencia_W',
    'Dif_temperatura_K',
    'Esfuerzo_desgaste',
    ]

    target = 'Falla_Maquina'

    X_train, X_test, y_train, y_test = split_data(
        df,
        features,
        target
        )

    print("Split Finalizado")

    #6 Entrenar modelo
    model = train_model(X_train, y_train)
    print("Entrenamiento Finalizado")

    #7 predecir y evaluar
    y_pred =  predict_model(model, X_test)
    print("predicción Finalizada")

    #8 Metricas
    metrics = evaluate_model(y_test, y_pred)
    print("evaluación Finalizada")

    





    
if __name__ == "__main__":
    pipeline()