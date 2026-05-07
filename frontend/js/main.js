const API_BASE = 'http://127.0.0.1:8000/api/resolver/';

document.addEventListener('DOMContentLoaded', () => {
    cargarCiudades();
    document.getElementById('btn-calcular').addEventListener('click', calcularRuta);
});

async function cargarCiudades() {
    try {
        const response = await fetch(API_BASE);
        const data = await response.json();
        
        const selectInicio = document.getElementById('select-inicio');
        const selectFin = document.getElementById('select-fin');
        
        [selectInicio, selectFin].forEach(select => {
            select.innerHTML = '';
            data.ciudades.forEach(ciudad => {
                const option = document.createElement('option');
                option.value = ciudad;
                option.textContent = ciudad.charAt(0).toUpperCase() + ciudad.slice(1);
                select.appendChild(option);
            });
        });
    } catch (error) {
        console.error("Error al cargar ciudades:", error);
    }
}

// frontend/js/main.js
async function calcularTodo() {
    // Obtener valores y convertir el puzzle de "4,2,3,1" a [4, 2, 3, 1]
    const inicio_dfs = document.getElementById('in_dfs').value.split(',').map(Number);
    const meta_dfs = document.getElementById('target_dfs').value.split(',').map(Number);
    
    const payload = {
        inicio_dfs: inicio_dfs,
        meta_dfs: meta_dfs,
        inicio_bfs: document.getElementById('in_bfs').value.toLowerCase(),
        meta_bfs: document.getElementById('target_bfs').value.toLowerCase(),
        inicio_ucs: document.getElementById('in_ucs').value.toLowerCase(),
        meta_ucs: document.getElementById('target_ucs').value.toLowerCase()
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/api/resolver/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (data.status === 'success') {
            // Mostrar DFS
            const resDfs = document.getElementById('res_dfs');
            resDfs.innerHTML = data.dfs.map(paso => `<li>[${paso}]</li>`).join('');

            // Mostrar BFS
            const resBfs = document.getElementById('res_bfs');
            resBfs.innerHTML = data.bfs.map(paso => `<li>${paso}</li>`).join('');

            // Mostrar UCS
            const resUcs = document.getElementById('res_ucs');
            resUcs.innerHTML = data.ucs.camino.map(paso => `<li>${paso}</li>`).join('');
            
            const costDiv = document.getElementById('costo_ucs');
            costDiv.style.display = 'block';
            costDiv.innerHTML = `<strong>Costo Total:</strong> ${data.ucs.costo} km`;
        }
    } catch (error) {
        console.error("Error en la petición:", error);
        alert("No se pudo conectar con el servidor. Revisa la consola (F12).");
    }
}

function mostrarResultado(data) {
    const section = document.getElementById('result-section');
    const container = document.getElementById('path-display');
    const info = document.getElementById('meta-info');
    
    section.classList.remove('hidden');
    container.innerHTML = '';

    if (data.status === 'success') {
        data.camino.forEach((paso, index) => {
            const node = document.createElement('div');
            node.className = 'node';
            node.textContent = `${paso.ciudad.toUpperCase()}`;
            container.appendChild(node);

            if (index < data.camino.length - 1) {
                const arrow = document.createElement('span');
                arrow.className = 'arrow';
                arrow.textContent = '→';
                container.appendChild(arrow);
            }
        });

        const costoTotal = data.camino[data.camino.length - 1].costo;
        info.innerHTML = `<p><strong>Costo Total:</strong> ${costoTotal} km</p>`;
    } else {
        container.innerHTML = `<p style="color: red;">${data.message}</p>`;
        info.innerHTML = '';
    }
}