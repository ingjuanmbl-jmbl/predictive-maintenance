from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)


def evaluate_model(y_test, y_pred)-> dict: 
    """
    Calcula las métricas clave de rendimiento para un modelo de clasificación.

    Transforma los resultados de evaluación tradicionales de Scikit-Learn en un 
    diccionario estructurado, facilitando su posterior exportación o registro.

    Argumentos:
        y_test (array-like o pd.Series): Valores reales y objetivos del conjunto 
            de prueba.
        y_pred (array-like o pd.Series): Valores predichos por el modelo.

    Retorna:
        dict: Un diccionario que contiene las siguientes métricas de evaluación:
            - "accuracy" (float): Exactitud global del modelo.
            - "precision" (float): Precisión del modelo.
            - "recall" (float): Sensibilidad (médica/operativa) del modelo.
            - "f1_score" (float): Media armónica entre precisión y recall.
            - "confusion_matrix" (list): Matriz de confusión estructurada como lista anidada.
            - "classification_report" (dict): Reporte detallado de métricas por clase.
    """

    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred),
        "confusion_matrix": confusion_matrix(
            y_test,
            y_pred
        ).tolist(),
        "classification_report": classification_report(
            y_test,
            y_pred,
            output_dict=True
        )
    }

    return metrics