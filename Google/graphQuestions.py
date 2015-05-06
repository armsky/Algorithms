"""
1. Even Tree
Given a tree (simple graph with no cycles), remove as many edges form the tree as
possible to obtain a forest while: Each connected component of the forest should
contain an even number of vertices. Find out the number of removed edges
--
input format:
    two integers means two vertices, and a edge betweens them
    Vertices list: V, Edges list: E
Forest:
    A forest is an undirected graph, all of whose connected components are trees; in other words, the graph consists of a disjoint union of trees. Equivalently, a forest is an undirected cycle-free graph. As special cases, an empty graph, a single tree, and the discrete graph on a set of vertices (that is, the graph with these vertices that has no edges), all are examples of forests.
"""
# Create a list of size (n+1), store the children numbers of each node.
# Counting the nodes in list with even childrens.
def eventree(V, E): # E is a list of items like (v1, v2),
    # helper to find all children of nth vertex
    def find_children(n):
        children = []
        for x in xrange(len(E)):
            if E[x][1] == n:
                children.append(E[x][0])
                # Recursively find grand childerens
                g_children = find_children(E[x][0])
                for child in g_children:
                    children.append(child)
        return children

    # build a tree, store children numbers
    tree = []
    for x in xrange(len(V)):
        tree.append(find_children(x))
    # if a vertex has odd number of children, cut it and count it
    count = 0
    for x in xrange(len(V)):
        if len(tree[x]) %2 == 1:
            count += 1
    return count-1 # NOTE: count is the tree number, removed edge number should -1

"""
2. Longest path problem: find a longest path of a directed acyclic graph
"""

"""
3. Traveling Salesman Problem (TSP)
Given a set of cities and distance between every pair of cities, the problem is to find the shortest possible route that visits every city exactly once and returns to the starting point.

NOTE: We already know that Hamiltonian Tour exists here
"""
# 1. Naive solution
"""
1. iterrate each city as start
2. generage all (n-1)! factorial permutations of cities, find the minimum one
Big-Omega(n!) time !!!
"""
# 2. DP solution
# O(n^2 * 2^n) time, much less than O(n!), space is also exponential
"""
1. Consider
"""

"""
4. Dijkstra's shortest path (Greedy)
Thie code for all verteice to src, but can modify to specify vertex
O(V^2) time with this matrix representation
Dijkstra DOES NOT work for negative weight graph.
"""
# a. create an empty shortest path tree set
# b. assign source vertex as 0, others as infinite
# c. while sptSet does not inlcude all vertices:
#       1. pick a vertex u that not in sptSet has min distance value
#       2. include u to sptSet
#       3. update distance value of all adjacent vertices of u
def min_dist(dist, sptSet):
    min_v = max_int
    for v in xrange(len(dist)):
        if sptSet[v] == 0 and dist[v] <= min_v:
            min_v = dist[v]
            min_index
    return min_index

def dijkstra(graph, src):
    # graph use matrix as [V][V]
    dist = [max_int] * V # output, hold the shortest path form src to i
    dist[src] = 0
    sptSet = [0] * V

    for x in xrange(V):
        u = min_dist(dist, sptSet)
        sptSet[u] = 1
        for v in xrange(V):
            if sptSet[v] == 0 and graph[u][v] != 0 \
                    and dist[u] != max_int \
                    and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

# Can be reduced to O(E log V) is use adjacency list
# With the help of min-heap, put all vertices into heap

"""
5. Prim's Minimum Spanning Tree, MST, Greedy
Spanning tree means all vertices must be connected. MST is with min weight edges
"""
# a. mstSet keep vertices already included
# b. mark src value as 0, others as infinite
# c. while mstSet doesn't include all vertices:
#       (same as Dijkstra, but D is dist to src, MST is for know vertices)

"""
6. Clone Graph
Given a undirected node (node in the graph contains a label and a list of its neighbors), return a undirected graph node.
A serialized graph represented as {0,1,2#1,2#2,2}

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""
#   a. DFS
#   Use a dict to map all nodes and their clones {node: clone}
def cloneGraph(self, node):
    if node is None:
        return None
    node_map = {}
    return cloneNode(node, node_map)

def cloneNode(self, node, node_map):
    if node is None:
        return None
    if node_map.has_key(node):
        return node_map[node]
    clone = UndirectedGraphNode(node.label)
    for neighbor in node.neighbors:
        clone.neighbors.append(self.cloneNode(neighbor, node_map))
# b. BFS
# Use a queue and a dict
import Queue
def cloneGraph(self, node):
    if node is None:
        return None
    queue = Queue.Queue()
    new_node = UndirectedGraphNode(node.label)
    queue.put(node)
    map = {}
    map[node] = new_node
    while queue is not None:
        curr = queue.get()
        for nb in curr.neighbors:
            if nb not in map:
                queue.put(nb)
                clone = UndirectedGraphNode(curr.label)
                map[curr].neighbors.append(clone)
                map[nb] = clone
            else:
                # Turn directed graph to undirected graph
                map[curr].neighbors.append(map[nb])
    return new_node
