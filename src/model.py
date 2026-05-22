import pandas as pd

from sklearn.model_selection import train_test_split, GridSearchCV
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
    random_state: int = 42
):
    """
    Entrena un modelo RandomForestClassifier optimizando hiperparámetros 
    mediante GridSearchCV (Validación Cruzada).

    Argumentos:
        X_train (array-like o pd.DataFrame): Matriz de características (predictores) para el entrenamiento del modelo.
        y_train (array-like o pd.Series): Vector de la variable objetivo (target).
        random_state (int, opcional): Semilla aleatoria para reproducibilidad. Por defecto es 42.

    Retorna:
        model: El MEJOR modelo entrenado obtenido por la búsqueda en grilla. basado en f1
    """
    #1. Definimos el modelo base
    base_model = RandomForestClassifier(
        class_weight='balanced',
        random_state=random_state
    )
    #2 Definimos la malla de hiperparametros a probar (Grid)
    param_grid = {
        'n_estimators': [20, 50, 100, 150, 200],
        'max_depth': [6, 8, 12, None],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4],
        'max_features': ['sqrt', 0.5],
        'criterion': ['gini', 'entropy']
    }

    #3. Configuramos la validación cruzada
    grid_search = GridSearchCV(
        estimator=base_model,
        param_grid=param_grid,
        cv=5,
        scoring='f1', #Metrica con la que se realiza la optimización de hiperparametros
        n_jobs=1, #Utiliza todos los nucleos del procesador
        verbose=1
    )

    print("Iniciando GridSearchCV (Probando combinaciones con CV=5)...")
    grid_search.fit(X_train, y_train)

    # 4. Imprimimos los mejores resultados en consola para nuestro control
    print(f"Mejores parámetros encontrados: {grid_search.best_params_}")
    print(f"Mejor F1-Score en validación cruzada: {grid_search.best_score_:.4f}")

    return grid_search.best_estimator_


def predict_model(model, X_test):

    return model.predict(X_test)



    

    