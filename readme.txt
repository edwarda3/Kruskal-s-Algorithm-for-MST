Uses Kruskal's algorithm to find the Minimum Spanning Tree of a complete, undirected graph in 2-d geopetric plane, with the vertices each being a (x,y) point, and the edges being the euclidian distance between them.

Code written by Alex Edwards for CS 420 class at Oregon State University

Find the longest path by running 

$ python3 euclidian-mst.py

Keep a file named graph.txt in the same directory with the following format:

------
1	<# test cases/graphs>
2	<# vertices>
3	<point1 point2>
4	<point1 point2>
5	<point1 point2>
6	...

------

For example,

3
3
0 1
2 1
2 5
5
0 0
0 4
4 4
4 8
1 1

Alternatively, use run visualizer.py

$ python3 visualizer.py

Which visualizes the result using pygame. 
Use LMouse to add a node at the position of the cursor.
Use RMouse to randomly scatter 50 points.
Press Spacebar to clear the graph.
