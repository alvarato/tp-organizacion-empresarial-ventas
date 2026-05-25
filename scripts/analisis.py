import os
from datetime import datetime


def generar_reporte_ventas():
    # 1. Obtener la fecha y hora actual en el formato deseado (dia-mes-año_hora-minuto)
    # Usamos guiones en lugar de barras '/' porque el sistema operativo no permite barras en los nombres de archivos.
    fecha_hora_actual = datetime.now().strftime("%d-%m-%Y_%H-%M")

    # 2. Armar el nombre del archivo dinámicamente con la fecha y hora
    nombre_archivo = f"{fecha_hora_actual}_reporte.txt"

    # 3. Definir las rutas relativas utilizando el nuevo nombre dinámico
    ruta_datos = os.path.join("..", "datos", "datos_analisis.csv")
    ruta_reporte = os.path.join("..", "resultados", nombre_archivo)

    print(f"Iniciando análisis estadístico de ventas...")
    print(f"El archivo se guardará como: {nombre_archivo}")

    # ... (El resto del código de lectura y cálculos sigue exactamente igual)

    total_dinero = 0.0
    total_unidades = 0
    conteo_productos = {}

    # Leer el archivo CSV línea por línea usando Python Puro
    with open(ruta_datos, "r", encoding="utf-8") as f:
        lineas = f.readlines()

        # Omitimos la primera línea que contiene los encabezados
        if len(lineas) <= 1:
            print("Error: El archivo CSV está vacío o solo contiene la cabecera.")
            return

        for linea in lineas[1:]:
            linea = linea.strip()
            if not linea:
                continue

            # Separar los campos por la coma (CSV)
            columnas = linea.split(",")

            # Mapeo de columnas según el CSV:
            # Producto (posición 3), Precio_Unitario (posición 4), Cantidad (posición 5)
            producto = columnas[3]
            precio_unitario = float(columnas[4])
            cantidad = int(columnas[5])

            # Cálculos solicitados por la cátedra
            total_venta = precio_unitario * cantidad
            total_dinero += total_venta
            total_unidades += cantidad

            # Guardar el conteo en un diccionario para sacar el producto más vendido
            if producto in conteo_productos:
                conteo_productos[producto] += cantidad
            else:
                conteo_productos[producto] = cantidad

    # Encontrar el producto con más unidades vendidas buscando el máximo en el diccionario
    producto_mas_vendido = max(conteo_productos, key=conteo_productos.get)
    unidades_mas_vendidas = conteo_productos[producto_mas_vendido]

    # Estructurar el cuerpo del reporte técnico
    reporte_contenido = f"""==================================================
        REPORTE DE VENTAS SEMANAL (QA)
--------------------------------------------------
Fecha de generación: 25/05/2026
Origen de datos: datos/datos_analisis.csv
Análisis correspondiente a: Célula de Trabajo UTN

--------------------------------------------------
METRICAS PRINCIPALES:
--------------------------------------------------
1. Total de dinero ingresado:
   $ {total_dinero:,.2f}

2. Total de unidades vendidas:
   {total_unidades} unidades

3. Producto más vendido de la semana:
   "{producto_mas_vendido}" ({unidades_mas_vendidas} unidades vendidas)

--------------------------------------------------
==================================================="""

    # Asegurar que la carpeta 'resultados' exista antes de escribir el archivo
    os.makedirs(os.path.dirname(ruta_reporte), exist_ok=True)

    # Guardar el reporte en formato de texto plano (.txt)
    with open(ruta_reporte, "w", encoding="utf-8") as f:
        f.write(reporte_contenido)

    print(f"¡Análisis completo! El archivo se guardó con éxito en: {ruta_reporte}")


if __name__ == "__main__":
    generar_reporte_ventas()
