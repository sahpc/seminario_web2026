
**2. `07_CONTEXTO/01_RESUMEN_DEL_CASO.md`**
```md
# Resumen del Caso: Predicción de Utilidad de Reseñas de Amazon

## 1. Resumen del caso
Este proyecto analiza reseñas de productos en Amazon con el fin de entender qué características hacen que una reseña sea considerada útil por otros usuarios. Las reseñas cumplen un rol central en el proceso de compra porque reducen la incertidumbre, aportan evidencia social y ayudan a comparar alternativas.

A partir del dataset histórico de Amazon Fine Food Reviews, se busca identificar patrones en variables como la longitud del texto, el puntaje otorgado, la fecha, el nivel de detalle y el sentimiento de la reseña. El propósito es construir una base analítica sólida que permita priorizar reseñas relevantes y apoyar futuras decisiones de producto, ranking o recomendación.

## 2. Contexto del dominio
Amazon opera en un entorno donde la confianza del comprador es clave para la conversión. En comercio electrónico, los usuarios no pueden inspeccionar físicamente los productos, por lo que dependen más de señales informativas como reseñas, calificaciones y votos de utilidad.

La decisión de destacar ciertas reseñas puede afectar:
- La conversión de compra
- La confianza del usuario
- El tiempo necesario para evaluar un producto
- La calidad percibida de la plataforma

### ¿Quién toma la decisión?
- Equipos de producto y experiencia de usuario
- Equipos de ranking y recomendación
- Equipos de analítica y growth

### Incentivos del negocio
- Mostrar primero las reseñas más útiles
- Reducir ruido informativo
- Mejorar la experiencia de descubrimiento del producto
- Aumentar la probabilidad de compra

## 3. Fuentes externas
1. Chen, Y. y Xie, J. (2008). Online Consumer Review: Word-of-Mouth as a New Element of Marketing Communication Mix.
2. McAuley, J., Pandey, R. y Leskovec, J. (2015). Inferring networks of substitutable and complementary products.
3. Deloitte. (2023). Digital Commerce Consumer Signals Report.
4. Kaggle. Amazon Fine Food Reviews Dataset: https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews

## 4. Pregunta de negocio principal
¿Qué características de una reseña aumentan la probabilidad de que otros usuarios la consideren útil?

## 5. Preguntas secundarias
- ¿Las reseñas más largas tienen mayor utilidad percibida?
- ¿El sentimiento extremo reduce la percepción de utilidad?
- ¿Las reseñas con más estructura textual reciben más votos útiles?
- ¿Existen diferencias por periodo de tiempo o tipo de calificación?

## 6. Métrica de éxito
### KPI de negocio
Aumentar la proporción de reseñas útiles visibles para el usuario en posiciones tempranas del ranking.

### Métrica analítica
Se usará como variable base:
`helpfulness_ratio = HelpfulnessNumerator / HelpfulnessDenominator`

### Dirección esperada
- Mayor `helpfulness_ratio`
- Mejor capacidad para identificar reseñas útiles antes de mostrarlas al usuario

## 7. Diccionario de variables
Completar esta tabla con resultados reales del EDA y perfilamiento del dataset.

| Variable | Tipo | Descripción | Rango / valores | % nulos | Observaciones |
|---|---|---|---|---|---|
| Id | int | Identificador de la reseña | Enteros positivos | 0% | Llave técnica |
| ProductId | string | Identificador del producto | Texto | 0% | Alta cardinalidad |
| UserId | string | Identificador del usuario | Texto | 0% | Alta cardinalidad |
| ProfileName | string | Nombre visible del usuario | Texto | X% | Puede tener nulos |
| HelpfulnessNumerator | int | Número de votos útiles | >= 0 | 0% | Parte de la variable objetivo |
| HelpfulnessDenominator | int | Número total de votos | >= 0 | 0% | Revisar ceros |
| Score | int | Calificación del producto | 1 a 5 | 0% | Variable ordinal |
| Time | datetime | Fecha de publicación | Fecha | 0% | Convertir desde timestamp |
| Summary | string | Resumen corto de la reseña | Texto | X% | Revisar nulos |
| Text | string | Cuerpo de la reseña | Texto libre | 0% | Variable principal para NLP |
| helpfulness_ratio | float | Proporción de utilidad | 0 a 1 | N/A | Variable derivada |

## 8. Hipótesis iniciales
1. Las reseñas con mayor número de palabras tienen un `helpfulness_ratio` promedio más alto.
2. Las reseñas con puntaje intermedio o argumentado son percibidas como más útiles que las extremadamente positivas o negativas.
3. Las reseñas con más oraciones y mejor estructura textual reciben más votos útiles.
4. Las reseñas con resumen y texto consistentes entre sí tienden a ser más útiles.
5. Las reseñas publicadas en periodos de alta demanda presentan patrones distintos de utilidad.
6. Las reseñas con mayor densidad informativa y menor ruido textual generan más confianza.

## 9. Relevancia para la decisión
Este análisis permitirá definir criterios para priorizar reseñas útiles, mejorar la experiencia del comprador y sentar una base para un sistema futuro de clasificación o recomendación de contenido generado por usuarios.
