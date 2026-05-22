import streamlit as st
from streamlit_option_menu import option_menu

# 1. Configuración de la página (DEBE ser lo primero en app.py)
st.set_page_config(
    page_title="Mantenimiento Predictivo AI",
    page_icon="⚙️",
    layout="wide"
)

# 2. Importar las vistas desde tu estructura de carpetas
from views.EDA_page import show_eda
from views.results_page import show_results
from views.context_page import context

# 3. Barra de Navegación Superior Fija (Tipo App Móvil/Web Moderna)
selected = option_menu(
    menu_title=None,               # Al poner None, quitamos el título del menú para ahorrar espacio arriba
    options=["Contexto Operativo", "Dashboard EDA", "Métricas del Modelo"], 
    icons=["book", "search", "bar-chart-line"], # Iconos estilizados de Bootstrap
    menu_icon="cast",              
    default_index=0,               
    orientation="horizontal",      # <-- ¡ESTA ES LA MAGIA! Lo vuelve barra superior
    styles={
        "container": {
            "padding": "0px!", 
            "background-color": "#111b21", 
            "border-radius": "8px",
            "margin-bottom": "25px"
        },
        "icon": {
            "color": "#00e676", 
            "font-size": "16px"
        }, 
        "nav-link": {
            "color": "#ffffff",          # <-- ¡ESTA LÍNEA ES LA MAGIA! Hace las letras visibles (Blanco)
            "font-size": "15px", 
            "text-align": "center", 
            "margin": "0px", 
            "--hover-color": "#202c33",
            "padding": "10px 0px"
        },
        "nav-link-selected": {
            "background-color": "#00a884",
            "color": "#ffffff",          # Asegura que el texto seleccionado también sea blanco continuo
            "font-weight": "bold"
        },
    }
)

# --- Contenedor Opcional para Branding Flotante ---
# Como quitamos la barra lateral, podemos poner una línea sutil arriba o abajo
# st.caption("⚙️ Industrial Tech Solutions | Analítica Avanzada")

# 4. Enrutador Dinámico (Corregido con elif)
if selected == "Contexto Operativo":
    context()
elif selected == "Dashboard EDA":
    show_eda()
elif selected == "Métricas del Modelo":
    show_results()