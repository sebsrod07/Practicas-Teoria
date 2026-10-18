import urllib.request
import re

def obtener_html(url):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
        return html
    except Exception as e:
        print(f"no se puede acceder a  {url}")
        return ""

def extraer_datos(html):    
    patron_correos = r'[\w._%+-]+@[\w-]+\.[\w]{2,}'
    patron_links = r'href=["\'](https?://[^\s^"^\']+)["\']'
    patron_fechas = r'\b(?:\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[/-]\d{1,2}[/-]\d{1,2})\b'

    correos = re.findall(patron_correos, html)
    links = re.findall(patron_links, html)
    fechas = re.findall(patron_fechas, html)

    return correos, links, fechas

def main():
    urls = []
    print("Puedes introducir 10 URLS, presiona 0 para salir\nIntroduce direcciones URL: ")
    for i in range(10):
        url = input(f"URL {i+1}: ")
        if url == "0":
            break
        urls.append(url)

    correosTotales = []
    linksTotales = []
    fechasTotales = []

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

        correosTotales.extend(correos)
        linksTotales.extend(links)
        fechasTotales.extend(fechas)

    with open("correos.txt", "w", encoding="utf-8") as f:
        for correo in correosTotales:
            f.write(correo + "\n")

    with open("links.txt", "w", encoding="utf-8") as f:
        for link in set(linksTotales):
            f.write(link + "\n")

    with open("fechas.txt", "w", encoding="utf-8") as f:
        for fecha in set(fechasTotales):
            f.write(fecha + "\n")


if __name__ == "__main__":
    main()