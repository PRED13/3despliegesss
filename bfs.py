from arbol import Nodo

def buscar_solucion_BFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodos_inicial = Nodo(estado_inicial) 
    nodos_frontera.append(nodos_inicial)
    
    while (not solucionado) and len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)
        
        if nodo.get_datos() == solucion:
            solucionado = True
            return nodo
        else:
            dato_nodo = nodo.get_datos()
            
            # Operador izquierdo
            hijo_izq_datos = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo_izq_datos)
            hijo_izquierdo.set_padre(nodo) # IMPORTANTE: Asignar padre
            
            if not hijo_izquierdo.en_lista(nodos_visitados) and not hijo_izquierdo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo)
            
            # Operador central
            hijo_cen_datos = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = Nodo(hijo_cen_datos)
            hijo_central.set_padre(nodo) 
            
            if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)
                
            # Operador derecho 
            hijo_der_datos = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_derecho = Nodo(hijo_der_datos)
            hijo_derecho.set_padre(nodo) 
            
            if not hijo_derecho.en_lista(nodos_visitados) and not hijo_derecho.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecho)
                
            nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])

if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)
    
    # Mostrar el resultado
    if nodo_solucion is not None:
        resultado = []
        nodo = nodo_solucion
        while nodo.get_padre() is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print("Camino encontrado:")
        for paso in resultado:
            print(paso)
    else:
        print("No se encontró solución.")