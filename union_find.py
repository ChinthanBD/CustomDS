class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1


# Example usage:
# Create a UnionFind object with 5 elements
uf = UnionFind(5)

# Perform some union operations
uf.union(0, 1)
uf.union(2, 3)
uf.union(0, 4)

# Find the set that an element belongs to
print(uf.find(0))  # Output: 0 (since 0 and 1 are in the same set)
print(uf.find(2))  # Output: 2 (since 2 and 3 are in the same set)
print(uf.find(4))  # Output: 0 (since 0 and 4 are in the same set)
