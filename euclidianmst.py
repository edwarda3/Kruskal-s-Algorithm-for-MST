import os
import sys
import argparse
import math

#We can assume a complete graph for this program.
#Takes input from a file as described in readme.txt
# @param filepath: The path to the textfile which holds the graph information
# @return graphs: A list of graphs, with the number of graphs being equivalent to the <test cases> in the text file.
#				  Each graph is a list of vertices in the form (x,y). Because a complete graph is assumed, no edges are stored here.
def getGraphFromFile(filepath):
	print("Reading file... ", end = '')
	try:
		myfile = open(filepath,'r')
	except IOError:
		print("Failed to read file!")
		sys.exit()
	with myfile:
		data = myfile.read()
	print("Done!")

	index = 1
	info = data.split('\n')
	graphs = [[] for _ in range(int(info[0]))]
	for g in range(int(info[0])):
		for v in range(int(info[index])):
			c = info[index+v+1].split(' ')
			if(c[0].isdigit() and c[1].isdigit()):
				graphs[g].append((int(c[0]),int(c[1])))
		index += int(info[index])+1

	#change occupancy grid from string to matrix 
	return graphs

#A representation of the graph to print out.
# @param graph: The graph to print
# @param n: The number, or index of this graph according to the graphs array.
# @return s: A string which holds the representation
def grepr(graph, n):
	s = ""
	s+="Graph "+str(n)+"\n"
	for vertex in graph:
		s+="\t"+str(vertex)+"\n"
	return s

#A representation of the MST to print out.
# @param weight: Total weight of the MST
# @param tree: The tree of the MST, listed as the edges which make up the tree. Each edge is (u,v) = ((x1,y1),(x2,y2))
# @return s: A string which holds the representation
def mstrepr(weight,tree):
	s=""
	s+="Minimum Spanning Tree:\n"
	s+="Weight: "+str(weight)+"\n"
	s+="Tree edges:\n"
	for edge in tree:
		s+="\t"+str(edge)+"\n"
	return s

#Returns the euclidian distance between two points rounded to the nearest integer.
# @param v1: The first point as (x,y)
# @param v2: The second point as (x,y)
# @return value: The distance between v1, v2 to the nearest integer.
def getdist(v1, v2):
	(x1,y1) = v1
	(x2,y2) = v2
	return round(math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2)))

#Checks to see if all vertices are part of the same component.
#This acts as a premature end, because in a connected graph, most edges are going to be useless. (time savings)
# @param sets: The dictionary which contains information about the connected components of the tree.
# @return: True if there is only a single connected component (a full tree). False otherwise.
def isDone(sets):
	val = None
	for key in sets:
		if(val == None):
			val = sets[key]
		else:
			if(not val == sets[key]):
				return False
	return True

#Finds the MST of a complete graph given the euclidian points as vertices.
#Use Kruskal's Algorithm: https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
# @param g: A graph representation where we are given points as vertices.
# @return weight: The total weight of the MST.
# @return tree: A list of edges which make up the MST.
def findMST(g):
	# Make a list of all edges, and store them as (dist, v1, v2), and sort them
	edges = []
	for v1i in range(len(g)):
		for v2i in range(v1i+1,len(g)):
			edges.append((getdist(g[v1i],g[v2i]),g[v1i],g[v2i]))
	edges.sort()

	# Set up a dictionary "sets", which assigns a value to each vertex.
	# This value will become representative of the connected component that each vertex belongs to.
	# Each vertex will have a unique value to start (as there are no edges yet).
	sets = {}
	for v in range(len(g)):
		sets[g[v]] = v
	tree = []
	weight = 0

	# Traverse through the sorted list of edges (lowest first)
	# At each edge, If both vertices are part of different components, then join them.
	# When joining two components, change all vertices that share that component number and change it to the component number that we merge with. 
	for edge in edges:
		if(not sets[edge[1]] == sets[edge[2]]):
			setnum = sets[edge[1]]
			setnumchange = sets[edge[2]]
			# Go through and change all keys connected to the second vertex of this edge.
			for key in sets:
				if(sets[key]==setnumchange):
					sets[key] = setnum
			tree.append((edge[1],edge[2]))
			weight+=edge[0]
			if(isDone(sets)):
				break

	return (weight,tree)

if __name__ == "__main__":
	""" parser = argparse.ArgumentParser()
	parser.add_argument("graphfile", help="Text repr of graph")
	args=parser.parse_args()
	wfile = args.graphfile """
	wfile="graph.txt"
	cwd = os.getcwd()

	graphs = getGraphFromFile(cwd+"/"+wfile)

	index = 1
	# Find the MST for each graph we have read.
	for graph in graphs:
		(weight, tree) = findMST(graph)
		#print("\n---\n"+grepr(graph,index))
		#print(mstrepr(weight,tree))
		print("Test case "+str(index)+": MST Weight "+str(weight))
		index+=1