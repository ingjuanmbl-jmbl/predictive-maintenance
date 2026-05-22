import streamlit as st



def context():
    st.markdown("""
                # **Analisis Predictivo Industrial**

                ## **Contexto de la Operación**
                La empresa "Industrial Tech Solutions" opera fresadoras CNC de alta precisión. Actualmente, la planta utiliza un modelo de mantenimiento preventivo basado en tiempo (se cambia la herramienta cada X horas) y mantenimiento correctivo (se reacciona cuando la máquina falla).

                A pesar de cumplir con los cronogramas de mantenimiento, la planta sigue experimentando:

                * Paros de línea no programados que detienen la producción por horas.

                * Lotes de productos defectuosos debido a variaciones térmicas y de torque no detectadas a tiempo.

                ## **Definición del Problema (El "Asesino Silencioso")**

                El problema principal es la Variabilidad No Detectada. Los ingenieros de planta no pueden monitorear manualmente la relación entre la temperatura del aire, la velocidad de rotación y el desgaste de la herramienta en tiempo real.

                **Consecuencia económica:**

                Costo de No Calidad: Se estima en un 18% de las ventas anuales debido a scrap y re-trabajos.

                Ineficiencia de Datos: Se generan miles de registros por segundo a través de sensores IoT, pero menos del 5% se analizan (Dark Data).

                ## **Objetivo del Proyecto (Analítica Prescriptiva)**

                Utilizar el dataset AI4I 2020 para desarrollar un modelo de Machine Learning capaz de:

                1. Predecir fallos prematuros con una ventana de tiempo suficiente para intervenir.

                2. Identificar las variables con mayor correlación de incidencia de fallo de la maquina

                3. Cuantificar el impacto de establecer un modelo de mantenimiento predictivo en la planta

                            
                """)

    st.markdown("""
    ## Significado de las variables

    | Nombre Original | Nombre en español | Tipo | Descripción técnica |
    | :--- | :--- | :---: | :--- |
    | Type (L, M, H) | Tipo_Material | Original | Nivel de dureza del material procesado: Low (50%), Medium (30%) y High (20%). |
    | Air temperature [K] | Temp_Aire_K | Original | Temperatura ambiente del sistema medida en Kelvin, influenciada por el sistema de refrigeración. |
    | Process temperature [K] | Temp_Proceso_K | Original | Temperatura generada durante el proceso de mecanizado debido a la fricción y operación de corte. |
    | Rotational speed [rpm] | Velocidad_Rotacion_RPM | Original | Velocidad de rotación del eje o cabezal de la máquina medida en revoluciones por minuto. |
    | Torque [Nm] | Torque_Nm | Original | Fuerza de torsión aplicada sobre la herramienta durante el proceso de mecanizado. |
    | Tool wear [min] | Desgaste_Herramienta_min | Original | Tiempo acumulado de uso de la herramienta de corte expresado en minutos. |
    | Machine failure | Falla_Maquina | Original | Variable objetivo binaria que indica si ocurrió una falla general en la máquina. |
    | TWF | Falla_Desgaste_Herramienta | Original | Falla ocasionada por desgaste excesivo de la herramienta de corte. |
    | HDF | Falla_Disipacion_Calor | Original | Falla generada por problemas de disipación térmica o sobrecalentamiento. |
    | PWF | Falla_Potencia | Original | Falla causada por condiciones anormales relacionadas con potencia o carga operativa. |
    | OSF | Falla_Sobreesfuerzo | Original | Falla provocada por sobreesfuerzo mecánico o exceder límites operativos. |
    | RNF | Falla_Aleatoria | Original | Falla aleatoria no asociada directamente a condiciones específicas del proceso. |
    | Potencia_W | Potencia_W | Creada | Variable derivada que estima la potencia mecánica del sistema a partir de la velocidad de rotación y el torque aplicado. |
    | Dif_temperatura_K | Dif_temperatura_K | Creada | Diferencia entre la temperatura del proceso y la temperatura ambiente, utilizada para medir esfuerzo térmico. |
    | Esfuerzo_desgaste | Esfuerzo_desgaste | Creada | Indicador compuesto entre torque y desgaste acumulado de la herramienta para representar nivel de exigencia mecánica. |
                """)
    
if __name__ == "__main__":
    context()