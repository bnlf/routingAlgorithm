# Redes de computadores
#
# FILE: main.py
#

import sys, time

# checks input arguments
def check_args():
	search_types = ["B", "D"]
	if len(sys.argv) < 4:
		print "Usage: <input_file> <type> <destination>"
		print "Search Type: B (bfs), iDFS"
		return False
	elif str(sys.argv[2]).upper() not in search_types:
		print "Search type \"%s\" not supported" % (sys.argv[2])
		return False
	else:
		return True

# checks/parses input file
def read_file():
	graph = {}
	values = []
	f = open(sys.argv[1], 'r')
	for row,line in enumerate(f.read().strip().split('\n')):
		for col,val in enumerate(line.split('	')):
			if col == 0:
				key = val
			if col == 1:
				value = val
		if not graph.get(int(key)):
			graph[int(key)] = []
		if not graph.get(int(value)):
			graph[int(value)] = []
		graph[int(key)].append(int(value))
	return graph

# Breadth first search
def bfs(graph, start, end):
	todo = [[start, [start]]]
	while 0 < len(todo):
		(node, path) = todo.pop(0)
		for next_node in graph[node]:
			if next_node in path:
				continue
			elif next_node == end:
				return path + [next_node]
			else:
				todo.append([next_node, path + [next_node]])

# depth first search
def idfs(graph, start, end, depth, path=[], i=0):
	path = path + [start]
	if start == end or i > depth:
		return path
	if not graph.has_key(start):
		return None
	shortest = None
	for node in graph[start]:
		if node not in path:
			i+=1
			newpath = idfs(graph, node, end, depth, path, i)
			if newpath:
				if not shortest or len(newpath) < len(shortest):
					shortest = newpath
	return shortest

# def relax(u, v, graph, d, p):
#     if d[v] > d[u] + graph[u][v]:
#         d[v]  = d[u] + graph[u][v]
#         p[v] = u

# def bellman_ford(graph, source):
#     d, p = initialize(graph, source)
#     for i in range(len(graph)-1):
#         for u in graph:
#             for v in graph[u]:
#                 relax(u, v, graph, d, p)
#     for u in graph:
#         for v in graph[u]:
#             assert d[v] <= d[u] + graph[u][v]
#     return d, p

# main execution
if check_args():
	graph = read_file()
	#print graph
	start_time = time.time()
	result = bfs(graph, 0, int(sys.argv[3]))
	print result, len(result)
	print time.time() - start_time, "seconds"
	#print idfs(graph, 0, 5022, 40, [], 0)
