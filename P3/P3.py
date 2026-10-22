import urllib.request
import re

def requestURLIB(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36 OPR/137.0.0.0'})
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    return html

def obtenerDatos(html):    
    expresionCorreos = r'[\w._%+-][\w._%+-]+@[\w-]+\.[\w]{2,}'
    expresionLinks = r'href=["\'](https?://[^\s"\']+)["\']'
    expresionFechas = r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}[/-]\d{1,2}[/-]\d{1,2}\b'

    correos = re.findall(expresionCorreos, html)
    links = re.findall(expresionLinks, html)
    fechas = re.findall(expresionFechas, html)

    return correos, links, fechas


# - - - - - MAIN - - - - - 
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

print("\nObteniendo datos de las URLS \n")
for url in urls:
    html = requestURLIB(url)
    if html=="":
        continue
        
    correos, links, fechas = obtenerDatos(html)
    
    print(f"\nResultados para {url}:")
    print(f"Correos encontrados: {len(correos)}")
    print(f"Links encontrados: {len(links)}")
    print(f"Fechas encontradas: {len(fechas)}")

    correosTotales.extend(correos)
    linksTotales.extend(links)
    fechasTotales.extend(fechas)

with open("correos.txt", "w", encoding="utf-8") as f:
    for correo in correosTotales:
        f.write(correo + "\n")

with open("links.txt", "w", encoding="utf-8") as f:
    for link in linksTotales:
        f.write(link + "\n")

with open("fechas.txt", "w", encoding="utf-8") as f:
    for fecha in fechasTotales:
        f.write(fecha + "\n")
print("Todos losdatos se escribieron en TXT")
