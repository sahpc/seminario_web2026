# Plan de Preparación de Datos

## 1. Objetivo
Preparar el dataset de reseñas de Amazon para análisis exploratorio y modelado, asegurando calidad, consistencia, trazabilidad y reproducibilidad.

## 2. Fuente de datos
- Origen: Amazon Fine Food Reviews
- Ubicación esperada del archivo crudo: `00_datos_crudos/`
- Salida del archivo limpio: `01_datos_procesados/`

## 3. Pasos de limpieza en orden

### 3.1 Carga inicial
- Leer el archivo crudo desde `00_datos_crudos/`
- Verificar dimensiones, nombres de columnas y tipos iniciales

### 3.2 Revisión de calidad
- Identificar nulos por columna
- Identificar duplicados
- Revisar valores imposibles o inconsistentes
- Revisar distribución de variables clave

### 3.3 Manejo de nulos
- `Text`: no se permiten nulos; si existen, se eliminan
- `Score`: no se permiten nulos; si existen, se eliminan
- `Summary`: se conserva y se documenta el porcentaje de nulos
- `ProfileName`: se conserva salvo que el análisis posterior demuestre lo contrario

**Justificación:** las columnas esenciales para el problema deben estar completas.

### 3.4 Manejo de duplicados
- Eliminar duplicados exactos de fila
- Documentar cuántas filas se removieron

**Justificación:** evita sobre-representación de observaciones.

### 3.5 Tipos de datos
- Convertir `Time` de timestamp a fecha
- Revisar que variables numéricas estén en formato numérico
- Revisar campos de texto en formato string

### 3.6 Variable objetivo
Crear:
```python
helpfulness_ratio = HelpfulnessNumerator / HelpfulnessDenominator
