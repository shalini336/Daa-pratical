from collections import deque


# Create graph using adjacency list
def create_graph(vertices, edges):
    graph = {i: [] for i in range(1, vertices + 1)}

    for _ in range(edges):
        u = int(input("Enter starting vertex: "))
        v = int(input("Enter ending vertex: "))

        graph[u].append(v)
        graph[v].append(u)

    return graph


# Depth First Search
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    # Visit unvisited adjacent vertices
    for vertex in graph[start]:
        if vertex not in visited:
            dfs(graph, vertex, visited)


# Breadth First Search
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        # Visit unvisited adjacent vertices
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# Take graph input
vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

graph = create_graph(vertices, edges)

print("\nGraph:")
for vertex in graph:
    print(vertex, ":", graph[vertex])

# Take starting vertex
start = int(input("\nEnter starting vertex: "))

# DFS
print("\nDFS Traversal:")
dfs(graph, start)

# BFS
print("\n\nBFS Traversal:")
bfs(graph, start)

print()