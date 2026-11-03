print("hello")
graph = {
    'A' : ['B','C'],
    'B' : ['A','D','E'],
    'C' : ['A','F'],
    'D' : ['B'],
    'E' : ['B','F'],
    'F' : ['C','E']

}

def dfs(node,visited):
    if node not in visited :
        print(node,end=" ")
        visited.add(node)

        for neighbour in graph[node]:
            dfs(neighbour,visited)

def bfs(start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node,end=" ")
            visited.add(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

print("Dfs Traversal")
dfs('A',set())

print("\nBfs Traversal")
bfs('A')