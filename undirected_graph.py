from directed_graph import DirectedGraph
from typing_extensions import overrides

class UndirectedGraph(DirectedGraph):
    @overrides
    def add_edge(self, u, v):
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)

def main():
    graph = UndirectedGraph()

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

