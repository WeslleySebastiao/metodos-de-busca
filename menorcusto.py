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

def ucs(inicio, objetivo):
    # (custo acumulado, caminho até agora)
    fila = [(0, [inicio])]
    visitados = set()

    while fila:
        custo_atual, caminho = heapq.heappop(fila)
        no_atual = caminho[-1]

        if no_atual == objetivo:
            return caminho, custo_atual

        if no_atual not in visitados:
            visitados.add(no_atual)

            for vizinho, custo in grafo.get(no_atual, []):
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                heapq.heappush(fila, (custo_atual + custo, novo_caminho))

    return None, float('inf')


# Execução
caminho, custo_total = ucs('A', 'F')
print("Caminho encontrado:", " → ".join(caminho))
print("Custo total:", custo_total)
