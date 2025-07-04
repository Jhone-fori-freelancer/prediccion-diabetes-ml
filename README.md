
"Predicción de Diabetes con Machine Learning y aplicación gráfica con Tkinter. Trabajo práctico integrador."

# 🔬 Predicción de Diabetes con Machine Learning

## 📑 Descripción del Proyecto
Este trabajo práctico integrador tiene como objetivo:
- Aplicar técnicas de exploración y limpieza de datos.
- Implementar modelos de Machine Learning supervisado.
- Comparar el desempeño de los modelos.
- Exportar el modelo más preciso.
- Crear una aplicación gráfica (Tkinter) que permita realizar predicciones.

---

## 📂 Estructura del Proyecto

```
📁 Prediccion_Diabetes
├── diabetes.csv                 # Dataset base (Pima Indians Diabetes Database)
├── TP_Prediccion_Diabetes.ipynb  # Notebook completo con análisis y entrenamiento
├── modelo_diabetes.pkl           # Modelo exportado (Random Forest)
├── app_diabetes.py               # Interfaz gráfica Tkinter
└── Presentacion_Diabetes.pptx    # Presentación resumen del proyecto
```

---

## 🔍 1. Exploración y limpieza de datos ✅

✔️ Dataset cargado con pandas.  
✔️ Análisis de tipos de datos y búsqueda de valores faltantes.  
✔️ Visualizaciones básicas con seaborn y matplotlib.  
✔️ Identificación de columnas con ceros sospechosos (`Glucose`, `BloodPressure`, etc.).  
✔️ Reemplazo de ceros por la mediana de cada columna.  
✔️ Normalización de los datos con `StandardScaler`.

---

## 🧠 2. Entrenamiento de modelos ✅

Se implementaron tres modelos:
- 🔹 Regresión Logística
- 🔹 Árbol de Decisión
- 🔹 Random Forest

Cada modelo fue entrenado sobre el conjunto normalizado y dividido (80% entrenamiento / 20% prueba).

---

## 📊 3. Evaluación y comparación ✅

✔️ Métricas evaluadas:
- Accuracy
- Score
- Matriz de confusión
- Reporte de clasificación (precision, recall, F1-score)

➡️ El modelo con mejor desempeño general fue **Random Forest**, con aproximadamente 80% de precisión.

---

## 💾 4. Exportación del modelo ✅

✔️ El modelo Random Forest se exportó como `modelo_diabetes.pkl` utilizando la librería `joblib`.  
✔️ El archivo exportado puede ser cargado en cualquier aplicación Python.

---

## 🖥️ 5. Interfaz Gráfica con Tkinter ✅

✔️ Se creó una app simple que permite ingresar datos manualmente.  
✔️ La app carga el modelo exportado y muestra la predicción.  
✔️ Resultado: `✅ Diabetes: Sí` o `❌ Diabetes: No`.

### Ejecución:
```bash
python app_diabetes.py
```
(asegurate de tener el modelo `modelo_diabetes.pkl` en la misma carpeta).

---

## 🎯 6. Presentación ✅

Incluye una presentación en PowerPoint (`Presentacion_Diabetes.pptx`) que resume:
- Introducción al problema
- Análisis exploratorio
- Comparación de modelos
- App Tkinter

---

## ⚙️ Requisitos

Instalar las dependencias:
```bash
pip install pandas scikit-learn matplotlib seaborn joblib
```
(Tkinter viene preinstalado con la mayoría de las versiones de Python 3).

---

## ✔️ Estado del Proyecto

| Criterio                                            | Completado |
|-----------------------------------------------------|------------|
| Exploración y limpieza de datos                     | ✅          |
| Implementación de los 3 modelos                     | ✅          |
| Evaluación y justificación del mejor modelo         | ✅          |
| Exportación del modelo para reutilización           | ✅          |
| Interfaz gráfica funcional con Tkinter              | ✅          |
| Documentación (README y presentación)               | ✅          |

---

Proyecto desarrollado por jhonatan Remon como parte del práctico integrador de la Unidad IV - Machine Learning.
