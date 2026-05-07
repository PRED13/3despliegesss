from arbol import Nodo

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    
    # Creamos el nodo inicial
    nodo_inicial = Nodo(estado_inicial)
    nodo_inicial.set_costo(0)
    nodos_frontera.append(nodo_inicial)
    
    while (not solucionado) and len(nodos_frontera) != 0:
        # Ordenar la frontera por costo acumulado (UCS)
        nodos_frontera.sort(key=lambda x: x.get_costo())
        
        # Extraer el nodo con menor costo
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)
        
        # Comprobar si es la meta
        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        else:
            # Expandir nodos hijos
            dato_nodo = nodo.get_datos()
            lista_hijos = [] 
            
            # Revisar las conexiones de la ciudad actual
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                costo_arista = conexiones[dato_nodo][un_hijo]
                # El costo total es el costo del padre + el de la arista
                hijo.set_costo(nodo.get_costo() + costo_arista)
                hijo.set_padre(nodo)
                lista_hijos.append(hijo)
                
                # Regla de exploración:
                if not hijo.en_lista(nodos_visitados):
                    if hijo.en_lista(nodos_frontera):
                        # Si ya está en la frontera, comparamos costos
                        for n in nodos_frontera:
                            if n.igual(hijo) and n.get_costo() > hijo.get_costo():
                                nodos_frontera.remove(n)
                                nodos_frontera.append(hijo)
                                break
                    else:
                        nodos_frontera.append(hijo)
            
            nodo.set_hijos(lista_hijos)
    return None

if __name__ == "__main__":
    conexiones = {
        "Jiloyork": {"CDMX": 125, "QRO": 513},
        "MORELOS": {"QRO": 524},
        "CDMX": {"Jiloyork": 125, "QRO": 423, "HGO": 491},
        "HGO": {"CDMX": 491, "QRO": 356, "MEXICALI": 309, "MONTERREY": 346},
        "QRO": {"SLP": 203, "MORELOS": 514, "Jiloyork": 513, "CDMX": 423, "MTY": 603, 
                "SONORA": 437, "HGO": 356, "MEXICALI": 313, "AGS": 599},
        "SLP": {"AGS": 390, "QRO": 203},
        "AGS": {"SLP": 390, "QRO": 599},
        "SONORA": {"QRO": 437, "MEXICALI": 394},
        "MEXICALI": {"MTY": 296, "HGO": 309, "QRO": 313},
        "MTY": {"MEXICALI": 296, "QRO": 603, "HGO": 346},
        "MONTERREY": {"HGO": 346} 
    }
    
    estado_inicial = "Jiloyork"
    solucion = "AGS"
    
    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)
    
    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None:
            resultado.append(f"{nodo.get_datos()} ({nodo.get_costo()} km)")
            nodo = nodo.get_padre()
        
        resultado.reverse()
        print(" -> ".join(resultado))
    else:
        print("No se encontró una solución.")