
**7. `01_datos_procesados/README.md`**
```md
# Datos Procesados

Esta carpeta contiene los datasets limpios y transformados que resultan del proceso de preparación.

## Archivos esperados
- `reviews_limpias.parquet`
- `reviews_limpias_muestra.csv`

## Criterios de calidad
- Nombres claros y descriptivos
- Sin sufijos ambiguos como `final_v2` o `df_limpio_ok`
- Exportados desde el notebook de preparación
- Con variables documentadas en `07_CONTEXTO/01_RESUMEN_DEL_CASO.md`

## Schema esperado
| Variable | Tipo | Descripción breve |
|---|---|---|
| Id | int | Identificador técnico |
| ProductId | string | Producto |
| UserId | string | Usuario |
| Score | int | Calificación |
| Time | datetime | Fecha de reseña |
| Text | string | Texto de reseña |
| helpfulness_ratio | float | Proporción de utilidad |
| word_count | int | Número de palabras |
| review_length | int | Longitud del texto |
| sentence_count | int | Número de oraciones |
