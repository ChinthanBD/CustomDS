from collections import defaultdict

class Graph:
    def __init__(self) -> None:
        self.adjacency_list = defaultdict(list)
    
    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)
        
    def dfs(self, source):
        stack = [source]
        visited = set()
        traversal = []
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                for neighbour in reversed(self.adjacency_list[vertex]):
                    if neighbour not in visited:
                        stack.append(neighbour)
        return traversal
    
    def bfs(self, source):
        queue = [source]
        visited = set()
        traversal = []
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                for neighbour in self.adjacency_list[vertex]:
                    if neighbour not in visited:
                        queue.append(neighbour)
        return traversal

def main():
    graph = Graph()

    # Adding edges
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)

    # Depth First Search (DFS)
    print("DFS Traversal:", graph.dfs(0))

    # Breadth First Search (BFS)
    print("BFS Traversal:", graph.bfs(0))

if __name__ == "__main__":
    main()
