import streamlit as st

st.set_page_config(page_title="Inicio")

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