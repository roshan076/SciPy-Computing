# Shortest Path Algorithm

This module implements Dijkstra's algorithm to find the shortest path between nodes in a weighted, undirected graph. The graph is represented as an adjacency list, and the algorithm computes the minimum distance from a start node to all other nodes. Additionally, it tracks the path taken to reach each node.

---

## Graph Representation

The graph is represented as a dictionary where:
- Each key is a node (a vertex in the graph).
- The value is a list of tuples, where each tuple contains a neighboring node and the weight (distance) to that neighbor.

---

## Function
`shortest_path(graph, start, target='')`
This function computes the shortest path from a specified start node to all other nodes in the graph (or to a specific target node if provided). It uses Dijkstra's algorithm, which is a well-known greedy algorithm for finding the shortest paths from a source node to all other nodes in a weighted graph.

### Parameters:
- `graph`: The input graph, represented as a dictionary of nodes and their neighboring nodes with edge weights.
- `start`: The starting node for the shortest path computation.
- `target` (optional): A specific node to which the shortest path is computed. If not provided, the function calculates the shortest path to all nodes in the graph.

### Algorithm Steps:
#### 1. Initialization:
- `unvisited`: A list of all nodes that have not been visited yet.
- `distances`: A dictionary mapping each node to its shortest known distance from the start node. Initially, the distance to the start node is set to 0, and the distance to all other nodes is set to infinity (float('inf')).
- `paths`: A dictionary mapping each node to the list of nodes representing the path taken to reach that node.

#### 2. Main Loop:
While there are still unvisited nodes:
- The current node is selected as the unvisited node with the smallest known distance.
For each neighboring node of the current node:
- If traveling from the current node to the neighbor results in a shorter path than previously known, update the distance and the path.
- Update the path by appending the current node to the neighbor’s path.
- The current node is then removed from the unvisited list.

#### 3. Path and Distance Calculation:
The algorithm continues until all nodes have been visited, ensuring that the shortest path to each node is determined.
Once the algorithm finishes, it either prints the shortest path and distance to a specific target node (if provided) or to all nodes in the graph.


Example graph:
```python
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}
