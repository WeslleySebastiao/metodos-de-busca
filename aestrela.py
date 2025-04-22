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
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 3,
    'F': 0
}

def a_estrela(inicio, objetivo):
    # (f = custo + heurística, custo real, caminho até agora)
    fila = [(heuristica[inicio], 0, [inicio])]
    visitados = set()

    while fila:
        f_total, custo_real, caminho = heapq.heappop(fila)
        no_atual = caminho[-1]

        if no_atual == objetivo:
            return caminho, custo_real

        if no_atual not in visitados:
            visitados.add(no_atual)

            for vizinho, custo in grafo.get(no_atual, []):
                g = custo_real + custo  # custo real acumulado
                h = heuristica[vizinho]
                f = g + h
                heapq.heappush(fila, (f, g, caminho + [vizinho]))

    return None, float('inf')


# Execução
caminho, custo_total = a_estrela('A', 'F')
print("Caminho A* encontrado:", " → ".join(caminho))
print("Custo total:", custo_total)
