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

