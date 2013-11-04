#
# MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
# Autor: Bruno Nunes Leal Faria - nUSP: 8765551
#
# FILE: main.py
#

import sys

# checks input arguments
def check_args():
	search_types = ["L", "P"]
	if len(sys.argv) < 3:
		print "Usage: <input_file> <type>"
		print "Search Type: L (largura), P (profundidade)"
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

# main execution
if check_args():
	graph = read_file()
	#print graph
	print bfs(graph, 0, 8)
