import streamlit as st
import pandas as pd
import os
import sys
import plotly.express as px



# Esto asegura que 'src' sea visible sin importar desde dónde se ejecute el script
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from src.stats import (descriptive,
                       coef_cv,
                       df_corr)




def show_eda():
    #Cargar data set
    @st.cache_data

    def cargar_datos():
        path = "data/clean/data_clean.csv"
        df = pd.read_csv(path)
        return df

    df = cargar_datos()

    #Realizamos analisis estaditico básico
    st.subheader("Resumen Estadístico de la Operación")

    stat = descriptive(df)

    # Mostramos en tabla resumen en el tablero
    st.dataframe(
        stat.style.format("{:.2f}") # Solo 2 decimales para que sea legible
    )

    #Calculamos el coeficiente de variación
    st.subheader("Análisis basado en el coeficiente de variación")

    df_coef = coef_cv(df)
    df_coef = df_coef.sort_values(by='cv_%', ascending=False)

    fig = px.bar(
        df_coef,
        x = 'variable',
        y = "cv_%",
        title="Coeficiente de Variación por Variable",
        text='cv_%'
    )

    fig.update_layout(
        xaxis_title= 'Variable',
        yaxis_title='cv (%)'
    )

    st.plotly_chart(fig, use_container_width=True)


    #### ANALISIS GRAFICO DE LA VARIABILDIAD #####

    #Asignamos una lista con las variables que deseamos analizar

    variables = [
        'Temp_Aire_K',
        'Temp_Proceso_K',
        'Velocidad_Rotacion_RPM',
        'Torque_Nm',
        'Desgaste_Herramienta_min',
        'Potencia_W',
        'Dif_temperatura_K',
        'Esfuerzo_desgaste',
        'Falla_Maquina'
    ]



    #################
    ### SELECTOR ####
    #################

    variable = st.selectbox(
        "Seleccione una variable a analizar",
        variables
    )

    variable_dos = st.selectbox(
        "Seleccione una variable a analizar - (Para Scatterplot)",
        variables
    )

    st.divider()

    #################
    ### COLUMNAS ####
    #################

    col1, col2, col3 = st.columns(3)


    #################
    ### 1.BOXPLOT ###
    #################

    with col1:
        fig_box = px.box(
            df,
            x = "Estado_Falla",
            y = variable,
            color = "Estado_Falla",
            points = 'outliers',
            title=f'Boxplot de {variable}'
            )
        
        fig_box.update_layout(
            showlegend=False
        )

        st.plotly_chart(
            fig_box,
            use_container_width=True
        )

    with col2:

        fig_hist = px.histogram(
            df,
            x=variable,
            color='Estado_Falla',
            barmode='overlay',
            opacity=0.6,
            marginal='box',
            title=f'Histograma de {variable}'
        )

        st.plotly_chart(
            fig_hist,
            use_container_width=True
        )

    # =========================
    # 3. SCATTERPLOT
    # =========================

    with col3:

        fig_scatter = px.scatter(
            df,
            x= variable,
            y= variable_dos,
            color='Estado_Falla',
            size='Torque_Nm',
            hover_data=[
                'Potencia_W',
                'Velocidad_Rotacion_RPM'
            ],
            title=f'Relación Torque vs {variable}'
        )

        st.plotly_chart(
            fig_scatter,
            use_container_width=True
        )

        fig_scatter.update_layout(
        xaxis_title= variable,
        yaxis_title=variable_dos
        )

    #Analisis de correlación

    st.subheader("Análisis de Correlación")

    method = st.selectbox(
        'Método',
        ['pearson', 'spearman']
    )

    #Calculamos la matriz de correlación
    corr_matriz = df_corr(df, method)

    #Graficamos con heatmap Interactivo
    fig = px.imshow(
        corr_matriz,
        text_auto='.2f',
        color_continuous_scale = 'RdBu_r',
        zmin = -1,
        zmax = 1,
        aspect ='auto'
    )

    fig.update_layout(
        title='Matriz de Correlación',
        width=900,
        height=700
    )

    #Instancia final del tablero
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    show_eda()