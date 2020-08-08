import doctest

from collections import defaultdict, deque

class Graph(object):
    """
    A graph class that support DFS And BFS
    """
    def __init__(self, input_file=None, graph=None):
        self._edges_size = 0
        self._vertices_size = 0
        self._adj = defaultdict(list)
        # Handle file input graph construction
        if input_file is not None: return
        if graph:
            self._adj = copy.deepcopy(graph._adj)
            self._edges_size = graph.edges_size()
    
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
