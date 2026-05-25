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

## 💵 5. Supuesto Teórico del Impacto Económico (ROI)

Para cuantificar el valor estratégico del modelo en la planta de producción, se estructuró un análisis de Retorno de Inversión (ROI) simulando un histórico de **100 eventos de falla potenciales al año**, contrastando las métricas reales de nuestra matriz de confusión (*Recall*: 77.94%, *Precision*: 89.83%).

### 🚨 1. Anatomía de una Falla Catastrófica (Enfoque Reactivo - Sin Modelo)
Si la máquina rompe por fatiga total debido a una falla no detectada:
* **Repuesto de urgencia:** $2,500 USD (Husillo, rodamientos o motor adquiridos con recargo por tiempo).
* **Mano de obra especializada externa:** $500 USD (Tarifa de emergencia).
* **Parada de línea no programada:** $7,200 USD ($1,200 USD/hora × 6 horas de lucro cesante).
* 💰 **Costo Total por Falla Reactiva:** **$10,200 USD**

### 🛠️ 2. Anatomía del Mantenimiento Predictivo (Enfoque Proactivo - Con Modelo)
Si el modelo emite una alerta temprana y se programa la intervención:
* **Repuesto planificado:** $1,500 USD (Adquirido a precio de mercado estándar).
* **Mano de obra interna:** $200 USD (Ejecutado por técnicos de la planta en turno normal).
* **Parada programada:** $0 USD (La intervención de 2 horas se agenda en ventanas de cambio de turno o fines de semana).
* 💰 **Costo Total por Falla Mitigada:** **$1,700 USD**

### ⚠️ 3. Costo por Falsa Alarma (Falso Positivo)
Debido a que la Precisión del modelo es del 89.83%, existe un riesgo de ~10% de alertas falsas que conllevan una inspección preventiva innecesaria:
* **Mano de obra para verificación:** $50 USD (Inspección rápida de 30 minutos sin cambio de componentes).

---

### 📊 Análisis Consolidado de Impacto Anual

| Escenario | Desglose del Cálculo | Costo Total Anual |
| :--- | :--- | :--- |
| **Escenario A: Tradicional** | 100 fallas catastróficas × $10,200 | $1,020,000 USD |
| **Escenario B: Con Modelo** | (78 fallas mitigadas × $1,700) + (22 fallas no capturadas × $10,200) + (10 falsas alarmas × $50) | $357,100 USD |

### 📉 Resultados Clave:
* 💰 **Ahorro Neto Estimado:** **$662,900 USD / año**.
* 📉 **Reducción del 65%** en los costos globales de mantenimiento de la planta CNC.
* 🛡️ **Riesgo Residual Controlado:** El 22% de costo remanente representa las fallas no capturadas por el *Recall* (22 de cada 100), justificando el desarrollo de la **Fase 2 (Modelo Multiclase)** para afinar la sensibilidad del diagnóstico.

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

Puedes compartir unicamente este código bajo fines educativos, siempre y cuando otorgues el crédito correspondiente y compartas tus derivados bajo esta misma licencia. Queda prohibida su comercialización sin autorización previa.