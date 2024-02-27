from collections import defaultdict

class TraversalType:
    BF = 'BreadthFirst'
    DF = 'DeapthFirst'

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

    def traversal(self, source, traversal_type = TraversalType.DF):
        ds_for_traversal = [source] 
        visited = set()
        traversal = []
        while ds_for_traversal:
            vertex = ds_for_traversal.pop() if traversal_type == TraversalType.DF else ds_for_traversal.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)
                adjacency_list = (reversed(self.adjacency_list[vertex]) 
                                 if traversal_type == TraversalType.DF 
                                 else self.adjacency_list[vertex])
                for neighbour in adjacency_list:
                    if neighbour not in visited:
                        ds_for_traversal.append(neighbour)
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

    def has_path(self, source, dest, traversal_type=TraversalType.DF):
        ds_for_traversal = [(source, [source])]
        visited = set()
        while ds_for_traversal:
            vertex, path = ds_for_traversal.pop() if traversal_type == TraversalType.DF else ds_for_traversal.pop(0)
            if vertex == dest:
                print("Path from", source, "to", dest, ":", "->".join(map(str, path)))
                return True
            if vertex not in visited:
                visited.add(vertex)
                adjacency_list = (reversed(self.adjacency_list[vertex]) 
                                 if traversal_type == TraversalType.DF 
                                 else self.adjacency_list[vertex])                
                for neighbour in adjacency_list:
                    ds_for_traversal.append((neighbour, path + [neighbour]))
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
    print("DFS Traversal:", graph.traversal(0,TraversalType.DF))

    # Breadth First Search (BFS)
    print("BFS Traversal:", graph.bfs_traversal(0))
    print("BFS Traversal:", graph.traversal(0,TraversalType.BF))

    # Check if there is a path between two vertices using DFS
    print("Path between 0 and 3 exists (DFS)?", graph.has_path_stack_dfs(0, 3))
    print("Path between 0 and 4 exists (DFS)?", graph.has_path_stack_dfs(0, 4))
    print("Path between 5 and 4 exists (DFS)?", graph.has_path_stack_dfs(5, 4))

    print("Path between 0 and 3 exists (DFS)?", graph.has_path(0, 3, TraversalType.DF))
    print("Path between 0 and 4 exists (DFS)?", graph.has_path(0, 4, TraversalType.DF))
    print("Path between 5 and 4 exists (DFS)?", graph.has_path(5, 4, TraversalType.DF))
    
    # Check if there is a path between two vertices using BFS
    print("Path between 0 and 3 exists (BFS)?", graph.has_path_queue_bfs(0, 3))
    print("Path between 0 and 4 exists (BFS)?", graph.has_path_queue_bfs(0, 4))
    print("Path between 5 and 4 exists (BFS)?", graph.has_path_queue_bfs(5, 4))

    print("Path between 0 and 3 exists (DFS)?", graph.has_path(0, 3, TraversalType.BF))
    print("Path between 0 and 4 exists (DFS)?", graph.has_path(0, 4, TraversalType.BF))
    print("Path between 5 and 4 exists (DFS)?", graph.has_path(5, 4, TraversalType.BF))
    

if __name__ == "__main__":
    main()
