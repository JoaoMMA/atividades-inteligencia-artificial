def avaliar_bc(modelo):
    regra1 = not modelo['P'] or modelo['Q']
    regra2 = modelo['P']
    return regra1 and regra2

def avaliar_alfa(modelo):
    return modelo['Q']

def tt_entails(simbolos, modelo):
    if not simbolos:
        if avaliar_bc(modelo): return avaliar_alfa(modelo)
        return True
    simbolo_atual = simbolos[0]
    restante = simbolos[1:]
    return (tt_entails(restante, {**modelo, simbolo_atual: True}) and 
            tt_entails(restante, {**modelo, simbolo_atual: False}))

if __name__ == "__main__":
    print(f"Resultado de Provador Logico TT-Entails: {tt_entails(['P', 'Q'], {})}")
