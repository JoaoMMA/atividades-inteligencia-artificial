import heapq

def algoritmo_dijkstra(grafo, inicio, destino):
    fila_prioridade = [(0, inicio, [inicio])]
    visitados = set()

    while fila_prioridade:
        (custo, cidade_atual, caminho) = heapq.heappop(fila_prioridade)
        if cidade_atual in visitados:
            continue
        print(f"[Busca] Agente avaliando o estado atômico: '{cidade_atual}' | Custo acumulado: {custo} km")
        if cidade_atual == destino:
            return custo, caminho
        visitados.add(cidade_atual)
        for vizinho, distancia in grafo.get(cidade_atual, {}).items():
            if vizinho not in visitados:
                custo_total = custo + distancia
                heapq.heappush(fila_prioridade, (custo_total, vizinho, caminho + [vizinho]))
    return float("inf"), []

MAPA_CIDADES = {
    'Porto Alegre': {'Curitiba': 700, 'Sao Paulo': 1100},
    'Curitiba': {'Porto Alegre': 700, 'Sao Paulo': 400},
    'Sao Paulo': {'Curitiba': 400, 'Porto Alegre': 1100, 'Rio de Janeiro': 430, 'Brasilia': 1000},
    'Rio de Janeiro': {'Sao Paulo': 430, 'Belo Horizonte': 440, 'Salvador': 1600},
    'Belo Horizonte': {'Rio de Janeiro': 440, 'Brasilia': 740},
    'Brasilia': {'Sao Paulo': 1000, 'Belo Horizonte': 740, 'Belem': 2100},
    'Salvador': {'Rio de Janeiro': 1600, 'Recife': 800},
    'Recife': {'Salvador': 800, 'Belem': 2000},
    'Belem': {'Brasilia': 2100, 'Recife': 2000}
}

if __name__ == "__main__":
    cidade_inicio, cidade_fim = 'Porto Alegre', 'Belem'
    print("=== INICIANDO SIMULAÇÃO: AGENTE CAMINHO MÍNIMO (BUSCA ATÔMICA) ===")
    custo_final, rota_final = algoritmo_dijkstra(MAPA_CIDADES, cidade_inicio, cidade_fim)
    print(f"\nRota final: {' -> '.join(rota_final)} | Distância: {custo_final} km")
