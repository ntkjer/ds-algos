import doctest, sys, copy

from collections import defaultdict, deque

class Graph(object):
    """
    A graph class that support DFS And BFS
    """
    def __init__(self, input_file=None, graph=None):
        assert(not (input_file and graph)), "Can't create G from file AND another graph."
        self._edges_size = 0
        self._vertices_size = 0
        self._adj = defaultdict(list)
        if input_file:
            g = self._create_graph_from_file(input_file)
            self._adj = copy.deepcopy(g._adj)
            self._edges_size = g.edges_size()
        if graph:
            self._adj = copy.deepcopy(graph._adj)
            self._edges_size = graph.edges_size()

    def _create_graph_from_file(self, input_file=None):
        """
        Creates a graph from file input by reading each line. 
        Expects the header of the file to be the number of V and E in a graph, separated by \n.
        E.g $ cat foo.txt
        1
        1
        0 3
        \t 
        TODO: read sys.stdin as dummy f so we can pipe like cat foo.txt | python graph.py
        """
        if input_file is None: return
        with open(input_file) as f:
            v_size = int(f.readline())
            e_size = int(f.readline())
            g = Graph()
            g._vertices_size = v_size
            for line in f:
                l = line.split(' ')
                v, w = int(l[0]), int(l[1])
                g.add_edge(v, w)
        return g

    
    def __iter__(self):
        """ for x in self.Graph(v) -> [w0, w1, ..., wn]"""
        return iter(self._adj)


    def add_edge(self, v, w):
        """
        Adds edge from v -> w and w -> v in adjacanecy matrix.
        """
        self._adj[v].append(w)
        self._adj[w].append(v)
        self._edges_size += 1

    def edges_size(self):
        return self._edges_size
    
    def vertices_size(self):
        return len(self._adj.keys())

    def adj(self, v):
        return self._adj[v]

    def __repr__(self):
        s = str(self.vertices_size()) + ' vertices, ' + str(self.edges_size()) + ' edges\n'
        for k in self._adj:
            try:
                lst = ''.join([str(vertex) for vertex in self._adj[k]])
            except TypeError:
                lst = ''.join([str(vertex) for vertex in self._adj[k]])
            s += '{}: {}\n'.format(k, lst)
        return s


class DepthFirstPaths(object):
    
    def __init__(self, g : Graph, start_vertex : int):
        self._marked = defaultdict(bool)
        self._edge_to = {}
        self._start = start_vertex
        self.dfs(g, self._start)

    
    def dfs(self, g : Graph, vertex):
        self._marked[vertex] = True
        for w in g.adj(vertex):
            if not self._marked[w]:
                self._edge_to[w] = vertex
                self.dfs(g, w)


    def has_path_to(self, vertex):
        return self._marked[vertex]

    def path_to(self, vertex):
        if not self.has_path_to(vertex): return None
        path = []
        x, start = vertex, self._start
        while x != start:
            path.append(x)
            x = self._edge_to[x]
        path.append(start)
        return path

    def print_path_to(self, vertex):
        paths = self.path_to(vertex)
        if paths is None: return
        print("Path to: ", vertex)
        while paths:
            print(paths.pop())


class BreadthFirstPaths(object):

    def __init__(self, g : Graph, start_vertex : int):
        self._marked = defaultdict(bool)
        self._edge_to = {}
        self._start = start_vertex
        self.bfs(g, self._start)

    def bfs(self, g : Graph, s : int):
        self._marked[s]
        q = deque()
        q.append(s)
        while len(q) > 0:
            v = q.popleft()
            for w in g.adj(v):
                if not self._marked[w]:
                    self._edge_to[w] = v
                    self._marked[w] = True
                    q.append(w)

    def has_path_to(self, v):
        return self._marked[v]

    def path_to(self, v):
        if not self.has_path_to(v): return None
        path = []
        x, start = v, self._start
        while x != start:
            path.append(x)
            x = self._edge_to[x]
        path.append(start)
        return path

    def print_path_to(self, v):
        paths = self.path_to(v)
        if not paths: return
        print("Path to: ", v)
        while paths:
            print(paths.pop())
             

class ConnectedComponents(object):
    """ 
    An application of depth first search for the union find problem.

    """
    def __init__(self, g : Graph):
        self._marked = defaultdict(bool)
        self._id = {}
        self._count = 0
        s = 0
        while s < g.vertices_size():
            if not self._marked[s]:
                self.dfs(g, s)
                self._count += 1
            s += 1
    
    def dfs(self, graph : Graph, v):
        self._marked[v] = True
        self._id[v] = self.count()
        for w in g.adj(v):
            if not self._marked[w]: 
                self.dfs(g, w)

    def connected(self, v, w):
        return self.id(v) == self.id(w)

    def id(self, v):
        return self._id[v]

    def count(self):
        return self._count

class Cycle(object):

    HAS_CYCLE = True

    def __init__(self, g : Graph):
        self._marked = defaultdict(bool)
        self.HAS_CYCLE = not self.HAS_CYCLE
        s = 0
        while s < g.vertices_size():
            if not self._marked[s]:
                self.dfs(g, -1, s)
            s += 1
    
    def dfs(self, g: Graph, u, v):
        self._marked[v] = True
        for w in g.adj(v):
            if not self._marked[w]:
                self.dfs(g, v, w)
            else if w != u:
                self.HAS_CYCLE = True

    def has_cycle(self):
        return self.HAS_CYCLE

class Bipartite(object):
    
    IS_BIPARTITE = True

    def __init__(self, g : Graph):
        self._marked = defaultdict(bool)
        self._color = defaultdict(bool)
        self.IS_BIPARTITE = not self.IS_BIPARTITE
        s = 0
        while s < g.vertices_size():
            if not self._marked[s]:
                self.dfs(g, s)
            s += 1

    def dfs(self, g : Graph, v):
        self._marked[v] = True
        for w in g.adj(v):
            if not self._marked[w]:
                self._color[w] = not self._color[v]
                self.dfs(g, w)
            else if self._color[w] == self._color[v]:
                self.IS_BIPARTITE = False

    def is_bipartite(self):
        return self.IS_BIPARTITE 



if __name__ == '__main__':
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(4, 1)
    g.add_edge(1, 7)
    g.add_edge(8, 7)
    dfp = DepthFirstPaths(g, 4)
    dfp.print_path_to(8)

    bfp = BreadthFirstPaths(g, 4)
    bfp.print_path_to(8)
    print("creating from file") 
    g = Graph("../sample_data/tinyg.txt")
    print(g.vertices_size(), g.edges_size())
    

