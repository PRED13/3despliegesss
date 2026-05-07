# Puzzle Lineal con Busqueda en Profundidad 

from arbol import Nodo
def buscar_solucion_DFS(estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodos_inicial = Nodo(estado_inicial)
    nodos_frontera.append(nodos_inicial)
    while (not solucionado) and len(nodos_frontera) !=0:
        nodo = nodos_frontera.pop()
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodo)
        if nodo.get_datos() == solucion:
            #solucion encontrada
            solucion = False
            return nodo
        else:
            # Expandir nodos Hijos
            dato_nodo = nodo.get_datos()


            #Operador Izquierdo
            hijo=[dato_nodo[1], dato_nodo[0], dato_nodo[2],dato_nodo[3]]
            hijo_izquierdo = Nodo(hijo)
            if not hijo_izquierdo.en_lista(nodos_visitados)\
                and not hijo_izquierdo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_izquierdo)

            #Operador derecho
            hijo=[dato_nodo[0], dato_nodo[2], dato_nodo[1],dato_nodo[3]]
            hijo_derecho = Nodo(hijo)
            if not hijo_derecho.en_lista(nodos_visitados)\
                and not hijo_derecho.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_derecho)
            
            #Operador central
            hijo=[dato_nodo[0], dato_nodo[1], dato_nodo[3],dato_nodo[2]]
            hijo_central = Nodo(hijo)
            if not hijo_central.en_lista(nodos_visitados)\
                and not hijo_central.en_lista(nodos_frontera):
                nodos_frontera.append(hijo_central)
            
            nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])
if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)

    # Mostrar el resultado correctamente
    resultado = []
    nodo = nodo_solucion
    
    # Recorremos desde el nodo solución hacia el padre hasta llegar al inicio
    while nodo is not None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    
    # Invertimos la lista una sola vez para que vaya de inicio a fin
    resultado.reverse()
    #imprimir de forma ordenada
    for resul in resultado:
        print(resul)
    #print(resultado)