# 🧠 Contexto del Caso: Predicción de Utilidad de Reseñas de Amazon

## 📌 Resumen del caso

Este proyecto analiza reseñas de productos en Amazon con el objetivo de predecir qué tan útiles son para otros usuarios. Las reseñas cumplen un papel fundamental en el proceso de compra, ya que influyen directamente en la percepción del producto y en la decisión final del consumidor.

A partir de datos históricos, se busca identificar patrones en el contenido textual y en las características de las reseñas que permitan estimar su utilidad. Esto permitirá priorizar reseñas relevantes y mejorar la experiencia del usuario en plataformas de comercio electrónico.

---

## 🏢 Contexto del dominio

Amazon es una plataforma de comercio electrónico donde millones de usuarios compran productos basándose, en gran medida, en opiniones de otros compradores. Las reseñas funcionan como un sistema de recomendación social.

### 👤 ¿Quién toma decisiones?

* Equipos de producto (UX / recomendación)
* Sistemas de ranking de contenido
* Algoritmos de recomendación

### 🎯 Incentivos del negocio

* Aumentar conversiones de compra
* Mejorar la confianza del usuario
* Reducir incertidumbre en decisiones
* Destacar contenido de alta calidad

### 📚 Fuentes externas

* Chen, Y., & Xie, J. (2008). Online Consumer Review
* McAuley et al. (2015). Amazon Review Dataset
* Deloitte (2023). Digital Commerce Report

---

## ❓ Pregunta de negocio

### 🔹 Pregunta principal

¿Qué características hacen que una reseña sea percibida como útil por otros usuarios?

### 🔹 Preguntas secundarias

* ¿La longitud del texto influye en la utilidad?
* ¿El sentimiento de la reseña afecta su percepción?
* ¿Las reseñas extremas (1 o 5 estrellas) son menos útiles?

---

## 📈 Métrica de éxito

La métrica principal será:

**helpfulness_ratio = HelpfulnessNumerator / HelpfulnessDenominator**

### 🎯 Objetivo:

* Maximizar la capacidad predictiva del modelo sobre esta variable
* Identificar reseñas con alta probabilidad de ser útiles

---

## 📊 Diccionario de variables

| Variable               | Tipo     | Descripción         | Rango | % Nulos | Observaciones  |
| ---------------------- | -------- | ------------------- | ----- | ------- | -------------- |
| Id                     | int      | Identificador único | -     | 0%      |                |
| ProductId              | string   | ID del producto     | -     | 0%      |                |
| UserId                 | string   | ID del usuario      | -     | 0%      |                |
| ProfileName            | string   | Nombre del usuario  | -     | ~0.01%  |                |
| HelpfulnessNumerator   | int      | Votos útiles        | ≥0    | 0%      |                |
| HelpfulnessDenominator | int      | Total de votos      | ≥0    | 0%      |                |
| Score                  | int      | Calificación        | 1–5   | 0%      |                |
| Time                   | datetime | Fecha de reseña     | -     | 0%      |                |
| Summary                | string   | Resumen corto       | -     | ~0.01%  |                |
| Text                   | string   | Texto completo      | -     | 0%      |                |
| helpfulness_ratio      | float    | Utilidad calculada  | 0–1   | -       | Feature creada |

---

## 🧪 Hipótesis iniciales

1. Las reseñas con mayor número de palabras tienen mayor utilidad percibida
2. Las reseñas con estructura clara (más oraciones) son más útiles
3. Las reseñas con sentimiento moderado son más confiables que las extremas
4. Usuarios con más experiencia generan reseñas más útiles
5. Las reseñas con mayor número de votos tienen mayor confiabilidad
6. Reseñas con lenguaje más detallado (palabras largas) son más útiles

---

## 🎯 Conclusión

Comprender qué hace útil una reseña permite mejorar los sistemas de recomendación y la experiencia del usuario. Este análisis permitirá desarrollar modelos predictivos que automaticen la identificación de contenido valioso dentro de grandes volúmenes de datos.
