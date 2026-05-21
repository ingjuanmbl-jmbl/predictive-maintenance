import pandas as pd
from pandas import DataFrame
import joblib
from pathlib import Path
import json
import os

##################### FUNCIONES PARA MAEJO DE CSV ######################

def read_csv(route: str):
    """
    Lee Archivos tipo csv de una ruta especificada
    Args:
        route: ruta en la cual se encuentra el DataFrame a Analizar
    """
    
    try:
        df = pd.read_csv(route)
        print(f"Archivo cargado existosamente desde: {route}")
        return df
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo en la ruta: {route}")
        return None

def save_csv(df: DataFrame, route: str):
    
    """
    Guarda un DataFrame en un archivo CSV
    Args: df: Debe ser un DataFrame
    route: ruta en la cual se guardará el DataFrame
    """
    df.to_csv(route, index=False)
    print(f"DataFrame guardado existosamente en la ruta: {route}")

####------------------------------------FUNCIONES DE GUARDADO DE ARTEFACTOS --------------- ###

# Definimos la ruta raíz del proyecto (un nivel arriba de src)
ROOT_DIR = Path(__file__).resolve().parent.parent
ARTIFACTS_DIR = ROOT_DIR / "artifacts"

#Definir la función de guardado del artefacto
def save_model(model, path, model_name):
    """Guarda un objeto o artefacto en la ruta especificada.
        Argumentos:
            Model: Model enttrenado que desea guardar.
            path: La ruta espefica donde desea almacenar el modelo entrenado
            model_name:  Nombre especifico con la que se quiere almacenar el mdoelos
        Retorna:
            Mensaje con la ruta donde se almacenó en modelo
    """
    # Combinamos la ruta de la carpeta y el nombre del archivo
    full_path = os.path.join(path, f"{model_name}.joblib")


    #Guardamos el modelo
    joblib.dump(model, full_path)
    return f"Modelo almacenado correctamente en: {path}"

def load_model(path):
    """
    Carga un modelo de una ruta especifica
    """
    return joblib.load(path)




##### -----------------------------------------------##########################

def save_metrics(metrics: dict, path: str) -> None:
    """
    Guarda las métricas de evaluación del modelo en un archivo con formato JSON.

    Almacena el diccionario estructurado con una sangría (indentación) de 4 espacios 
    para garantizar que el archivo sea fácilmente legible por humanos.

    Argumentos:
        metrics (dict): Diccionario que contiene los resultados de la evaluación 
            (como el generado por la función evaluate_model).
        path (str): Ruta del archivo de destino (ej. 'metrics/evaluation_results.json').
    """
    with open(path, "w") as f:
        json.dump(metrics, f, indent=4)


def load_metrics(path: str) -> dict:
    """
    Carga las métricas de evaluación guardadas desde un archivo JSON.

    Argumentos:
        path (str): Ruta del archivo JSON que contiene las métricas.

    Retorna:
        dict: Diccionario con las métricas y el rendimiento del modelo cargado.
    """
    with open(path, "r") as f:
        return json.load(f)



    
