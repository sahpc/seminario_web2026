# 🧹 Plan de Preparación de Datos

## 📌 Objetivo

Preparar el dataset de reseñas de Amazon para su análisis exploratorio y modelado predictivo, asegurando calidad, consistencia y relevancia de la información.

---

## 🔄 1. Carga de datos

Se carga el dataset original desde la carpeta `00_datos_crudos/`.

✔ Justificación:
Trabajar siempre desde datos originales sin modificar permite mantener trazabilidad y reproducibilidad.

---

## 🧽 2. Limpieza de datos

### 🔹 2.1 Manejo de valores nulos

* Se eliminan registros con valores nulos en columnas críticas como `Text` y `Score`
* Se mantiene `ProfileName` y `Summary` aunque tengan pocos nulos

✔ Justificación:
Las columnas clave deben estar completas para análisis confiable. Otras columnas tienen bajo impacto en el modelo.

---

### 🔹 2.2 Eliminación de duplicados

* Se eliminan filas duplicadas completas

✔ Justificación:
Evita sesgos y duplicación de información en el modelo.

---

### 🔹 2.3 Manejo de denominador cero

* Se eliminan registros donde `HelpfulnessDenominator = 0`

✔ Justificación:
No es posible calcular la variable objetivo (`helpfulness_ratio`).

---

## 📊 3. Transformación de variables

### 🔹 3.1 Conversión de tipos

* `Time` → convertido a formato datetime

✔ Justificación:
Permite análisis temporal y creación de nuevas variables.

---

### 🔹 3.2 Creación de variable objetivo

```python
helpfulness_ratio = HelpfulnessNumerator / HelpfulnessDenominator
```

✔ Justificación:
Representa la proporción de utilidad de la reseña.

---

### 🔹 3.3 Variables derivadas (feature engineering)

Se crean nuevas variables para capturar características del texto:

* `word_count`: número de palabras
* `sentence_count`: número de oraciones
* `review_length`: longitud del texto en caracteres
* `sentiment`: análisis de sentimiento
* `avg_word_length`: longitud promedio de palabras
* `exclamation_count`: cantidad de signos de exclamación
* `question_count`: cantidad de signos de interrogación

✔ Justificación:
Estas variables ayudan a capturar calidad, complejidad y emoción del texto, lo cual influye en la utilidad.

---

## 🚨 4. Detección y tratamiento de outliers

### 🔹 Método IQR

* Se detectan valores extremos en `helpfulness_ratio` y `word_count`

✔ Acción:

* Se eliminan valores fuera del rango permitido

✔ Justificación:
Los outliers pueden distorsionar el modelo y afectar la interpretación.

---

## 🔠 5. Procesamiento de texto

* Limpieza básica (minúsculas, eliminación de caracteres especiales)
* Tokenización

✔ Justificación:
Permite análisis NLP y mejora la calidad de las features.

---

## 🔄 6. Normalización (opcional)

* Aplicación de escalado a variables numéricas

✔ Justificación:
Algunos modelos requieren variables en la misma escala.

---

## ❌ 7. Variables descartadas

| Variable    | Motivo                     |
| ----------- | -------------------------- |
| Id          | No aporta valor predictivo |
| ProfileName | Información irrelevante    |
| UserId      | Alta cardinalidad          |
| ProductId   | Alta cardinalidad          |

✔ Justificación:
Estas variables no aportan directamente a la predicción o generan ruido.

---

## 📦 8. Exportación de datos

* Se guarda el dataset limpio en:

```
01_datos_procesados/
```

✔ Formato:

* `.csv` o `.parquet`

✔ Justificación:
Facilita reutilización en análisis y modelado.

---

## 🎯 Conclusión

Este proceso asegura un dataset limpio, consistente y enriquecido con variables relevantes que permitirán un análisis robusto y modelos predictivos más precisos.
