from collections import defaultdict


class DirectedGraph:
    def __init__(self) -> None:
        self.adjacency_list = defaultdict(list)
    
    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        
    def dfs_traversal(self, source):
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
    
    def bfs_traversal(self, source):
        queue = [(source, [source])]
        visited = set()
        traversal = []
        while queue:
            vertex, path = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                for neighbour in self.adjacency_list[vertex]:
                    if neighbour not in visited:
                        queue.append((neighbour, path + [neighbour]))
        return traversal

    def has_path_stack_dfs(self, source, dest):
        stack = [(source, [source])]
        visited = set()
        while stack:
            vertex, path = stack.pop()
            if vertex == dest:
                print("Path from", source, "to", dest, ":", "->".join(map(str, path)))
                return True
            else:
                if vertex not in visited:
                    visited.add(vertex)
                    for neighbour in reversed(self.adjacency_list[vertex]):
                        stack.append((neighbour, path + [neighbour]))
        print("No path from", source, "to", dest)
        return False

    def has_path_queue_bfs(self, source, dest):
        queue = [(source, [source])]
        visited = set()
        while queue:
            vertex, path = queue.pop(0)
            if vertex == dest:
                print("Path from", source, "to", dest, ":", "->".join(map(str, path)))
                return True
            if vertex not in visited:
                visited.add(vertex)
                for neighbour in self.adjacency_list[vertex]:
                    queue.append((neighbour, path + [neighbour]))
        print("No path from", source, "to", dest)
        return False

    
def main():
    graph = DirectedGraph()

    # Adding edges
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)

    # Depth First Search (DFS)
    print("DFS Traversal:", graph.dfs_traversal(0))

    # Breadth First Search (BFS)
    print("BFS Traversal:", graph.bfs_traversal(0))

    # Check if there is a path between two vertices using DFS
    print("Path between 0 and 3 exists (DFS)?", graph.has_path_stack_dfs(0, 3))
    print("Path between 0 and 4 exists (DFS)?", graph.has_path_stack_dfs(0, 4))
    print("Path between 5 and 4 exists (DFS)?", graph.has_path_stack_dfs(5, 4))

    # Check if there is a path between two vertices using BFS
    print("Path between 0 and 3 exists (BFS)?", graph.has_path_queue_bfs(0, 3))
    print("Path between 0 and 4 exists (BFS)?", graph.has_path_queue_bfs(0, 4))
    print("Path between 5 and 4 exists (BFS)?", graph.has_path_queue_bfs(5, 4))

if __name__ == "__main__":
    main()
