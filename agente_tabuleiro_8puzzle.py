from collections import deque

ESTADO_META = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def exibir_tabuleiro(estado):
    for i in range(0, 9, 3):
        linha = [str(x) if x != 0 else " " for x in estado[i:i+3]]
        print(f"[ {linha[0]} | {linha[1]} | {linha[2]} ]")
    print("-" * 15)

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

def resolver_8_puzzle(estado_inicial):
    fila = deque([(estado_inicial, [])])
    visitados = set([estado_inicial])

    while fila:
        estado_atual, caminho = fila.popleft()
        if estado_atual == ESTADO_META:
            return caminho
        for proximo_estado, acao in obter_sucessores(estado_atual):
            if proximo_estado not in visitados:
                visitados.add(proximo_estado)
                fila.append((proximo_estado, caminho + [acao]))
    return None

if __name__ == "__main__":
    estado_inicial = (1, 2, 3, 4, 0, 6, 7, 5, 8)
    solucao = resolver_8_puzzle(estado_inicial)
    print(f"Resolvido em {len(solucao)} passos! Sequência de ações: {solucao}")
