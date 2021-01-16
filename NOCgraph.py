# graph core&link placement
import math
from collections import namedtuple
Edge = namedtuple('Edge', ['vertex', 'weight'])

class GraphUndirectedWeighted(object):  
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, source, dest, weight):
        self.adjacency_list[source].append(Edge(dest, weight))
        self.adjacency_list[dest].append(Edge(source, weight))

    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v

def dist(a , b):
    d = (a[0] -b[0])**2 + (a[1] -b[1])**2 
    d = math.sqrt(d)
    d = math.ceil(d)
    return d

def create_graph(design):
    g = GraphUndirectedWeighted(1000)
    for r in range(64):
        b = design[r]
        for n in design[r].Neighbours:
            nxt = core_location(design,n)
            distance = dist(b.Position, nxt.Position)
            g.add_edge(b.Id,nxt.Id,distance)
    return g

def core_location(design , v_pos):
    for i in design:
        if i.Position == v_pos:
            return i
    print("Unknown core")