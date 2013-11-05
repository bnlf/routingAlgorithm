"""
The Bellman-Ford algorithm

Graph API:

    iter(graph) gives all nodes
    iter(graph[u]) gives neighbours of u
    graph[u][v] gives weight of edge (u, v)
    
"""

import sys
import csv

def initialize(graph, source):
    d = {}
    p = {}
    for node in graph:
        d[node] = float('Inf')
        p[node] = None
    d[source] = 0
    return d, p

def relax(u, v, graph, d, p):
    if d[v] > d[u] + graph[u][v]:
        d[v]  = d[u] + graph[u][v]
        p[v] = u

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    for i in range(len(graph)-1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)
    for u in graph:
        for v in graph[u]:
            assert d[v] <= d[u] + graph[u][v]
    return d, p

def read_file():
    graph = {}
    reader = csv.reader(open(sys.argv[1]), delimiter='\t')
    for row in reader:
        orig = int(row[0])
        dest = int(row[1])
        weight = int(row[2])
        d = graph.get(orig)
        if not d:
            graph[orig] = {dest: weight}
        else:
            d[dest] = weight
            graph[orig] = d
    return graph

def test():
    #g = read_file()
    g = read_file()
    
    d, p = bellman_ford(g, 0)
    print d
    print p
    
    graph = {
        'a': {'b': -1, 'c':  4},
        'b': {'c':  3, 'd':  2, 'e':  2},
        'c': {},
        'd': {'b':  1, 'c':  5},
        'e': {'d': -3}
        }
    
    d, p = bellman_ford(graph, 'a')
    print d
    print p
    
    #assert d == {
    #    'a':  0,
    #    'b': -1,
    #    'c':  2,
    #    'd': -2,
    #    'e':  1
    #    }
    #
    #assert p == {
    #    'a': None,
    #    'b': 'a',
    #    'c': 'b',
    #    'd': 'e',
    #    'e': 'b'
    #    }

if __name__ == '__main__': 
    test()
