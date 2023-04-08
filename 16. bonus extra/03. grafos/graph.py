class Graph:
    def __init__(self, num_vertices):
        # Initialize the graph with the given number of vertices
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v, weight=1):
        # Add a directed edge from vertex u to vertex v with the given weight
        self.adj_list[u].append((v, weight))

    def get_adjacent_vertices(self, u):
        # Return a list of tuples (v, w) representing the edges from vertex u to its
        # adjacent vertices v, with weights w
        return self.adj_list[u]

    def get_indegree(self, u):
        # Return the indegree of vertex u (i.e., the number of edges pointing to it)
        indegree = 0
        for v in range(self.num_vertices):
            for (adj_v, _) in self.adj_list[v]:
                if adj_v == u:
                    indegree += 1
        return indegree

    def get_edge_weight(self, u, v):
        # Return the weight of the edge from vertex u to vertex v
        for (adj_v, weight) in self.adj_list[u]:
            if adj_v == v:
                return weight
        return None

    def set_edge_weight(self, u, v, weight):
        # Set the weight of the edge from vertex u to vertex v
        for (i, (adj_v, _)) in enumerate(self.adj_list[u]):
            if adj_v == v:
                self.adj_list[u][i] = (adj_v, weight)
                return
        self.adj_list[u].append((v, weight))


# Create a new graph with 4 vertices
g = Graph(4)

# Add some edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

# Print the adjacency list for each vertex
for i in range(4):
    print(f"Vertex {i}: {g.get_adjacent_vertices(i)}")

# Print the indegree of each vertex
for i in range(4):
    print(f"Indegree of vertex {i}: {g.get_indegree(i)}")

# Set the weight of the edge (0, 2) to 10
g.set_edge_weight(0, 2, 10)

# Print the weight of the edge (0, 2)
print(f"Weight of edge(0, 2): {g.get_edge_weight(0, 2)}")
