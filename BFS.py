def bfs(graph, node):
    visited = []
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m)
        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("BFS")
bfs(graph, 'A')

