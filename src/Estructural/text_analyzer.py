import string

def analizar_texto(archivo):
    # """Analiza un archivo de texto y devuelve estadísticas."""
    try:
        with open(archivo, 'r', encoding="utf-8") as f:
            texto = f.read()
    except FileNotFoundError:
        print("El archivo no se encuentra en la ruta especificada.")
        return

    # Conteo de líneas
    conteo_lineas = texto.count('\n')
    if texto and not texto.endswith('\n'):
        conteo_lineas += 1

    # Conteo de caracteres
    conteo_caracteres = len(texto)

    # Conteo de palabras
    palabras = texto.split()
    conteo_palabras = len(palabras)

    # Procesar palabras (eliminar puntuación y pasar a minúsculas)
    words = [word.strip(string.punctuation).lower() for word in palabras if word.strip(string.punctuation)]
    
    # Conteo de palabras únicas
    conteo_palabras_unicas = len(set(words))

    # Retornar resultados como diccionario
    return {
        "Líneas": conteo_lineas,
        "Caracteres": conteo_caracteres,
        "Palabras": conteo_palabras,
        "Palabras únicas": conteo_palabras_unicas
    }

# Pedir archivo al usuario y analizarlo
archivo = input("Ingrese la ruta del archivo: ")
resultados = analizar_texto(archivo)

# Mostrar resultados si el archivo se encontró
if resultados:
    print("\nEstadísticas del archivo:")
    for clave, valor in resultados.items():
        print(f"{clave}: {valor}")
