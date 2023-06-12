class BreadthFirstSearch:

    """This search algorithm traverses a graph by exploring all adjacent vertices before moving to the next closest."""

    def __init__(self, graph):
        self.graph = graph

    def search(self, start_vertex, distances=dict()):
        discovered_set = set()
        frontier_queue = []
        visited_list = []

        distances[start_vertex] = 0

        frontier_queue.append(start_vertex)
        discovered_set.add(start_vertex)

        while len(frontier_queue) != 0:
            current_vertex = frontier_queue.pop(0)
            visited_list.append(current_vertex)
            for adjacent_vertex in self.graph.adjacency_list[current_vertex]:
                if adjacent_vertex not in discovered_set:
                    frontier_queue.append(adjacent_vertex)
                    discovered_set.add(adjacent_vertex)
                    distances[adjacent_vertex] = distances[current_vertex] + 1
        return visited_list

