class Graph:
    """The graph represents a set of vertices connected in some way via edges to represent a relationship."""

    def __init__(self):
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []

    def add_directed_edge(self, from_vertex, to_vertex, weight=1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undirected_edge(self, vertex_a, vertex_b, weight=1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)

    def get_vertex(self, vertex_label):
        for vertex in self.adjacency_list:
            if vertex.label == vertex_label:
                return vertex
        return None

    def dijkstra_shortest_path(self, start_vertex):
        unvisited_queue = []
        for current_vertex in self.adjacency_list:
            unvisited_queue.append(current_vertex)

        start_vertex.distance = 0

        while len(unvisited_queue) > 0:
            smallest_index = 0
            for i in range(1, len(unvisited_queue)):
                if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                    smallest_index = i
            current_vertex = unvisited_queue.pop(smallest_index)

            for adj_vertex in self.adjacency_list[current_vertex]:
                edge_weight = self.edge_weights[(current_vertex, adj_vertex)]
                alternative_path_distance = current_vertex.distance + edge_weight

                if alternative_path_distance < adj_vertex.distance:
                    adj_vertex.distance = alternative_path_distance
                    adj_vertex.pred_vertex = current_vertex

    def get_shortest_path(self, start_vertex, end_vertex):
        path = ""
        current_vertex = end_vertex
        while current_vertex is not start_vertex:
            path = " -> " + str(current_vertex.label) + path
            current_vertex = current_vertex.pred_vertex
        path = start_vertex.label + path
        return path


class Vertex:
    """The node class for the graph implementation"""

    def __init__(self, label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None

    def __str__(self):
        return str(self.label)
