import math
import random

CIDADES = {
    'A': (10, 20), 'B': (30, 80), 'C': (20, 40), 'D': (80, 10),
    'E': (90, 50), 'F': (50, 50), 'G': (10, 90), 'H': (60, 20)
}

def calcular_distancia_entre(c1, c2):
    return math.sqrt((CIDADES[c1][0] - CIDADES[c2][0])**2 + (CIDADES[c1][1] - CIDADES[c2][1])**2)

def calcular_custo_rota(rota):
    distancia = 0
    for i in range(len(rota)):
        distancia += calcular_distancia_entre(rota[i], rota[(i + 1) % len(rota)])
    return distancia

def obter_vizinhos_permutacao(rota):
    vizinhos = []
    for i in range(len(rota)):
        for j in range(i + 1, len(rota)):
            nova_rota = list(rota)
            nova_rota[i], nova_rota[j] = nova_rota[j], nova_rota[i]
            vizinhos.append(nova_rota)
    return vizinhos

def resolver_caixeiro_viajante():
    lista_cidades = list(CIDADES.keys())
    random.shuffle(lista_cidades)
    rota_atual = lista_cidades
    custo_atual = calcular_custo_rota(rota_atual)
    
    while True:
        vizinhos = obter_vizinhos_permutacao(rota_atual)
        melhor_vizinho = min(vizinhos, key=calcular_custo_rota)
        melhor_custo = calcular_custo_rota(melhor_vizinho)
        if melhor_custo >= custo_atual: break
        rota_atual, custo_atual = melhor_vizinho, melhor_custo
    return rota_atual, custo_atual

if __name__ == "__main__":
    r, c = resolver_caixeiro_viajante()
    print(f"Melhor Circuito Local: {' -> '.join(r)} | Distância: {c:.2f} km")
