import sys

sys.path.append("../graph")

from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for link in ancestors:
        if not graph.isvertex(link[0]):# not in graph.vertices:
            graph.add_vertex(link[0])
        if not graph.isvertex(link[1]):#  not in graph.vertices:
            graph.add_vertex(link[0])
        graph.add_edge(link[0], link[1])
    return graph.dfs(starting_node)
    # if ll == None:
    #     ll = LinkedList()
    #     for pair in ancestors:
    #         pair = Node(pair)
    #         ll.insert_at_head(pair)
    # print(ll)
    # for node in ll:
    #     if node[1] == starting_node:
    #         return earliest_ancestor(ancestors, node, ll)

    #     # if pair describes startnode as a child, recurse with parent
    #     if pair[1] == starting_node: # child in question
    #         tbr = earliest_ancestor(ancestors, pair[0])
    #         if tbr:
    #             return tbr
    # return None



    # g = Graph()
    # for pair in ancestors:
    #     parent, child = [node for node in pair]
    #     g.add_vertex(child)
    #     g.add_vertex(parent)
    #     g.add_edge(child, parent)
        
    #     q = Queue()
    #     visited = set()
    #     # initialize possible paths
    #     q.enqueue([starting_node])
    #     # actually searching for longest path; initialize
    #     longest = 1
    #     earliest = -1
    #     while q.size() > 0:
    #         path = q.dequeue()
    #         parent = path[-1]
    #         if (len(path) > longest):
    #             earliest = parent
    #             longest = len(path)
    #         for neighbor in g.vertices[parent]:
    #             nextpath = path.append(neighbor)
    #             q.enqueue(nextpath)
    #     return earliest

    #     s.push(starting_node)
    #     current = starting_node
    #     while s.size():
    #         node = s.pop()
    #         if node not in visited:
    #             if s.size() and g.vertices.get(node) == set():
    #                 farther = s.pop()
    #                 if farther < node:
    #                     node = farther
    #             current = node
    #             visited.add(node)
    #         for relative in g.vertices[node]:
    #             if relative not in visited:
    #                 s.push(relative)
    #     return current


