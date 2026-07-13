"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]
    """
    conteo_meses = {}
    with open('data.csv', 'r') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea:
                continue
            columnas = linea.split(',')
            fecha = columnas[2]      # columna 3 (índice 2)
            mes = fecha.split('-')[1]  # obtenemos el mes (dos dígitos)
            conteo_meses[mes] = conteo_meses.get(mes, 0) + 1

    # Ordenamos por mes (numéricamente, pero como son strings de 2 dígitos, sorted funciona)
    resultado = sorted(conteo_meses.items(), key=lambda x: int(x[0]))
    return resultado