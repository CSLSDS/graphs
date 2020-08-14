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
        # TODO check functionality
        self.vertices[vertex_id] = set()

    def isvertex(self, vertex):
        return vertex in self.vertices

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # TODO check functionality
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            return

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO check functionality
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # TODO check functionality
        # create empty queue
        q = Queue()
        # add starting vertex id
        q.enqueue(starting_vertex)
        # create set for visited visited
        visited = set()
        # while q is not empty
        while q.size() > 0:
            # dequeue a vert (dft uses stack)
            v = q.dequeue()
            # if not visd, 
            if v not in visited:
                # mark as visd
                visited.add(v)
                # add all neighs to q
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO check functionality
        # create empty stack
        stack = Stack()
        # add starting vertex id
        stack.push(starting_vertex)
        # create set for visited visited
        visited = set()
        # while q is not empty
        while stack.size() > 0:
            # pop a vert 
            v = stack.pop()
            # if not visd, 
            if v not in visited:
                # mark as visd
                visited.add(v)
                # add all neighs to q
                for neighbor in self.get_neighbors(v):
                    stack.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # TODO
        visited.append(starting_vertex)
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
        return visited
                

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        path = [starting_vertex]
        q.enqueue(path)
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            dqpath = q.dequeue()
            # Grab the last vertex from the PATH
            v = dqpath[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # CHECK IF IT'S THE TARGET
                if v == destination_vertex:
                  # IF SO, RETURN PATH
                    return dqpath
                # Mark it as visited...
                visited.add(v)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    npath = dqpath.copy()
                    npath.append(neighbor)
                    q.enqueue(npath)
                  # COPY THE PATH
                  # APPEND THE NEIGHBOR TO THE BACK
                ''' Valid BFS path: [1, 2, 4, 6] '''

    def dfs(self, starting_vertex):
        """ MODIFIED TO GET ANCESTOR
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack and push A PATH TO the starting vertex ID
        stack = Stack()
        path = [starting_vertex]
        stack.push(path)
        # Create a Set to store visited vertices
        visited = set()
        paths = []
        # While the STACK is not empty...
        while stack.size() > 0:
            # pop the first PATH
            poppath = stack.pop()
            # Grab the last vertex from the PATH
            v = poppath[-1]
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited...
                visited.add(v)
                if len(self.vertices[v]) == 0:
                    paths.append(poppath)
                for nextv in self.vertices[v]:
                    if nextv not in visited:
                        new = poppath.copy()
                        new.append(nextv)
                        stack.push(new)

        longest = float('-inf')
        ancestor = float('inf')
#        longest = 0
#        ancestor = -1
        for path in paths:
            if len(path) > longest:
                # check for and assign longest path(s)
                longest = len(path)
                ancestor = path[-1]
            if len(path) == longest:
                # check which is lower to break ties
                ancestor = min(ancestor, path[-1])
        if ancestor == starting_vertex:
            ancestor = -1
        return ancestor

                
    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # TODO
        # first iteration only as setup
        if visited == None:
            visited = set()
        if path == None:
            path = []
        # initialize starting values (recursable)
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        # check for end condition
        if starting_vertex == destination_vertex:
            return path
        # else loop over neighbors/possible paths
        for neighbor in self.get_neighbors(starting_vertex):
            if neighbor not in visited:
                npath = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if npath: # why do i have to do this part
                    return npath
        # if no path
        return None
    ''' Valid DFS [1, 2, 4, 6], [1, 2, 4, 7, 6]'''

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
    print(f'graph.vertices {graph.vertices}')

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
    print(f'graph.bfs {graph.bfs(1, 6)}')

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(f'graph.dfs {graph.dfs(1, 6)}')
    print(f'graph.dfs_recursive {graph.dfs_recursive(1, 6)}')
