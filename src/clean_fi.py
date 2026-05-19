import pandas as pd

def rename_cols(df: pd.DataFrame) -> pd.DataFrame:
    """
    Realiza proceso de limpieza de columnas
        Args:
        df: Corresponde al dataset previamente cargado
    """


    #Renombramos las columnas para un mejor entendimiento del problema
    nuevos_nombres = {
        'UDI': 'ID_Unico',
        'Product ID': 'ID_Producto',
        'Type': 'Tipo_Material',
        'Air temperature [K]': 'Temp_Aire_K',
        'Process temperature [K]': 'Temp_Proceso_K',
        'Rotational speed [rpm]': 'Velocidad_Rotacion_RPM',
        'Torque [Nm]': 'Torque_Nm',
        'Tool wear [min]': 'Desgaste_Herramienta_min',
        'Machine failure': 'Falla_Maquina',
        'TWF': 'Falla_Desgaste_Herramienta',
        'HDF': 'Falla_Disipacion_Calor',
        'PWF': 'Falla_Potencia',
        'OSF': 'Falla_Sobreesfuerzo',
        'RNF': 'Falla_Aleatoria'
    }

    df.rename(columns=nuevos_nombres, inplace=True)
    
    return df

def feature_ing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea Caracteristicas o variables nuevas que ayudan a mejorar el modelo preditivo
    """
    #1. Calculo de la potencia (Relación fisica entre Toque y velocidad)
    #Usamos contante de conversión simle (Vel * Torque) / 9.5488

    df['Potencia_W'] = (df['Velocidad_Rotacion_RPM'] * df['Torque_Nm']) / 9.5488

    #2. Diferencial de temperatura (Esfuerzo termico)
    df['Dif_temperatura_K'] = df['Temp_Proceso_K'] - df['Temp_Aire_K']

    #3 Factor de desgaste torque (que tanto sufre la herramienta)
    df['Esfuerzo_desgaste'] = df['Torque_Nm'] * df['Desgaste_Herramienta_min']
    
    #Creamos una Variable más visual para representar cuando la maquina falla y cuando no
    df['Estado_Falla'] = df['Falla_Maquina'].map({
    0: 'No Falla',
    1: 'Falla'
})

    print("Variables Creadas Exitosamente")

    return df





