from collections import deque

# Exemplo de grafo
grafo = {
    "A": ["B", "D", "B", "C"],
    "B": ["F", "E", "A"],
    "C": ["A"],
    "G": ["D", "I", "H"],
    "J": ["K", "I"],
    "I": ["H", "G", "D", "K", "J"],
    "D": ["G", "A", "H", "I"],
    "F": ["B", "E"],
    "H": ["I", "G", "D"],
    "E": ["F", "B"],
    "N": ["M", "K", "L"],
    "M": ["N", "K", "L"],
    "K": ["M", "L", "N"],
    "L": ["K", "M", "N"]
}

# Busca em Largura (BFS)
def busca_largura(inicio, objetivo):
    fila = deque([[inicio]])
    visitados = set()

    while fila:
        caminho = fila.popleft()
        atual = caminho[-1]

        if atual == objetivo:
            return caminho

        if atual not in visitados:
            for vizinho in grafo[atual]:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                fila.append(novo_caminho)
            visitados.add(atual)

    return None

# Busca em Profundidade (DFS)
def busca_profundidade(inicio, objetivo):
    pilha = [[inicio]]
    visitados = set()

    while pilha:
        caminho = pilha.pop()
        atual = caminho[-1]

        if atual == objetivo:
            return caminho

        if atual not in visitados:
            for vizinho in grafo[atual]:
                novo_caminho = list(caminho)
                novo_caminho.append(vizinho)
                pilha.append(novo_caminho)
            visitados.add(atual)

    return None

# Teste
inicio = "A"
destino = "M"

print("Busca em Largura (BFS):", busca_largura(inicio, destino))
print("Busca em Profundidade (DFS):", busca_profundidade(inicio, destino))
