import pandas as pd
import shap


def get_feature_importance(model, features: list) -> pd.DataFrame:
    """
    Calcula la importancia global de las variables basándose en el modelo entrenado.

    Utiliza la métrica nativa del modelo (como la ganancia de Gini o entropía en árboles)
    para estructurar y ordenar los predictores según su impacto general.

    Argumentos:
        model: Objeto del modelo entrenado que posee el atributo 'feature_importances_'.
        features (list): Lista con los nombres de las variables (columnas) utilizadas.

    Retorna:
        pd.DataFrame: Un DataFrame ordenado de mayor a menor impacto con las 
            columnas ['feature', 'importance'].
    """
    importance_df = pd.DataFrame({
        "feature": features,
        "importance": model.feature_importances_
    })

    importance_df = importance_df.sort_values(
        by="importance",
        ascending=False
    )

    return importance_df


def calculate_shap_values(model, X_test: pd.DataFrame) -> tuple:
    """
    Calcula los valores SHAP utilizando un explicador basado en árboles (TreeExplainer).

    Los valores SHAP (SHapley Additive exPlanations) permiten desglosar el impacto 
    individual de cada variable para cada predicción específica, aportando 
    interpretabilidad local y gráficos de fuerza/resumen al pipeline.

    Argumentos:
        model: Objeto del modelo entrenado basado en árboles (Random Forest, XGBoost, etc.).
        X_test (pd.DataFrame): Matriz de características del conjunto de prueba.

    Retorna:
        tuple: Una tupla que contiene:
            - explainer (shap.TreeExplainer): El objeto explicador de SHAP ajustado.
            - shap_values (array o list): Los valores SHAP calculados para el conjunto X_test.
    """
    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X_test)

    return explainer, shap_values