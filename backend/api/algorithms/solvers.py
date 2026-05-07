# api/algorithms/solvers.py
from .arbol import Nodo

def buscar_bfs(conexiones, inicio, fin):
    visitados = []
    frontera = [Nodo(inicio)]
    
    while frontera:
        nodo = frontera.pop(0)
        visitados.append(nodo)
        
        if nodo.get_datos() == fin:
            return nodo
        
        # IMPORTANTE: Obtener las ciudades vecinas del diccionario
        vecinos = conexiones.get(nodo.get_datos(), {})
        for ciudad in vecinos: # Itera sobre las llaves del dict
            hijo = Nodo(ciudad)
            hijo.set_padre(nodo)
            if not hijo.en_lista(visitados) and not hijo.en_lista(frontera):
                frontera.append(hijo)
    return None

def buscar_dfs(conexiones, inicio, fin):
    visitados = []
    frontera = [Nodo(inicio)]
    while frontera:
        nodo = frontera.pop()
        visitados.append(nodo)
        if nodo.get_datos() == fin: return nodo
        
        dato_nodo = nodo.get_datos()
        # Si no hay conexiones, asumimos lógica de Puzzle Lineal
        if conexiones is None:
            # Operadores de movimiento del puzzle
            ops = [
                [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]],
                [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]],
                [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            ]
            for op in ops:
                hijo = Nodo(op)
                hijo.set_padre(nodo)
                if not hijo.en_lista(visitados) and not hijo.en_lista(frontera):
                    frontera.append(hijo)
        elif dato_nodo in conexiones:
            for ciudad in conexiones[dato_nodo]:
                hijo = Nodo(ciudad)
                hijo.set_padre(nodo)
                if not hijo.en_lista(visitados) and not hijo.en_lista(frontera):
                    frontera.append(hijo)
    return None

def buscar_ucs(conexiones, inicio, fin):
    visitados = []
    nodo_ini = Nodo(inicio)
    nodo_ini.set_costo(0)
    frontera = [nodo_ini]
    while frontera:
        frontera.sort(key=lambda x: x.get_costo())
        nodo = frontera.pop(0)
        visitados.append(nodo)
        if nodo.get_datos() == fin: return nodo
        if conexiones and nodo.get_datos() in conexiones:
            for ciudad, costo in conexiones[nodo.get_datos()].items():
                hijo = Nodo(ciudad)
                hijo.set_costo(nodo.get_costo() + costo)
                hijo.set_padre(nodo)
                if not hijo.en_lista(visitados):
                    existente = next((n for n in frontera if n.igual(hijo)), None)
                    if existente:
                        if existente.get_costo() > hijo.get_costo():
                            frontera.remove(existente)
                            frontera.append(hijo)
                    else: frontera.append(hijo)
    return None