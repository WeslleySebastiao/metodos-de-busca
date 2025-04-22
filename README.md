# metodos-de-busca
Métodos de busca são estratégias usadas para encontrar uma solução dentro de um espaço de possibilidades (como caminhos em um grafo, movimentos em um jogo ou estados de um problema). Eles são fundamentais em áreas como inteligência artificial, ciência da computação e algoritmos.

# Busca não informada (ou cega)
-Não usam nenhuma informação extra sobre o problema além da estrutura do próprio grafo-

**Busca em largura (BFS):** explora os nós nível por nível.

**Busca em profundidade (DFS):** vai o mais fundo possível antes de voltar.

**Busca de custo uniforme:** sempre expande o nó de menor custo acumulado.

# Busca informada (ou heurística)
-Utiliza uma função heurística (uma estimativa) para guiar a busca-

**Busca gulosa:** escolhe o próximo nó com base na menor estimativa de custo até o objetivo.

**Busca A***: considera tanto o custo acumulado quanto a estimativa até o objetivo (mais completa e eficiente, se a heurística for boa).
