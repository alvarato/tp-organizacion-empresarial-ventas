# Trabajo Práctico: Gestión Colaborativa, Control de Versiones y Organización Empresarial (Git, GitHub y Jira)

**Alumno:** Alvaro Bernabey Izquierdo
**Comisión:** 14

## Información del Proyecto

- **Institución:** Universidad Tecnológica Nacional (UTN)
- **Carrera:** Tecnicatura Universitaria en Programación (TUP) - Modalidad a Distancia
- **Cátedra:** Organización Empresarial (Año Lectivo 2026)
- **Célula Ágile / Equipo:** \* Hugo (P1) - Líder y Organizador
  - Paco (P2) - Desarrollador Técnico
  - Luis (P3) - Revisor y QA

---

## 1. Escenario Elegido

- Análisis de Ventas de una Tienda.

---

## 2. Descripción del Dataset Utilizado

El conjunto de datos utilizado para este análisis se encuentra almacenado de forma local dentro del repositorio en la carpeta `/datos`.

- **Nombre del archivo:** `datos_analisis.csv`
- **Volumen:** Tamaño moderado para optimizar la velocidad de clonación y el rendimiento del entorno.
- **Campos principales:**
  - `ID_Venta`: Identificador Único de la transacción.
  - `Fecha`: Fecha en que se realizó la venta.
  - `Categoría`: Variable cuantitativa base del análisis estadístico y segmentación cualitativa para agrupar los resultados.
  - `Producto`: Descripción del artículo vendido.
  - `Precio_Unitario`: Costo por unidad del producto.
  - `Cantidad`: Volumen de unidades adquiridas.

---

## 3. Estructura del Repositorio

Siguiendo los lineamientos de gobernanza establecidos por la cátedra, el proyecto cuenta con la siguiente arquitectura de directorios:

```text
├── datos/          # Contiene los archivos de datos utilizados en el análisis (CSV/Excel).
├── scripts/        # Contiene los programas o scripts desarrollados en Python o R.
├── resultados/     # Almacena los resultados generados (gráficos, tablas exportadas).
├── .gitignore      # Exclusión de archivos basura de Python, caché y checkpoints.
└── README.md       # Documentación principal del proyecto (este archivo).
```
