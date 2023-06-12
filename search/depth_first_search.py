class DepthFirstSearch:

    """This search traverses a graph by visiting every vertex along a path before backtracking to the next available
     path."""

    def __init__(self, graph):
        self.graph = graph

    def search(self, start_vertex, visit_function):
        vertex_stack = [start_vertex]
        visited_set = set()

        while len(vertex_stack) > 0:
            current_vertex = vertex_stack.pop()
            if current_vertex not in visited_set:
                visit_function(current_vertex)
                visited_set.add(current_vertex)
                for adjacent_vertex in self.graph.adjacency_list[current_vertex]:
                    vertex_stack.append(adjacent_vertex)