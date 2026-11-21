import sys
def cargaAutomata(archivo):
    with open(archivo, 'r', encoding='utf-8') as f:
        lineas = [line.strip() for line in f if line.strip() and not line.strip().startswith('//')]
        
    alfabeto = lineas[0].split()
    numEstados = int(lineas[1])
    estados = lineas[2].split()
    estadoInicial = lineas[3]
    numEstadosF = int(lineas[4])
    estadosF = lineas[5].split()

    transiciones={}
    for estado in estados:
        transiciones[estado]={}
    
    estadoI=0
    for linea in lineas[6:]:
        simbolo=0
        partes = linea.split()
        for destino in partes:
            transiciones[estados[estadoI]][alfabeto[simbolo]]=destino
            simbolo+=1
        estadoI+=1  
    return alfabeto, estados, estadoInicial, estadosF, transiciones

def validaCadena(cadena, alfabeto, estadoI, estadosF, transiciones):
    estadoA = estadoI
    for simbolo in cadena:
        if simbolo not in alfabeto:
            return False 
        if simbolo not in transiciones[estadoA]:
            return False 
        estadoA = transiciones[estadoA][simbolo]
    
    return estadoA in estadosF

#### M A I N F
print("AFN")
archivo = input("Ingresa el archivo del automata: ")

alfabeto, estados, estadoI, estadosF, transiciones = cargaAutomata(archivo)
print("\nAutomata generado")

while True:
    cadena = input("\nIngresa una cadena a evaluar o 0 para terminar: ")
    if cadena.lower() == '0':
        break
        
    valida = validaCadena(cadena, alfabeto, estadoI, estadosF, transiciones)
    
    if valida:
        print(f"La cadena '{cadena}' es Aceptada")
    else:
        print(f"La cadena '{cadena}' NO es aceptada")