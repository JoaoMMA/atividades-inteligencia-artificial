import random

def calcular_conflitos(estado):
    conflitos = 0
    n = len(estado)
    for i in range(n):
        for j in range(i + 1, n):
            if estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j):
                conflitos += 1
    return conflitos

def obter_melhor_sucessor(estado):
    melhor_estado = list(estado)
    min_conflitos = calcular_conflitos(estado)
    n = len(estado)

    for col in range(n):
        linha_original = estado[col]
        for linha in range(n):
            if linha == linha_original:
                continue
            estado_teste = list(estado)
            estado_teste[col] = linha
            conflitos_teste = calcular_conflitos(estado_teste)
            if json_teste < min_conflitos:
                min_conflitos = conflitos_teste
                melhor_estado = estado_teste
    return melhor_estado, min_conflitos

def resolver_8_rainhas():
    passo = 0
    while True:
        estado_atual = [random.randint(0, 7) for _ in range(8)]
        conflitos_atuais = calcular_conflitos(estado_atual)
        print(f"[Reinício] Novo Estado Inicial Completo: {estado_atual} | Conflitos: {conflitos_atuais}")

        while True:
            proximo_estado, novos_conflitos = obter_melhor_sucessor(estado_atual)
            if novos_conflitos >= conflitos_atuais:
                break 
            estado_atual = proximo_estado
            conflitos_atuais = novos_conflitos
            passo += 1
            print(f" -> Passo {passo}: Tabuleiro alterado para {estado_atual} | Conflitos: {conflitos_atuais}")
            if conflitos_atuais == 0:
                return estado_atual

def exibir_tabuleiro(estado):
    print("\n Visão do Tabuleiro Resolvido:")
    print("  " + " ".join(str(i) for i in range(8)))
    for linha in range(8):
        linha_visual = []
        for col in range(8):
            linha_visual.append("👑" if estado[col] == linha else " .")
        print(f"{linha} " + " ".join(linha_visual))
    print("-" * 25)

if __name__ == "__main__":
    print("=== INICIANDO SIMULAÇÃO: AGENTE 8 RAINHAS (ESTADOS COMPLETOS) ===")
    solucao = resolver_8_rainhas()
    print(f"\n=== OBJETIVO ALCANCADO ===")
    print(f"Configuração do Vetor Solução: {solucao}")
    exibir_tabuleiro(solucao)
