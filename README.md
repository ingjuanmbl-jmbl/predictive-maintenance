# ⚙️ Sistema de Mantenimiento Predictivo Inteligente (Fase 1: Enfoque Binario)

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-F7931E.svg)
![MLflow](https://img.shields.io/badge/MLOps-MLflow-0194E2.svg)
![Random Forest](https://img.shields.io/badge/Algorithm-Random%20Forest-green.svg)

Este repositorio contiene el core técnico y la interfaz interactiva de una solución de **Analítica Predictiva y Prescriptiva** aplicada al sector industrial. El sistema procesa señales en tiempo real de sensores IoT para interceptar fallas en fresadoras CNC antes de que ocurra un colapso en la línea de producción.

👉 **Puedes interactuar con la Web App en vivo aquí:** [predictive-maintenance-ejvwjrs7hprjxhcmv3h5b5.streamlit.app](https://predictive-maintenance-ejvwjrs7hprjxhcmv3h5b5.streamlit.app/)

---

## 🎯 1. Contexto de Negocio e Impacto
En la planta piloto "Industrial Tech Solutions" (basada en el dataset **AI4I 2020**), los paros de línea no programados y el scrap por descalibración térmica representan un **Costo de No Calidad estimado en el 18% de las ventas anuales**. 

Este proyecto migra la estrategia operativa de un enfoque preventivo tradicional (basado en tiempo) a un enfoque **predictivo y prescriptivo**, permitiendo:
1. Minimizar las falsas alarmas que detienen la producción innecesariamente.
2. Alertar al operario con una acción prescriptiva clara basada en la probabilidad del riesgo.

---

## 📐 2. Arquitectura de Software y Modularización
El proyecto se diseñó bajo principios de código limpio y desacoplamiento de responsabilidades, facilitando su mantenibilidad y futura escalabilidad (como la Fase 2 Multiclase).

```
predictive-maintenance/
│
├── .streamlit/              # Configuración visual de la interfaz (config.toml)
├── .venv/                   # Entorno virtual de Python
├── artifacts/               # Modelos serializados (.joblib) y JSON de métricas
├── data/                    # Set de datos industrial (AI4I 2020)
├── mlruns/                  # Registro local de experimentos y ejecuciones de MLflow
├── notebooks/               # Sandboxing y Análisis Exploratorio (EDA) inicial
├── src/                     # Código fuente modular (ETL, utilidades de carga)
├── views/                   # Vistas modulares de la interfaz de Streamlit
│
├── .gitignore               # Exclusión de archivos pesados y entornos virtuales
├── app.py                   # Orquestador principal y enrutamiento del menú
├── main.py                  # Script de ejecución del pipeline principal
├── mlflow.db                # Base de datos relacional para el tracking de MLflow
├── README.md                # Documentación técnica del proyecto
└── requirements.txt         # Dependencias del entorno de producción
└── LICENCE.txt              # LICENCIA DE USO
```
## 🧠 3. Ingeniería de Características (Feature Engineering)

El modelo no solo se alimenta de las métricas crudas de los sensores; incorpora variables calculadas basadas en principios físicos de la ingeniería mecánica para potenciar el poder predictivo.

### Potencia Física (W)
Relación matemática entre el torque y la velocidad de rotación.

$$
P = \frac{RPM \times T}{9.5488}
$$

Donde:

- $P$ = Potencia mecánica (W)
- $RPM$ = Velocidad de rotación
- $T$ = Torque (Nm)

---

### Diferencial de Temperatura (ΔK)
Indicador de esfuerzo térmico en la herramienta.

$$
\Delta T = T_{proceso} - T_{aire}
$$

Donde:

- $\Delta T$ = Diferencial térmico
- $T_{proceso}$ = Temperatura del proceso
- $T_{aire}$ = Temperatura ambiente

---

### Esfuerzo de Desgaste
Interacción acumulada entre fuerza de torsión y tiempo de uso.

$$
E_d = T \times t
$$

Donde:

- $E_d$ = Esfuerzo de desgaste
- $T$ = Torque (Nm)
- $t$ = Tiempo de desgaste de herramienta (min)
$$

---

## 📊 4. Rendimiento del Modelo (Fase Binaria)
Tras evaluar múltiples algoritmos y registrar su ciclo de vida en **MLflow**, el modelo **RandomForestClassifier** optimizado arrojó las siguientes métricas clave en el conjunto de prueba:

| Métrica | Valor | Impacto Operativo |
| :--- | :--- | :--- |
| **Precisión (Precision)** | **89.83%** | De cada 10 alertas de fallo, 9 son reales. Reduce el escepticismo de los operarios. |
| **Sensibilidad (Recall)** | **77.94%** | Captura casi el 78% de las fallas mecánicas reales antes de que sucedan. |
| **Especificidad** | **> 99.00%** | Tasa de error en estado normal inferior al 1%. Evita paros en falso de la planta. |

---

🛠️ Próximos Pasos (Fase 2)

* Evolución Multiclase: Reingeniería del pipeline para clasificar la causa raíz exacta de la falla (HDF, PWF, OSF, TWF).
*  Mapeo con MLflow: Apertura de una nueva línea de experimentación dedicada en el Model Registry para control de versiones del modelo multiclase.

---
## 📄 Licencia

Este proyecto está bajo la licencia **Creative Commons Atribución-NoComercial-CompartirIgual 4.0 Internacional (CC BY-NC-SA 4.0)**.

<p align="left">
  <a href="https://creativecommons.org/licenses/by-nc-sa/4.0/deed.es" target="_blank">
    <img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-nc-sa.svg" alt="CC BY-NC-SA 4.0" height="40">
  </a>
</p>

Puedes usar, copiar y modificar este código con fines educativos, de aprendizaje o para tu propio portafolio, siempre y cuando otorgues el crédito correspondiente y compartas tus derivados bajo esta misma licencia. Queda prohibida su comercialización sin autorización previa.