import heapq

ESTADO_META = (1, 2, 3, 4, 5, 6, 7, 8, 0)
COORDENADAS_META = {peça: (i // 3, i % 3) for i, peça in enumerate(ESTADO_META)}

def calcular_distancia_manhattan(estado):
    distancia_total = 0
    for i, peça in enumerate(estado):
        if peça != 0:
            linha_atual, coluna_atual = i // 3, i % 3
            linha_meta, coluna_meta = COORDENADAS_META[peça]
            distancia_total += abs(linha_atual - linha_meta) + abs(coluna_atual - coluna_meta)
    return distancia_total

def obter_sucessores(estado):
    sucessores = []
    vazio = estado.index(0)
    linha, coluna = vazio // 3, vazio % 3
    acoes = {'Cima': (-1, 0), 'Baixo': (1, 0), 'Esquerda': (0, -1), 'Direita': (0, 1)}
    for acao, (dl, dc) in acoes.items():
        nova_l, nova_c = linha + dl, coluna + dc
        if 0 <= nova_l < 3 and 0 <= nova_c < 3:
            novo_vazio = nova_l * 3 + nova_c
            novo_estado = list(estado)
            novo_estado[vazio], novo_estado[novo_vazio] = novo_estado[novo_vazio], novo_estado[vazio]
            sucessores.append((tuple(novo_estado), acao))
    return sucessores

def resolver_A_estrela(estado_inicial):
    h_inicial = calcular_distancia_manhattan(estado_inicial)
    fila_prioridade = [(h_inicial, 0, estado_inicial, [])]
    visitados = set()

    while fila_prioridade:
        f, g, estado_atual, caminho = heapq.heappop(fila_prioridade)
        if estado_atual in visitados:
            continue
        if estado_atual == ESTADO_META:
            return caminho
        visitados.add(estado_atual)
        for proximo_estado, acao in obter_sucessores(estado_atual):
            if proximo_estado not in visitados:
                g_novo = g + 1
                h_novo = calcular_distancia_manhattan(proximo_estado)
                heapq.heappush(fila_prioridade, (g_novo + h_novo, g_novo, proximo_estado, caminho + [acao]))
    return None

if __name__ == "__main__":
    estado_inicial = (2, 8, 3, 1, 0, 4, 7, 6, 5)
    solucao = resolver_A_estrela(estado_inicial)
    print(f"Solução Ótima A* em {len(solucao)} movimentos: {solucao}")
