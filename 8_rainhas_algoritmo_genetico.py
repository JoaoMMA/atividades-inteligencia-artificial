import random

TAM_POPULACAO = 100
TAXA_MUTACAO = 0.05
MAX_PARES_IDEAL = 28

def calcular_fitness(individuo):
    ataques = 0
    n = len(individuo)
    for i in range(n):
        for j in range(i + 1, n):
            if individuo[i] == individuo[j] or abs(individuo[i] - individuo[j]) == abs(i - j):
                ataques += 1
    return MAX_PARES_IDEAL - ataques

def crossover(pai1, pai2):
    ponto = random.randint(1, 6)
    return pai1[:ponto] + pai2[ponto:], pai2[:ponto] + pai1[ponto:]

def mutar(individuo):
    if random.random() < TAXA_MUTACAO:
        individuo[random.randint(0, 7)] = random.randint(0, 7)
    return individuo

def algoritmo_genetico():
    populacao = [[random.randint(0, 7) for _ in range(8)] for _ in range(TAM_POPULACAO)]
    while True:
        populacao_avaliada = [(ind, calcular_fitness(ind)) for ind in populacao]
        populacao_avaliada.sort(key=lambda x: x[1], reverse=True)
        if populacao_avaliada[0][1] == MAX_PARES_IDEAL:
            return populacao_avaliada[0][0]
        
        nova_pop = [populacao_avaliada[0][0], populacao_avaliada[1][0]]
        while len(nova_pop) < TAM_POPULACAO:
            p1 = random.choice(populacao_avaliada[:20])[0]
            p2 = random.choice(populacao_avaliada[:20])[0]
            f1, f2 = crossover(p1, p2)
            nova_pop.extend([mutar(f1), mutar(f2)])
        populacao = nova_pop[:TAM_POPULACAO]

if __name__ == "__main__":
    print(f"Solução Evoluída por AG: {algoritmo_genetico()}")
