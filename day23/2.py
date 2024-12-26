from collections import defaultdict


maxLength = 2


def findLoop3(graph, start, end, path=[]):
    path = path + [start]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node == end:
            paths.append(path)
        if node not in path:
            newpaths = findLoop3(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def findCLuster(graph, start, end, cnode=[]):
    cnode = cnode + [start]
    if start not in graph:
        return []
    cnodes = []
    for node in graph[start]:

    return paths


def checkHasLink(graph, iterNode, elem):
    for node in iterNode:
        if elem not in graph[node]:
            return False
    return True


def checkHasT(iter):
    for elem in iter:
        if elem.startswith('t'):
            return True
    return False


file = open('input.txt')
result = 0
d = defaultdict(list)
for line in file:
    a, b = line.strip().split('-')
    d[a].append(b)
    d[b].append(a)

# print(d)
result = set()
for elem in d:
    loops = findLoop3(d, elem, elem)
    floops = {frozenset(x) for x in loops}
    result = result | floops

result = {x for x in result if checkHasT(x)}


print(len(result))
