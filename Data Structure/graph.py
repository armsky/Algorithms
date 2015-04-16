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

# BFS traversal
# Time Complexity: O(V+E)
# Use a boolean visited array.
# NOTE: this will only work when it can traversal all vertices start from the given vertex
def BFS(s):
    # s is a int and means the start point
    visited = [0]*V
    # Create a queue for BFS
    queue = Queue.Queue()
    queue.put(s)
    visited[s] = 1
    while queue is not None:
        s = queue.get()
        print s
        # Get all adjacent vertices of the dequeued s
        # If a adjacent has not been visited, mark and enqueue it
        for i in xrange(len(adj[s])): # adj[s] is a list of all adjacent vertices of s
            if visited[i] == 0:
                visited[i] = 1
                queue.put(i)
# revised version: Can traverse every vertex
def BFS(V):
    visited = [0] * V
    queue = Queue.Queue()
    for i in xrange(V):
        if visited[i] == 0:
            queue.put(i)
            visited[i] = 1
            while queue is not None:
                s = queue.get()
                print s
                for i in xrange(len(adj[s])):
                    if visited[i] == 0:
                    visited[i] = 1
                    queue.put(i)


# DFS traversal
# O(V+E) time
# NOTE:Since tried every vertex, so this is a full traversal
def DFSUtil(v, visited):
    visited[v] = 1
    print v
    for i in xrange(len(adj[v])):
        if visited[i] == 0:
            DFSUtil(1, visited)

def DFS(V):
    visited = [0] * V
    for i in xrange(V):
        if visited[i] == 0:
            DFSUtil(i, visited)
