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
            transiciones[estados[estadoI]][alfabeto[simbolo]]=destino.split(',')
            simbolo+=1
        estadoI+=1  
    return alfabeto, estados, estadoInicial, estadosF, transiciones

def cerraduraEpsilon(transiciones, estados):
    CE = []
    pila = []
    for estado in estados:
        if estado not in CE:
            CE.append(estado)
            pila.append(estado)
            
    while pila:
        edoActual = pila.pop()
        if transiciones[edoActual]['eps'] == ['-']:
            continue
        for edo in transiciones[edoActual]['eps']:
            if edo not in CE:
                CE.append(edo)
                pila.append(edo)
    return CE

def moverA(transiciones, estados, simbolo):
    MA=[]
    for estado in estados:
        if transiciones[estado][simbolo] == ['-']:
            continue
        for edo in transiciones[estado][simbolo]:
            if edo in MA:
                continue
            MA.append(edo)
    return MA
def irA(simbolo, estados, transiciones):
    return cerraduraEpsilon(transiciones, moverA(transiciones,estados,simbolo))

def obtenerAFD():
    archivo =input("Ingresa el archivo del automata: ")
    alfabeto,estados, EInit, estadosF, transiciones = cargaAutomata(archivo)
    # print(moverA(transiciones, ['q0', 'q1','q7'],'a'))
    edosAFD=[cerraduraEpsilon(transiciones, [EInit])]
    
    for edo in edosAFD:
        edosResultantes=[]
        for simbolo in alfabeto:
            if simbolo =='eps':
                continue
            edosResultantes.append(irA(simbolo,edo,transiciones))
        for edoSS in edosResultantes:
            if edoSS in edosAFD:
                continue
            edosAFD.append(edoSS)
    edosFinalesAFN=[]
    for edo in edosAFD:
        if set(estadosF).issubset(edo):
            edosFinalesAFN.append(edo)
    transicionesAFN={}
    for edo in edosAFD:
        if edo!=[]:
            transicionesAFN[tuple(edo)]={}
    for edo in edosAFD:
        if edo==[]:
            continue
        for simbolo in alfabeto:
            if simbolo=='eps':
                continue
            transicionesAFN[tuple(edo)][simbolo]=irA(simbolo,edo,transiciones)
    edoInicialAFN=cerraduraEpsilon(transiciones, [EInit])
    return alfabeto, edosAFD,edosFinalesAFN, transicionesAFN, edoInicialAFN
def mapeoAFD(alfabetoAFN, transicionesAFN, edosFinalesAFN,edosAFN, edoInicialAFN):
    alfabetoAFD=list.copy(alfabetoAFN)
    alfabetoAFD.pop()
    # Alfabeto AFD CHECK    
    diccionarioEdosAFD={}
    i='A'
    for estado in edosAFN:
        if estado != []:
            diccionarioEdosAFD[tuple(estado)]=i
            i = chr(ord(i) + 1)
    #Declaracion del diccionario para mapeo CHECK
    edosAFD=[]
    for edo in edosAFN:
        if edo != []:
            edosAFD.append(diccionarioEdosAFD[tuple(edo)])
    # Edos AFD guardados en forma A, B, C CHECK
    edosFinalesAFD=[]
    for edo in edosFinalesAFN:
        edosFinalesAFD.append(diccionarioEdosAFD[tuple(edo)])
    # Edos Finales guardados en forma A, B, C CHECK
    transicionesAFD={}
    for estado in edosAFD:
        transicionesAFD[estado]={}
    for estado in edosAFN:
        if estado==[]:
            continue
        for simbolo in alfabetoAFN:
            if simbolo =='eps':
                continue
            if transicionesAFN[tuple(estado)][simbolo] == []:
                transicionesAFD[diccionarioEdosAFD[tuple(estado)]][simbolo]='λ'
                continue
            transicionesAFD[diccionarioEdosAFD[tuple(estado)]][simbolo]=diccionarioEdosAFD[tuple(transicionesAFN[tuple(estado)][simbolo])]
    return alfabetoAFD,edosAFD, edosFinalesAFD, transicionesAFD, diccionarioEdosAFD[tuple(edoInicialAFN)]


# # # # # # M A I N # # # # # # 
alfabetoAFN, edosAFN, edosFinalesAFN, transicionesAFN, edoInicialAFN = obtenerAFD()
alfabetoAFD, edosAFD, edosFinalesAFD, transicionesAFD, edoInicialAFD = mapeoAFD(alfabetoAFN, transicionesAFN, edosFinalesAFN, edosAFN, edoInicialAFN)

print("\n" + " - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print("           QUINTUPLA DEL AFD")
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
print(f"1. Conjunto de Estados: {edosAFD}")
print(f"2. Alfabeto:            {alfabetoAFD}")
print(f"3. Estado Inicial:     {edoInicialAFD}")
print(f"4. Estados Finales:     {edosFinalesAFD}")
print("5. Tabla de Transiciones:\n")

encabezado = f"  {'Estado'}\t" + "\t".join(f"{simbolo}" for simbolo in alfabetoAFD)
print(encabezado)
print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

for estado in edosAFD:
    fila=f"\t{estado}\t"
    for simbolo in alfabetoAFD:
        destino = transicionesAFD[estado][simbolo]
        fila += f"{destino}\t"
    print(fila)

print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - -")