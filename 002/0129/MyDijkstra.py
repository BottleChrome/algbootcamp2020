class Graph:
    def __init__(self):
        self.node = set()
        self.edges = {}
        self.distances = {}
 
    def add_node(self, value):
        self.nodes.add(value)
 
    def add_edge(self, from_node, to_node, distance):
        self._add_edge(from_node, to_node, distance)
        self._add_edge(to_node, from_node, distance)
 
    def _add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, [])
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance
 
def dijkstra(graph, initial_node):
    visited = {initial_node: 0}
    path = {}
 
    nodes = set(graph.nodes)
 
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break
 
        nodes.remove(min_node)
        cur_wt = visited[min_node]
 
        for edge in graph.edges[min_node]:
            wt = cur_wt + graph.distances[(min_node, edge)]
            if edge not in visited or wt < visited[edge]:
                visited[edge] = wt
                path[edge] = min_node
    return visited, path
 
def shortest_path(graph, initial_node, goal_node):
    distance, path = dijkstra(graph, initial_node)
    route = [goal_node]
    while goal_node != initial_node:
        route.append(path[goal_node])
        goal_node = path[goal_node]
 
    route.reverse()
    return route
 
g = Graph()
n = 8
k = 14
g.nodes = set(range(1, k+1))
for _ in range(k):
  a,b, w = list(map(int, input().split())) 
  g.add_edge(a, b, w)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 7)
g.add_edge(2, 5, 4)
g.add_edge(2, 4, 5)
g.add_edge(3, 4, 1)
g.add_edge(4, 5, 2)
 
print(shortest_path(g, 1, 5))
print(shortest_path(g, 1, 4))