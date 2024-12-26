from collections import defaultdict


def find_cliques(graph):
    cliques = []
    visited = set()

    def dfs(node, clique):
        visited.add(node)
        clique.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, clique)

    for node in graph:
        if node not in visited:
            clique = set()
            dfs(node, clique)
            if len(clique) > 1:
                cliques.append(clique)

    return cliques


# Example usage
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['A', 'B', 'C', 'E'],
    'E': ['F'],
    'F': ['E']
}

cliques = find_cliques(graph)
print(f'Number of cliques: {len(cliques)}')
print(f'Cliques: {cliques}')
