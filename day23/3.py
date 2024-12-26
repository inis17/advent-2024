import networkx as nx
from collections import defaultdict
G = nx.Graph()
file = open('input.txt')
result = 0
d = defaultdict(list)
for line in file:
    a, b = line.strip().split('-')
    d[a].append(b)
    d[b].append(a)

for key in d:
    G.add_edges_from([(key, elem) for elem in d[key]])

cliques = list(nx.find_cliques(G))
longest = max(cliques, key=len)
longest.sort()
print(','.join(longest))
