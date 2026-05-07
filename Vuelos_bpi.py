#vuelos con busqueda con profundidad iterativa
from arbol import Nodo

def DFS_profundidad_iterativa(nodo, solucion):
    for limite in range(0, 100):
        visitados = []#= set()
        sol = buscar_solucion_DFS_REC(nodo, solucion, visitados, limite)
        if sol != None:
            return sol
        
def buscar_solucion_DFS_REC(nodo, solucion, visitados, limite):
    if limite > 0:
        visitados.append(nodo)
        if nodo.get_datos() == solucion:
            return nodo
        else:
            #espandir nodos hijo (ciudades con conexion)
            dato_nodo = nodo.get_datos()
            lista_hijos = []
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                if not hijo.en_lista(visitados):
                    lista_hijos.append(hijo)
            nodo.set_hijos(lista_hijos)
            for nodo_hijo in nodo.get_hijos():
                if not nodo_hijo.get_datos() in visitados:
                    #llamada recursiva
                    sol = buscar_solucion_DFS_REC(nodo_hijo, solucion, visitados, limite-1)
                    if sol != None:
                        return sol
        return None
if __name__ == "__main__":
    conexiones = {
        "jiloyork": ["celaya", "cdmx", "queretaro"],
        "sonora": ["zacatecas", "sinaloa"],
        "guanajuato": ["aguas_calientes"],
        "oaxaca": ["queretaro"],
        "sinaloa": ["celaya", "sonora", "jiloyork"],
        "queretaro": ["tamaulipas", "oaxaca", "sinaloa", "jiloyork", "monterrey"],
        "celaya": ["jiloyork", "sinaloa"],
        "zacatecas": ["sonora", "monterrey", "queretaro"],
        "monterrey": ["zacatecas", "sinaloa"],
        "tamaulipas": ["queretaro"],
        "cdmx": ["jiloyork"]
    }
    
    estado_inicial = "jiloyork"
    solucion = "oaxaca"
    nodo_inicial = Nodo(estado_inicial)
    nodo = DFS_profundidad_iterativa(nodo_inicial, solucion)
    #mostrar resultado
    if Nodo != None:
        resultado = []
        while nodo.get_padre() != None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.append(estado_inicial)
        resultado.reverse()
        print(resultado)
    
    else:
        print("solucion no encontrada")