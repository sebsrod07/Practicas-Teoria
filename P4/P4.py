import sys

def cargar_automata(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            lineas = [line.strip() for line in f if line.strip() and not line.strip().startswith('//')]
            
        alfabeto = lineas[0].split()
        num_estados = int(lineas[1])
        estados = lineas[2].split()
        estado_inicial = lineas[3]
        num_estados_finales = int(lineas[4])
        estados_finales = lineas[5].split()
        

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
            
        return alfabeto, estados, estado_inicial, estados_finales, transiciones
    
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo}'.")
        sys.exit(1)
    except Exception as e:
        print(f"Error al procesar el archivo: {e}")
        sys.exit(1)

def evaluar_cadena(cadena, alfabeto, estado_inicial, estados_finales, transiciones):
    estado_actual = estado_inicial
    for simbolo in cadena:
        if simbolo not in alfabeto:
            return False 
        if simbolo not in transiciones[estado_actual]:
            return False 
        estado_actual = transiciones[estado_actual][simbolo]
    
    return estado_actual in estados_finales

if __name__ == "__main__":
    print("=== EVALUADOR DE AUTÓMATAS FINITOS DETERMINISTAS ===")
    archivo = input("Ingresa el nombre del archivo del autómata (ej. L1.txt): ")
    
    alfabeto, estados, estado_inicial, estados_finales, transiciones = cargar_automata(archivo)
    print("\n¡Autómata cargado exitosamente!")
    
    while True:
        cadena = input("\nIngresa una cadena a evaluar (o 'salir' para terminar): ")
        if cadena.lower() == 'salir':
            break
            
        es_reconocida = evaluar_cadena(cadena, alfabeto, estado_inicial, estados_finales, transiciones)
        
        if es_reconocida:
            print(f"✅ La cadena '{cadena}' ES RECONOCIDA por el autómata.")
        else:
            print(f"❌ La cadena '{cadena}' NO ES RECONOCIDA por el autómata.")