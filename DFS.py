def dfs(graph,node):
    S=[]
    visited=[]
    S.append(node)
    while(S):
        x=S.pop()
        if(x not in visited):
            visited.append(x)
            for i in graph[x]:
                S.append(i)
    print(visited)

graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("DFS")
dfs(graph, 'A')