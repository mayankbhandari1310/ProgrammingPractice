import random
from collections import defaultdict, deque

class UnDirectedUnweightedGraph:
	def __init__(self):
		self.graph_dict = {}
		self.num_vertices = 0

	def add_vertex(self, vertex_ind):
		if vertex_ind not in self.graph_dict.keys():
			self.graph_dict[vertex_ind] = []
			self.num_vertices += 1

	def add_edge(self, vertex1, vertex2):
		#if vertices are missing then add the vertices first
		if vertex1 not in self.graph_dict.keys():
			self.graph_dict[vertex1] = []
			self.num_vertices += 1
		if vertex2 not in self.graph_dict.keys():
			self.graph_dict[vertex2] = []
			self.num_vertices += 1
		self.graph_dict[vertex1].append(vertex2)
		self.graph_dict[vertex2].append(vertex1)

	def clear_graph(self):
		for ix in self.graph_dict.keys():
			del self.graph_dict[ix]
		del self.graph_dict
		self.graph_dict = {}
		self.num_vertices = 0


	def print_graph(self):
		print("Graph is: ")
		for key in self.graph_dict.keys():
			print("Vertex: ", key, "  has adjacent vertices: ", self.graph_dict[key])


	#does a depth first seach on nodes reachable from start_node
	def dfs(self, start_node):
		#-1 -> not yet encountered, 0 -> pushed in the stack, 1 -> visited and popped
		visited = defaultdict(lambda: -1)
		dfs_stack = deque()
		dfs_stack.append(start_node)
		visited[start_node] = 0
		while dfs_stack:
			cur_vertex = dfs_stack[-1]
			dfs_stack.pop()
			visited[cur_vertex] = 1
			print(cur_vertex, end="->")
			for item in self.graph_dict[cur_vertex]:
				if visited[item] > -1:
					continue
				dfs_stack.append(item)
				visited[item] = 0
		print()



	#does a breadth first seach on nodes reachable from start_node
	def bfs(self, start_node):
		#-1 -> not yet encountered, 0 -> pushed in the stack, 1 -> visited and popped
		visited = defaultdict(lambda: -1)
		bfs_queue = deque()
		bfs_queue.append(start_node)
		visited[start_node] = 0
		while bfs_queue:
			cur_vertex = bfs_queue[0]
			bfs_queue.popleft()
			visited[cur_vertex] = 1
			print(cur_vertex, end="->")
			for item in self.graph_dict[cur_vertex]:
				if visited[item] > -1:
					continue
				bfs_queue.append(item)
				visited[item] = 0
		print()


#Make UnDirectedGraph
graph = UnDirectedUnweightedGraph()
graph.add_edge(1, 2)
graph.add_edge(5, 3)
graph.add_edge(3, 4)
graph.add_edge(3, 2)
graph.add_edge(2, 4)
graph.add_edge(6, 4)
for ix in range(min(graph.graph_dict.keys()), max(graph.graph_dict.keys())+1):
	print("Dfs with starting node: ", ix)
	graph.dfs(ix)

graph.print_graph()

for ix in range(min(graph.graph_dict.keys()), max(graph.graph_dict.keys())+1):
	print("Bfs with starting node: ", ix)
	graph.bfs(ix)



class DirectedUnweightedGraph:
	def __init__(self):
		self.graph_dict = {}
		self.num_vertices = 0

	def add_vertex(self, vertex_ind):
		if vertex_ind not in self.graph_dict.keys():
			self.graph_dict[vertex_ind] = []
			self.num_vertices += 1

	def add_edge(self, vertex1, vertex2):
		#adds a edge directed from vertex1 to vertex2
		#if vertices are missing then add the vertices first
		if vertex1 not in self.graph_dict.keys():
			self.graph_dict[vertex1] = []
			self.num_vertices += 1

		if vertex2 not in self.graph_dict.keys():
			self.graph_dict[vertex2] = []
			self.num_vertices += 1

		self.graph_dict[vertex1].append(vertex2)
		
	def clear_graph(self):
		for ix in self.graph_dict.keys():
			del self.graph_dict[ix]
		del self.graph_dict
		self.graph_dict = {}
		self.num_vertices = 0


	def print_graph(self):
		print("Graph is: ")
		for key in self.graph_dict.keys():
			print("Vertex: ", key, "  has adjacent vertices: ", self.graph_dict[key])


	#does a depth first seach on nodes reachable from start_node
	def dfs(self, start_node):
		#-1 -> not yet encountered, 0 -> pushed in the stack, 1 -> visited and popped
		visited = defaultdict(lambda: -1)
		dfs_stack = deque()
		dfs_stack.append(start_node)
		visited[start_node] = 0
		while dfs_stack:
			cur_vertex = dfs_stack[-1]
			dfs_stack.pop()
			visited[cur_vertex] = 1
			print(cur_vertex, end="->")
			for item in self.graph_dict[cur_vertex]:
				if visited[item] > -1:
					continue
				dfs_stack.append(item)
				visited[item] = 0
		print()



	#does a breadth first seach on nodes reachable from start_node
	def bfs(self, start_node):
		#-1 -> not yet encountered, 0 -> pushed in the stack, 1 -> visited and popped
		visited = defaultdict(lambda: -1)
		bfs_queue = deque()
		bfs_queue.append(start_node)
		visited[start_node] = 0
		while bfs_queue:
			cur_vertex = bfs_queue[0]
			bfs_queue.popleft()
			visited[cur_vertex] = 1
			print(cur_vertex, end="->")
			for item in self.graph_dict[cur_vertex]:
				if visited[item] > -1:
					continue
				bfs_queue.append(item)
				visited[item] = 0
		print()


'''
Topological Sort for DAG, dependency of one task on another is given by the edges
'''
def topological_sort(graph):
	task_order = []
	visited = defaultdict(lambda: -1)
	
	for start_node in graph.keys():
		#-1 -> not yet encountered, 0 -> pushed in the stack, 1 -> visited and popped
		if visited[start_node] > -1:
			continue
		'''
		Dfs is done only on nodes not yet visited
		If visited previously then it means they were in a dfs before 
		'''
		dfs_stack = deque()
		dfs_stack.append(start_node)
		visited[start_node] = 0
		while dfs_stack:
			cur_vertex = dfs_stack[-1]
			#adjacent nodes mean the dependencies of the current vertex
			#if the vertex is visited and the adjacent nodes have been pushed into the stack already
			#then append the current vertex in the task_order list and pop it out of the stack
			if visited[cur_vertex] == 1:
				task_order.append(cur_vertex)
				dfs_stack.pop()
				continue

			#if adjacent nodes not not pushed then push the adjacent nodes	
			#but don't remove the current vertex
			visited[cur_vertex] = 1
			for item in graph[cur_vertex]:
				if visited[item] > -1:
					continue
				dfs_stack.append(item)
				visited[item] = 0
	return task_order


#create graph for topological sort
directed_graph = DirectedUnweightedGraph()
#add directed edges in the graph
directed_graph.add_edge(7, 11)
directed_graph.add_edge(5, 11)
directed_graph.add_edge(3, 8)
directed_graph.add_edge(3, 10)
directed_graph.add_edge(7, 8)
directed_graph.add_edge(11, 2)
directed_graph.add_edge(11, 9)
directed_graph.add_edge(8, 9)
directed_graph.add_edge(11, 10)

task_order = topological_sort(directed_graph.graph_dict)
print("One of the possible orderings: ", task_order)



#Shortest path algorithms
'''
Print shortest path in undirected graph
1. Unweighted graph
2. Weighted graph
'''

#parameter passed is the graph dictionary
#finds one of the shortest path between two nodes in an 
#unweighted undirected graph if it exists, returns the found path
def shortest_path_in_unweighted_graph(graph, start_vertex, destination_vertex):
	#-1 -> not yet encountered, 0 -> pushed in the stack, 1 -> visited and popped
	visited = defaultdict(lambda: 0)

	#path to be returned
	path = []

	#dictionary to store parent node for the vertices inserted
	parent_vertex_dict = defaultdict(lambda: -1)
	bfs_queue = deque()
	bfs_queue.append(start_vertex)
	visited[start_vertex] = 1
	
	while bfs_queue:
		cur_vertex = bfs_queue[0]
		#if cur_vertex is the destination vertex needed, then stop
		if cur_vertex  == destination_vertex:
			break
		#otherwise carry on
		bfs_queue.popleft()
		for item in graph[cur_vertex]:
			if visited[item]:
				continue
			bfs_queue.append(item)
			visited[item] = 1
			parent_vertex_dict[item] = cur_vertex
			
	cur_vertex = destination_vertex
	while cur_vertex != -1:
		path.append(cur_vertex)
		cur_vertex = parent_vertex_dict[cur_vertex]
	return list(reversed(path))

#create graph
graph = UnDirectedUnweightedGraph()
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(2, 5)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 5)
graph.add_edge(4, 6)
graph.add_edge(5, 6)
graph.add_edge(5, 7)
graph.add_edge(6, 7)

graph.print_graph()

for ix in range(3):
	start_vertex = random.randint(1, 7)
	destination_vertex = random.randint(1, 7)
	print("starting vertex: ", start_vertex)
	print("destination_vertex: ", destination_vertex)
	shortest_path = shortest_path_in_unweighted_graph(graph.graph_dict, start_vertex, destination_vertex)
	if shortest_path[0] != start_vertex:
		print("Can't reach destination vertex from starting vertex")
	else:
		print("One of the shortest path can be followed via nodes : ")	
		print(shortest_path)
		print("Path length: ", len(shortest_path)-1)






'''
Djikstra Algorithm, given a graph with weighted edges, returns one of the paths with min-weighted distance
'''
import sys
from sortedcontainers import SortedSet

class UnDirectedWeightedGraph:
	def __init__(self):
		self.graph_dict = {}
		self.num_vertices = 0
		self.distance_dict =  defaultdict(lambda: defaultdict(lambda: -1))
	
	def add_vertex(self, vertex, dist):
		if vertex_ind not in self.graph_dict.keys():
			self.graph_dict[vertex] = []
			self.num_vertices += 1

	def add_edge(self, vertex1, vertex2, dist):
		#if vertices are missing then add the vertices first
		if vertex1 not in self.graph_dict.keys():
			self.graph_dict[vertex1] = []
			self.num_vertices += 1
		if vertex2 not in self.graph_dict.keys():
			self.graph_dict[vertex2] = []
			self.num_vertices += 1
		self.graph_dict[vertex1].append(vertex2)
		self.graph_dict[vertex2].append(vertex1)
		print(self.distance_dict[vertex1][vertex2], self.distance_dict[vertex2][vertex1])
		if self.distance_dict[vertex1][vertex2] == -1 or self.distance_dict[vertex1][vertex2] > dist:
			self.distance_dict[vertex1][vertex2] = dist
			self.distance_dict[vertex2][vertex1] = dist
			#print("Added distances between vertex1 : {}, vertex2: {}, with a value: {}".format(vertex1, vertex2, dist))
		#print(self.distance_dict[vertex1][vertex2], self.distance_dict[vertex2][vertex1])
	def clear_graph(self):
		del self.graph_dict
		self.graph_dict = {}
		self.num_vertices = 0
		del self.distance_dict

	def print_graph(self):
		print("Graph is: ")
		for key in self.graph_dict.keys():
			distances = [self.distance_dict[key][item] for item in self.graph_dict[key]]
			print("Vertex: {}  has adjacent vertices: {} with corresponding distances: {}".format(key, self.graph_dict[key], distances))


#returns one of the paths with min-weighted distance
def djikstra(graph_object, start_vertex, destination_vertex):
	graph = graph_object.graph_dict
	distance_dict = graph_object.distance_dict
	#-1 -> not yet encountered, 0 -> encountered a someone's adjacent neighbour, 1 -> encountered completely
	visited = defaultdict(lambda: -1)
	#distance to unreached node is set to max dist
	min_distance_to_reach_specific_node = defaultdict(lambda: sys.maxsize)
	parent_vertex_dict = defaultdict(lambda: -1)
	priority_vertex_set = SortedSet()
	priority_vertex_set.add((0, start_vertex))
	parent_vertex_dict[start_vertex] = -1
	while priority_vertex_set:
		cur_dist, cur_vertex = priority_vertex_set[0]
		print(cur_dist,cur_vertex)
		priority_vertex_set.discard(priority_vertex_set[0])
		if visited[cur_vertex] == 1:
			continue

		visited[cur_vertex] = 1
		for item in graph[cur_vertex]:
			if visited[item] == 1:
				continue
			else:
				if visited[item] == -1:
					priority_vertex_set.add((cur_dist+distance_dict[cur_vertex][item], item))
					min_distance_to_reach_specific_node[item] = cur_dist+distance_dict[cur_vertex][item]
					visited[item] = 0
					parent_vertex_dict[item] = cur_vertex
				elif min_distance_to_reach_specific_node[item] > cur_dist+distance_dict[cur_vertex][item]:
					priority_vertex_set.add((cur_dist+distance_dict[cur_vertex][item], item))
					min_distance_to_reach_specific_node[item] = cur_dist+distance_dict[cur_vertex][item]
					visited[item] = 0
					parent_vertex_dict[item] = cur_vertex
	path = []
	if visited[destination_vertex] != -1:
		cur_vertex = destination_vertex
		while cur_vertex != -1:
			path.append(cur_vertex)
			cur_vertex = parent_vertex_dict[cur_vertex]
		path = list(reversed(path))
		return (min_distance_to_reach_specific_node[destination_vertex], path)
	else:
		return (-1, path)

#create graph
graph = UnDirectedWeightedGraph()
graph.add_edge(1, 3, 7)
graph.add_edge(1, 4, 5)
graph.add_edge(2, 3, 8)
graph.add_edge(2, 5, 5)
graph.add_edge(3, 4, 9)
graph.add_edge(3, 5, 47)
graph.add_edge(4, 5, 15)
graph.add_edge(4, 6, 6)
graph.add_edge(5, 6, 8)
graph.add_edge(5, 7, 9)
graph.add_edge(6, 7, 55)

graph.print_graph()

min_dist, path = djikstra(graph, 1, 7)
print("Minimum distance to reach is : {} via nodes: {}".format(min_dist, path))




'''
Bellman Ford Algorithm
'''
import sys
from sortedcontainers import SortedSet

class DirectedWeightedGraph:
	def __init__(self):
		self.graph_dict = {}
		self.num_vertices = 0
		self.distance_dict =  defaultdict(lambda: defaultdict(lambda: sys.maxsize))
	
	def add_vertex(self, vertex, dist):
		if vertex_ind not in self.graph_dict.keys():
			self.graph_dict[vertex] = []
			self.num_vertices += 1

	def add_edge(self, vertex1, vertex2, dist):
		#if vertices are missing then add the vertices first
		if vertex1 not in self.graph_dict.keys():
			self.graph_dict[vertex1] = []
			self.num_vertices += 1
		if vertex2 not in self.graph_dict.keys():
			self.graph_dict[vertex2] = []
			self.num_vertices += 1
		self.graph_dict[vertex1].append(vertex2)
		self.distance_dict[vertex1][vertex2] = dist

	def clear_graph(self):
		del self.graph_dict
		self.graph_dict = {}
		self.num_vertices = 0
		del self.distance_dict

	def print_graph(self):
		print("Graph is: ")
		for key in self.graph_dict.keys():
			distances = [self.distance_dict[key][item] for item in self.graph_dict[key]]
			print("Vertex: {}  has adjacent vertices: {} with corresponding distances: {}".format(key, self.graph_dict[key], distances))

def BellmanFord(graph_object, start_vertex):
	graph = graph_object.graph_dict
	distance_dict = graph_object.distance_dict
	min_dist_to_vertex_dict = defaultdict(lambda: sys.maxsize)
	predecessor_dict = {}
	for vertex in graph.keys():
		min_dist_to_vertex_dict[vertex] = sys.maxsize
		predecessor_dict[vertex] = None
	min_dist_to_vertex_dict[start_vertex] = 0
	for ix in range(len(graph.keys())-1):
		for cur_vertex in graph.keys():
			for adj_vertex in graph[cur_vertex]:
				if min_dist_to_vertex_dict[adj_vertex] > min_dist_to_vertex_dict[cur_vertex] + distance_dict[cur_vertex][adj_vertex]:
					min_dist_to_vertex_dict[adj_vertex] = min_dist_to_vertex_dict[cur_vertex] + distance_dict[cur_vertex][adj_vertex]
					predecessor_dict[adj_vertex] = cur_vertex
	
	#assert that there are no negative weight cycles
	for cur_vertex in graph.keys():
		for adj_vertex in graph.keys():
			assert  min_dist_to_vertex_dict[adj_vertex] <= min_dist_to_vertex_dict[cur_vertex] + distance_dict[cur_vertex][adj_vertex]

	return (min_dist_to_vertex_dict, predecessor_dict)

graph = DirectedWeightedGraph()
graph.add_edge(1, 3, 4)
graph.add_edge(1, 2, -1)
graph.add_edge(2, 5, 2)
graph.add_edge(2, 4, 2)
graph.add_edge(2, 3, 3)
graph.add_edge(4, 3, 5)
graph.add_edge(4, 2, 1)
graph.add_edge(5, 4, -3)

print("BellmanFord Testing")
min_distances, predecessors = BellmanFord(graph, 1)
print(min_distances)
print(predecessors)


'''
Prims algorithm, takes the unvisited minimum dist node till now
'''
import sys
from sortedcontainers import SortedSet

class UnDirectedWeightedGraph:
	def __init__(self):
		self.graph_dict = {}
		self.num_vertices = 0
		self.distance_dict =  defaultdict(lambda: defaultdict(lambda: -1))
	
	def add_vertex(self, vertex, dist):
		if vertex_ind not in self.graph_dict.keys():
			self.graph_dict[vertex] = []
			self.num_vertices += 1

	def add_edge(self, vertex1, vertex2, dist):
		#if vertices are missing then add the vertices first
		if vertex1 not in self.graph_dict.keys():
			self.graph_dict[vertex1] = []
			self.num_vertices += 1
		if vertex2 not in self.graph_dict.keys():
			self.graph_dict[vertex2] = []
			self.num_vertices += 1
		self.graph_dict[vertex1].append(vertex2)
		self.graph_dict[vertex2].append(vertex1)
		#print(self.distance_dict[vertex1][vertex2], self.distance_dict[vertex2][vertex1])
		if self.distance_dict[vertex1][vertex2] == -1 or self.distance_dict[vertex1][vertex2] > dist:
			self.distance_dict[vertex1][vertex2] = dist
			self.distance_dict[vertex2][vertex1] = dist
		#print(self.distance_dict[vertex1][vertex2], self.distance_dict[vertex2][vertex1])
	def clear_graph(self):
		del self.graph_dict
		self.graph_dict = {}
		self.num_vertices = 0
		del self.distance_dict

	def print_graph(self):
		print("Graph is: ")
		for key in self.graph_dict.keys():
			distances = [self.distance_dict[key][item] for item in self.graph_dict[key]]
			print("Vertex: {}  has adjacent vertices: {} with corresponding distances: {}".format(key, self.graph_dict[key], distances))


def primsMST(graph_object):
	graph = graph_object.graph_dict
	distance_dict = graph_object.distance_dict
	MST = UnDirectedWeightedGraph()
	visited = set()
	keys = list(graph.keys())
	start_vertex = keys[0]
	visited.add(start_vertex)
	vertices_not_visited_yet = set()
	for vertex in keys[1:]:
		vertices_not_visited_yet.add(vertex)

	print(visited, vertices_not_visited_yet)
	#print(start_vertex)

	num_unvisited_nodes = len(vertices_not_visited_yet)
	for ix in range(num_unvisited_nodes):
		parent_vertex = next(iter(visited))
		min_dist = sys.maxsize
		min_vertetx = -1
		for cur_vertex in visited:
			for adj_vertex in graph[cur_vertex]:
				if adj_vertex in visited:
					continue
				if distance_dict[cur_vertex][adj_vertex] < min_dist:
					min_dist = distance_dict[cur_vertex][adj_vertex]
					min_vertex = adj_vertex
					parent_vertex = cur_vertex
		if min_vertex != -1:
			MST.add_edge(min_vertex, parent_vertex, min_dist)
			visited.add(min_vertex)
			vertices_not_visited_yet.discard(min_vertex)

	return MST

#create graph for mst
graph = UnDirectedWeightedGraph()
graph.add_edge(1, 3, 7)
graph.add_edge(1, 4, 5)
graph.add_edge(2, 3, 8)
graph.add_edge(2, 5, 5)
graph.add_edge(3, 4, 9)
graph.add_edge(3, 5, 7)
graph.add_edge(4, 5, 15)
graph.add_edge(4, 6, 6)
graph.add_edge(5, 6, 8)
graph.add_edge(5, 7, 9)
graph.add_edge(6, 7, 11)

MST = primsMST(graph)
MST.print_graph()
