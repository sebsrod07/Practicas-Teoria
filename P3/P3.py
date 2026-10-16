import urllib.request
import re

def obtener_html(url):
    try:
        # Se añade un User-Agent para evitar bloqueos básicos de algunas páginas
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
        return html
    except Exception as e:
        print(f"Error al acceder a {url}: {e}")
        return ""

def extraer_datos(html):
    # Patrones de expresiones regulares
    patron_correos = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    patron_links = r'href=["\'](https?://[^\s^"^\']+)["\']'
    patron_fechas = r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[/-]\d{1,2}[/-]\d{1,2})\b'

    correos = re.findall(patron_correos, html)
    links = re.findall(patron_links, html)
    fechas = re.findall(patron_fechas, html)

    return correos, links, fechas

def main():
    urls = []
    print("Introduce tres direcciones URL (ej. https://www.ejemplo.com):")
    for i in range(3):
        url = input(f"URL {i+1}: ")
        urls.append(url)

    todos_correos = []
    todos_links = []
    todas_fechas = []

    print("\n--- Procesando URLs ---")
    for url in urls:
        html = obtener_html(url)
        if not html:
            continue
            
        correos, links, fechas = extraer_datos(html)
        
        print(f"\nResultados para {url}:")
        print(f" - Correos encontrados: {len(correos)}")
        print(f" - Links encontrados: {len(links)}")
        print(f" - Fechas encontradas: {len(fechas)}")

        todos_correos.extend(correos)
        todos_links.extend(links)
        todas_fechas.extend(fechas)

    # Generación de archivos de salida
    with open("salida_correos.txt", "w", encoding="utf-8") as f:
        f.write("--- Correos Electrónicos Encontrados ---\n")
        for correo in set(todos_correos): # set() para evitar duplicados
            f.write(correo + "\n")

    with open("salida_links.txt", "w", encoding="utf-8") as f:
        f.write("--- Links Encontrados ---\n")
        for link in set(todos_links):
            f.write(link + "\n")

    with open("salida_fechas.txt", "w", encoding="utf-8") as f:
        f.write("--- Fechas Encontradas ---\n")
        for fecha in set(todas_fechas):
            f.write(fecha + "\n")

    print("\nProceso finalizado. Los archivos 'salida_correos.txt', 'salida_links.txt' y 'salida_fechas.txt' han sido generados exitosamente.")

if __name__ == "__main__":
    main()