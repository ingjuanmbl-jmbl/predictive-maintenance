import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def split_data(
        df: pd.DataFrame,
        features: list,
        target: str,
        test_size: float = 0.2,
        random_state: int = 42
        ):
    """
    Separa los datos en entrenamiento y prueba
        Argumentos:
            df: pd.DataFrame: Contiene el df previamente prepocesado
            Features: list: Contiene la lista de predictores
            target: str: contiene la variable
            test_size: El tamaño a elección de la sección de prueba por defecto es el 20%
            random_state: semilla aleatoria para garantizar reproducibilidad por defecto es 42
        Retorna:
        Conjuntos separados por train y test para X y Y
    """

    X = df[features]
    y = df[target]

    return train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state,
        stratify=y
    ) #Por defecto sckitlearn devuelve las variables train y test tanto para X como para y

def train_model(
    X_train,
    y_train,
    n_estimators: int = 100,
    random_state: int = 42
):
    """
    Entrena un modelo de clasificación/regresión basado en conjuntos (Ensemble Learning).

    Argumentos:
        X_train (array-like o pd.DataFrame): Matriz de características (predictores) 
            para el entrenamiento del modelo.
        y_train (array-like o pd.Series): Vector de la variable objetivo (target).
        n_estimators (int, opcional): Número de árboles en el modelo. 
            Por defecto es 100.
        random_state (int, opcional): Semilla aleatoria para garantizar la 
            reproducibilidad del entrenamiento. Por defecto es 42.

    Retorna:
        model: El modelo entrenado y listo para realizar predicciones o evaluaciones.
    """

    model = RandomForestClassifier(
        n_estimators=n_estimators,
        class_weight='balanced',
        random_state=random_state
    )

    model.fit(X_train, y_train)

    return model


def predict_model(model, X_test):

    return model.predict(X_test)



    

    