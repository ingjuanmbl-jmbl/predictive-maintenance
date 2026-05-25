import streamlit as st
import pandas as pd
import os
import sys

from src.utils import load_model

# Esto asegura que 'src' sea visible sin importar desde dónde se ejecute el script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)



def render_predict():
    st.header("Simulador de Diagnóstico en Tiempo Real")
    st.markdown(
        """
        Modifica los parámetros de operación de la fresadora CNC para evaluar el
        riesgo inminente de falla mediante el modelo predictivo.
        """
    )

    st.write("---")

    #Cargamos el modelos que se usará para realizar predicciones
    model = load_model("artifacts/save_model/model_rf.joblib")
    if model is None:
        return
    
    #Columnas para cargar los inputs del usuario de forma ejecutiva
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🌡️ Variables Térmicas")
        temp_aire = st.slider("Temperatura del Aire (K)",
                            min_value= 290.0,
                            max_value=305.0,
                            step=0.1)
        
        temp_proceso = st.slider("Temperatura del Proceso (K)",
                                min_value=300.0, max_value=315.0,
                                value=308.0,
                                step=0.1)
    
    with col2:
        st.subheader("⚙️ Variables Mecánicas")
        velocidad = st.number_input("Velocidad de Rotación (RPM)",
                                    min_value=1000,
                                    max_value=3000,
                                    value=1500,
                                    step=50)
        
        torque = st.slider("Torque (Nm)",
                            min_value=3.0,
                            max_value=80.0,
                            value=40.0,
                            step=0.1)
        
        desgaste = st.number_input("Desgaste de Herramienta (min)",
                                   min_value=0,
                                   max_value=300,
                                   value=60,
                                   step=5)

    st.write("---")
    #Procesamiento interno, variables calculadas

    # 1. Cálculo de la potencia
    potencia = (velocidad * torque) / 9.5488
    
    # 2. Diferencial de temperatura
    dif_temp = temp_proceso - temp_aire
    
    # 3. Factor de desgaste torque
    esfuerzo_desgaste = torque * desgaste

    #Crear el input de datos exactamente en el mismo orden que se entreno el modelo
    input_data = pd.DataFrame([{
        'Temp_Aire_K': temp_aire,
        'Temp_Proceso_K': temp_proceso,
        'Velocidad_Rotacion_RPM': velocidad,
        'Torque_Nm': torque,
        'Desgaste_Herramienta_min': desgaste,
        'Potencia_W': potencia,
        'Dif_temperatura_K': dif_temp,
        'Esfuerzo_desgaste': esfuerzo_desgaste
    }])

    #Mostramos las variables con las variables calculadas para que garantizar transparencia en el proceso
    with st.expander("🔍 Ver variables de Ingeniería de Características calculadas en el fondo"):
        st.dataframe(input_data[['Potencia_W', 'Dif_temperatura_K', 'Esfuerzo_desgaste']].round(2), use_container_width=True)
    
    #Boton de inferencia
    if st.button("🚀 Evaluar Estado de la Máquina", type="primary", use_container_width=True):

        #1. Calcular probabilidad dura
        prediccion = model.predict(input_data)[0]

        #2. Calcular probabilidad de falla
        propabilidades = model.predict_proba(input_data)[0]
        propalidad_falla = propabilidades[1] * 100  #Convertimos a % para facilitar su lectura

        st.subheader("📊 Resultado del Diagnóstico")
        
        # --- NUEVA LÓGICA DE SEMÁFORO EN BASE A LA PROBABILIDAD ---
        
        # Nivel 1: Crítico (Mayor al 90%)
        if propalidad_falla > 90.0:
            st.error(f"🚨 **ALERTA DE FALLA INMINENTE:** El riesgo de colapso mecánico/térmico es extremadamente alto.")
            st.metric(
                label="Probabilidad de Falla", 
                value=f"{propalidad_falla:.2f}%", 
                delta="Riesgo Crítico", 
                delta_color="inverse"
            )
            st.warning("⚠️ **Acción Prescriptiva Urgente:** Se recomienda detener la línea de producción de inmediato para inspección preventiva y evitar daños severos en la herramienta CNC.")
        
        # Nivel 2: Advertencia (Entre 50% y 90%)
        elif propalidad_falla >= 50.0:
            st.warning(f"🟡 **ATENCIÓN: POSIBLE FALLA:** La máquina muestra un comportamiento anómalo fuera de los parámetros ideales.")
            st.metric(
                label="Probabilidad de Falla", 
                value=f"{propalidad_falla:.2f}%", 
                delta="Monitoreo Requerido", 
                delta_color="off"
            )
            st.info("💡 **Acción Recomendada:** Programar una revisión de mantenimiento preventivo al finalizar el turno actual. Verificar lubricación, torque y nivel de desgaste físico.")
        
        # Nivel 3: Seguro (Menor al 50%)
        else:
            st.success(f"🟢 **OPERACIÓN SEGURA:** La máquina se encuentra trabajando bajo parámetros totalmente estables.")
            st.metric(
                label="Probabilidad de Falla", 
                value=f"{propalidad_falla:.2f}%", 
                delta="Condición Estable"
            )

# Para probar la vista de manera aislada si es necesario
if __name__ == "__main__":
    render_predict()



