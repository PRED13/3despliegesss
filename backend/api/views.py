# api/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .algorithms.solvers import buscar_bfs, buscar_dfs, buscar_ucs

# api/views.py

CONEXIONES = {
    "jiloyork": {"cdmx": 125, "queretaro": 513, "celaya": 150},
    "cdmx": {"jiloyork": 125, "queretaro": 423, "hgo": 491},
    "queretaro": {"slp": 203, "jiloyork": 513, "cdmx": 423, "hgo": 356, "ags": 599, "tamaulipas": 200, "oaxaca": 300, "monterrey": 600},
    "hgo": {"cdmx": 491, "queretaro": 356, "mexicali": 309, "monterrey": 346},
    "slp": {"ags": 390, "queretaro": 203},
    "ags": {"slp": 390, "queretaro": 599},
    "sonora": {"zacatecas": 250, "sinaloa": 394},
    "mexicali": {"hgo": 309, "queretaro": 313, "monterrey": 296},
    "monterrey": {"hgo": 346, "mexicali": 296, "zacatecas": 300},
    "zacatecas": {"sonora": 250, "monterrey": 300, "queretaro": 350},
    "celaya": {"jiloyork": 150, "sinaloa": 400},
    "sinaloa": {"celaya": 400, "sonora": 394, "jiloyork": 600},
    "oaxaca": {"queretaro": 300},
    "tamaulipas": {"queretaro": 200}
}
@csrf_exempt
def resolver_todas_las_rutas(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Procesar Puzzle (DFS)
            res_dfs = buscar_dfs(None, data['inicio_dfs'], data['meta_dfs'])
            
            # Procesar Vuelos (BFS)
            res_bfs = buscar_bfs(CONEXIONES, data['inicio_bfs'].lower(), data['meta_bfs'].lower())
            
            # Procesar Carretera (UCS)
            res_ucs = buscar_ucs(CONEXIONES, data['inicio_ucs'].lower(), data['meta_ucs'].lower())

            def obtener_ruta(nodo):
                r = []
                while nodo:
                    r.append(nodo.get_datos())
                    nodo = nodo.get_padre()
                return r[::-1]

            return JsonResponse({
                "status": "success",
                "dfs": obtener_ruta(res_dfs),
                "bfs": obtener_ruta(res_bfs),
                "ucs": {
                    "camino": obtener_ruta(res_ucs),
                    "costo": res_ucs.get_costo() if res_ucs else 0
                }
            })
        except Exception as e:
            # Esto imprimirá el error real en tu terminal de Django
            print(f"ERROR INTERNO: {e}") 
            return JsonResponse({"status": "error", "message": str(e)}, status=500)