"""
1). A SIMPLE graph satisfying:
    1. Having at most one edge between two nodes (vertices).
    2. Not having an edge coming back to the original node (vertex).

2). Two vertices, v and w are ADJACENT is there is an edge vx joining them
The two vertices are then concidered INCIDENT to the edge vw.

3). The DEGREE of a vertex v is the number of edges incident with v.


Eulerian:
If a graph has way of getting from one vertex to another that includes every edge exactly once and ends at the initial vertex.
( if and only if the degree of each vertex of G is even then it's solvable)

Hamiltonian:
if a graph has a path that includes every vertex exactly once, while ending at the initial vertex.

semi-Hamiltonian:
if a graph has a path that includes every vertex exactly once, but ending at another vertex than the starting one.
"""

# BFS
# Time Complexity: O(V+E) where V is number of vertices in the graph
#   and E is number of edges in the graph.
