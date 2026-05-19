import pandas as pd


def descriptive(df: pd.DataFrame) -> pd.DtaFrame:
    """
    Calculas mas estadisticas descriptivas de las variables ya parametrizadas

    Parametros:
        df: pd.DataFrame
            DataFrame de entrada
        ---
        Returns:
        df: pd.DataFrame
        DataFrame resultante con las estadisticas descriptivas
    """
    cols_descriptivas = ['Temp_Aire_K',
                     'Temp_Proceso_K',
                     'Velocidad_Rotacion_RPM',
                     'Torque_Nm',
                     'Desgaste_Herramienta_min',
                     'Potencia_W',
                     'Dif_temperatura_K',
                     'Esfuerzo_desgaste',
                     'Falla_Maquina']

    stat = df[cols_descriptivas].describe().T
    return stat

def coef_cv(df: pd.DataFrame) -> pd.DtaFrame:
    # Calculo del coeficiente de variación

    cols_cv = ['Temp_Aire_K',
               'Temp_Proceso_K', 
               'Velocidad_Rotacion_RPM', 
               'Torque_Nm', 
               'Desgaste_Herramienta_min',
               'Potencia_W',
               'Dif_temperatura_K',
               'Esfuerzo_desgaste',
               ]


    resultados_cv = []

    for cols in cols_cv:
        cv =(df[cols].std()/df[cols].mean())*100

        resultados_cv.append({'variable': cols,
                                'std':df[cols].std(),
                                'mean':df[cols].mean(),
                                'cv_%': round(cv, 2)

                                })

    df_cv = pd.DataFrame(resultados_cv).sort_values(by='cv_%', ascending=False)
    return df_cv

def df_corr(df: pd.DataFrame,
            method: str = 'spearman') -> pd.DataFrame:
    """
    Calcula matriz de correlación mediante el método de spearman
    ---
        Parametros:
        df : pd.DataFrame
            DataFrame de entrada

            method : str, optional
            Método de correlación: 'pearson', 'spearman' o 'kendall'.
        
        -------
        
        Returns:
        pd.DataFrame
        Matriz de correlación.

    """
    cols_corr = ['Temp_Aire_K',
               'Temp_Proceso_K', 
               'Velocidad_Rotacion_RPM', 
               'Torque_Nm', 
               'Desgaste_Herramienta_min',
               'Potencia_W',
               'Dif_temperatura_K',
               'Esfuerzo_desgaste',
               'Falla_Maquina'
               ]
    
    corr = df[cols_corr].corr(method = method)

    return corr