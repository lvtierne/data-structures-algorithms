# Graph class using an adjacency list
class Graph:
    def __init__(self):
        self.graph = {}  # Initialize an empty dictionary to hold the graph

    def add_vertex(self, vertex):
        # Add a vertex to the graph
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex, edge):
        # Add an edge to the graph (undirected)
        if vertex in self.graph:
            self.graph[vertex].append(edge)
        if edge in self.graph:
            self.graph[edge].append(vertex)

    def print_graph(self):
        # Print the adjacency list of the graph
        for vertex in self.graph:
            print(f"{vertex}: {self.graph[vertex]}")
