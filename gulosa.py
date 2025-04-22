import heapq

# Representação do grafo com custos
grafo = {
    'A': [('B', 10), ('C', 2)],
    'B': [('C', 3), ('D', 3)],
    'C': [('E', 4)],
    'D': [('F', 6)],
    'E': [('D', 3), ('F', 12)],
    'F': []
}

# Exemplo de Heurística estimada até o nó F
heuristica = {
    'A': 16,
    'B': 8,
    'C': 14,
    'D': 6,
    'E': 12,
    'F': 0,
}

def busca_gulosa(inicio, objetivo):
    # (heurística, caminho)
    fila = [(heuristica[inicio], [inicio])]
    visitados = set()

    while fila:
        h_atual, caminho = heapq.heappop(fila)
        no_atual = caminho[-1]

        if no_atual == objetivo:
            return caminho

        if no_atual not in visitados:
            visitados.add(no_atual)

            for vizinho, _ in grafo.get(no_atual, []):
                if vizinho not in visitados:
                    heapq.heappush(fila, (heuristica[vizinho], caminho + [vizinho]))

    return None


# Execução
caminho = busca_gulosa('A', 'F')
print("Caminho pela Busca Gulosa:", " → ".join(caminho))
