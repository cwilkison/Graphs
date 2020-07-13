"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set() # this will hold edges

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vert")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()

        visited = set()

        q.enqueue(starting_vertex)

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                print(v)
                for neighbor in self.get_neighbors(v):
                    if neighbor not in visited:
                        q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()

        visited = set()

        s.push(starting_vertex)

        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                for neighbor in self.get_neighbors(v):
                    if neighbor not in visited:
                        s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # check to see if visited vertices is none
        if visited is None:
            # change it to a set
            visited = set()
        
        # print current starting vertex
        print(starting_vertex)
        # add starting vertex to visitd vertexs
        visited.add(starting_vertex)
        # call recursive function on neighbors of starting vertex
        for neighbor in self.get_neighbors(starting_vertex):
            # if the neighbor is not in the visited vertices
            if neighbor not in visited:
                # run dft_recursive again with neighbor as starting vertex
                self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create an empty Queue and begin with starting vertex
        q = Queue()
        q.enqueue([starting_vertex])
        # create a visited vertices set
        visited = set()

        # while the queue size has items
        while q.size() > 0:
            # dequeue first path
            path = q.dequeue()
            # take last vertex of path and check if visited
            if path[-1] not in visited:
                # if not visited check against destination vertex
                if path[-1] == destination_vertex:
                    # return path if true
                    return path
            #  otherwise add to visited set
            visited.add(path[-1])
            
            # add unvisited neighbors to queue
            for neighbor in self.get_neighbors(path[-1]):
                # duplicate the path
                new_path = list(path)
                # add neighbor
                new_path.append(neighbor)
                # add new path to queue
                q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create an empty Stack and begin with starting vertex
        s = Stack()
        s.push([starting_vertex])
        # create a visited vertices set
        visited = set()

        # while the stack size has items
        while s.size() > 0:
            # pop first vertex from Stach
            path = s.pop()
            # take last vertex of path and check if visited
            if path[-1] not in visited:
                # if not visited check against destination vertex
                if path[-1] == destination_vertex:
                    # return path if true
                    return path
            #  otherwise add to visited set
            visited.add(path[-1])
            
            # add unvisited neighbors to Stack
            for neighbor in self.get_neighbors(path[-1]):
                # duplicate the path
                new_path = list(path)
                # add neighbor
                new_path.append(neighbor)
                # add new path to queue
                s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()

        if path == None:
            path = []

        visited.add(starting_vertex)

        path = path + [starting_vertex]

        if starting_vertex == destination_vertex:
            return path
        
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                neighbor_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
            if neighbor_path is not None:
                return neighbor_path

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
