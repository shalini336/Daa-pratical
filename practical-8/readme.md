# Practical 8 - Graph and Searching (DFS and BFS)

## Aim

To implement a graph and perform Depth First Search (DFS) and Breadth First Search (BFS) in Python.

## Graph Representation

The graph is represented using an adjacency list.

Vertices are numbered from 1 to n.

## 1. Depth First Search (DFS)

### Algorithm

1. Start.
2. Create an empty set of visited vertices.
3. Select the starting vertex.
4. Mark the starting vertex as visited.
5. Display the vertex.
6. Visit each adjacent vertex.
7. If an adjacent vertex is not visited, recursively perform DFS on that vertex.
8. Continue until all reachable vertices are visited.
9. Stop.

### Time Complexity

- O(V + E)

### Space Complexity

- O(V)

## 2. Breadth First Search (BFS)

### Algorithm

1. Start.
2. Create an empty set of visited vertices.
3. Create a queue.
4. Add the starting vertex to the queue and mark it as visited.
5. Remove a vertex from the front of the queue.
6. Display the vertex.
7. Add all unvisited adjacent vertices to the queue.
8. Mark the newly added vertices as visited.
9. Repeat until the queue becomes empty.
10. Stop.

### Time Complexity

- O(V + E)

### Space Complexity

- O(V)

Where:

- `V` = number of vertices
- `E` = number of edges

## Example

### Input

```text
Enter number of vertices: 4
Enter number of edges: 4

Enter starting vertex: 1
Enter ending vertex: 2
Enter starting vertex: 1
Enter ending vertex: 3
Enter starting vertex: 2
Enter ending vertex: 4
Enter starting vertex: 3
Enter ending vertex: 4

Enter starting vertex: 1