class MundoWumpusLogico:
    def __init__(self):
        self.tamanho = 4
        self.posicao_ouro = (1, 2)
        self.posicao_wumpus = (2, 0)
        self.posicao_pocos = [(0, 2), (2, 3)]
        self.bc_visitados = set()
        self.bc_seguras = set([(0, 0)])
        self.bc_percepcoes = {}

    def obter_percepcao(self, pos):
        percepcao = []
        l, c = pos
        vizinhos = [(l+1, c), (l-1, c), (l, c+1), (l, c-1)]
        if pos == self.posicao_ouro: percepcao.append('Brilho')
        for v in vizinhos:
            if v == self.posicao_wumpus: percepcao.append('Fedor')
            if v in self.posicao_pocos: percepcao.append('Brisa')
        return set(percepcao)

    def obter_vizinhos_validos(self, pos):
        return [v for v in [(pos[0]+1, pos[1]), (pos[0]-1, pos[1]), (pos[0], pos[1]+1), (pos[0], pos[1]-1)] 
                if 0 <= v[0] < self.tamanho and 0 <= v[1] < self.tamanho]

    def raciocinar(self, pos_atual):
        self.bc_visitados.add(pos_atual)
        percepcoes = self.obter_percepcao(pos_atual)
        self.bc_percepcoes[pos_atual] = percepcoes
        vizinhos = self.obter_vizinhos_validos(pos_atual)
        if 'Brisa' not in percepcoes and 'Fedor' not in percepcoes:
            for v in vizinhos: self.bc_seguras.add(v)

    def simular(self):
        pos_atual = (0, 0)
        for _ in range(15):
            self.raciocinar(pos_atual)
            if 'Brilho' in self.bc_percepcoes[pos_atual]:
                print(f"[SUCESSO] Ouro coletado em {pos_atual}!"); return
            proxima = None
            for v in self.obter_vizinhos_validos(pos_atual):
                if v in self.bc_seguras and v not in self.bc_visitados:
                    proxima = v; break
            if not proxima:
                for v in self.bc_seguras:
                    if v in self.obter_vizinhos_validos(pos_atual): proxima = v; break
            if proxima: pos_atual = proxima
            else: return

if __name__ == "__main__":
    MundoWumpusLogico().simular()
