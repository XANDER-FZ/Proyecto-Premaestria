# Sistema de Procesamiento y Validación de Datos de Estudiantes

## Descripción

Este proyecto implementa un sistema en Python para la carga, validación, análisis y exportación de datos de estudiantes almacenados en archivos CSV.

El sistema permite:

- Validar y limpiar datos de estudiantes.
- Filtrar estudiantes por edad o promedio.
- Ordenar registros según distintos criterios.
- Calcular estadísticas básicas.
- Exportar resultados en formato JSON.
- Ejecutar pruebas unitarias para validar la lógica del sistema.

---

# Estructura del proyecto

```text
Proyecto-Premaestria/
│
├── tests/
│   └── test_processor.py
│
├── CLI.py
├── data_loader.py
├── exporter.py
├── main.py
├── processor.py
├── utils.py
│
├── .gitignore
└── README.md
```
---

# Descripción de los módulos

### main.py
Archivo principal que inicia el programa y ejecuta la interfaz de línea de comandos.

### CLI.py
Implementa la interfaz de usuario por consola que permite:

- Mostrar datos
- Filtrar estudiantes
- Ordenar registros
- Calcular estadísticas
- Exportar resultados

### data_loader.py
Encargado de:

- Leer archivos CSV
- Convertir tipos de datos
- Aplicar validaciones
- Construir el dataset final

### processor.py
Contiene funciones de **validación de datos**, como:

- Validación de extensión de archivo
- Validación de edad
- Validación de promedio
- Validación de nombre

### utils.py
Incluye funciones de procesamiento de datos:

- Filtrar por edad
- Filtrar por promedio
- Ordenar estudiantes
- Calcular promedio general
- Calcular edad mínima y máxima
- Contar estudiantes por carrera

### exporter.py
Permite exportar resultados del análisis a **archivos JSON**.

### tests/test_processor.py
Contiene **pruebas unitarias con pytest** para verificar el correcto funcionamiento de las funciones de validación.

---

# Funcionalidades principales

El sistema permite realizar las siguientes operaciones:

### 1. Cargar datos desde CSV
Se leen los datos de estudiantes y se validan los campos.

### 2. Validar información
Se verifican condiciones como:

- Edad positiva
- Promedio entre 0 y 10
- Nombre no vacío
- Archivo con extensión `.csv`

### 3. Filtrar estudiantes

Ejemplos:

- Estudiantes con edad mayor o igual a un valor.
- Estudiantes con promedio mayor o igual a un valor.

### 4. Ordenar datos

Se pueden ordenar registros por diferentes criterios como:

- edad
- promedio
- nombre

### 5. Calcular estadísticas

El sistema calcula:

- promedio general
- edad mínima
- edad máxima
- cantidad de estudiantes por carrera

### 6. Exportar resultados

Los resultados pueden exportarse a archivos **JSON**.

---

# Ejecución del programa

Para ejecutar el sistema:

```bash
python main.py
```

---
# Autor
Alexander Fabian Zeña Cornejo


