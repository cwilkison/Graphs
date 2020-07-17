from graph import Graph
from util import Queue
def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    # creating graph
    for pair in ancestors:
        # checking each node to see if it already exists, if it is then add the vertex
        if pair[0] not in graph.vertices:
            graph.add_vertex(pair[0])
        if pair[1] not in graph.vertices:
            graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])
    q = Queue()
    longest_path = []
    # node_location = 0
    q.enqueue([starting_node])
    while q.size() > 0:
        deq = q.dequeue()
        if len(deq) > len(longest_path):
            longest_path = deq
        if len(deq) == len(longest_path):
            if deq[-1] < longest_path[-1]:
                longest_path = deq
        for neighbor in graph.get_neighbors(deq[-1]):
            temp_path = deq.copy()
            temp_path.append(neighbor)
            q.enqueue(temp_path)
    if len(longest_path) <= 1:
        return -1
    return longest_path[-1]