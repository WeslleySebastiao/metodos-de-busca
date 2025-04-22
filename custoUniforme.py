import heapq

# Exemplo de grafo com pesos
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [],
    'F': [('G', 2)],
    'G': []
}

def busca_custo_uniforme(grafo, inicio, objetivo):
    # Fila de prioridade: (custo acumulado, nó atual, caminho até o nó)
    fila = [(0, inicio, [inicio])]
    visitados = set()

    while fila:
        custo, no_atual, caminho = heapq.heappop(fila)

        if no_atual in visitados:
            continue
        visitados.add(no_atual)

        if no_atual == objetivo:
            return caminho, custo

        for vizinho, custo_ate_vizinho in grafo.get(no_atual, []):
            if vizinho not in visitados:
                heapq.heappush(fila, (custo + custo_ate_vizinho, vizinho, caminho + [vizinho]))

    return None, float('inf')



# Executar busca
caminho, custo_total = busca_custo_uniforme(grafo, 'A', 'G')
print("Caminho encontrado:", caminho)
print("Custo total:", custo_total)
