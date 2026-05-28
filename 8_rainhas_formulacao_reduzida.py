import random

def avaliar_conflitos(estado):
    conflitos = 0
    n = len(estado)
    for i in range(n):
        for j in range(i + 1, n):
            if estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j):
                conflitos += 1
    return conflitos

def obter_vizinhos_reduzidos(estado):
    vizinhos = []
    n = len(estado)
    for col in range(n):
        linha_atual = estado[col]
        for nova_linha in range(n):
            if nova_linha != linha_atual:
                novo_estado = list(estado)
                novo_estado[col] = nova_linha
                vizinhos.append(novo_estado)
    return vizinhos

def hill_climbing_reduzido():
    tentativa = 0
    while True:
        tentativa += 1
        estado_atual = [random.randint(0, 7) for _ in range(8)]
        custo_atual = avaliar_conflitos(estado_atual)
        while True:
            vizinhos = obter_vizinhos_reduzidos(estado_atual)
            if not vizinhos: break
            melhor_vizinho = min(vizinhos, key=avaliar_conflitos)
            melhor_custo = avaliar_conflitos(melhor_vizinho)
            if melhor_custo >= custo_atual: break
            estado_atual = melhor_vizinho
            custo_atual = melhor_custo
        if custo_atual == 0:
            return estado_atual

if __name__ == "__main__":
    solucao = hill_climbing_reduzido()
    print(f"Solução na Formulação Reduzida encontrada: {solucao}")
