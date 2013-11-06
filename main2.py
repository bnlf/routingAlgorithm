# Redes de computadores
#
# FILE: main.py
#

import sys
from random import randrange

# Import pygraph
from pygraph.classes.graph import graph
from pygraph.classes.digraph import digraph
from pygraph.algorithms.searching import breadth_first_search
from pygraph.algorithms.searching import depth_first_search

# checks input arguments
def check_args():
	search_types = ["B"]
	if len(sys.argv) < 3:
		print "Usage: <input_file> <type>"
		print "Search Type: B (bfs)"
		return True
	elif str(sys.argv[2]).upper() not in search_types:
		print "Search type \"%s\" not supported" % (sys.argv[2])
		return False
	else:
		return True

# checks/parses input file
def read_file():
	# Graph creation
	gr = graph()
	f = open(sys.argv[1], 'r')
	for row,line in enumerate(f.read().strip().split('\n')):
		for col,val in enumerate(line.split('	')):
			if col == 0:
				key = val
			if col == 1:
				value = val
		if not gr.has_node(key):
			gr.add_node(key)
		if not gr.has_node(value):
			gr.add_node(value)
		gr.add_edge((key,value), randrange(10))
	return gr

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

# main execution
if check_args():
	graph = read_file()
	#print graph
	st, pre, post = depth_first_search(graph, root='9')
	print st
	#print bfs(graph, 0, 235)
