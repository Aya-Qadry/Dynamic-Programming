class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

    def bellman_ford(self, source):
        # Step 1: Initialize distances from source to all other vertices as INFINITE
        distances = [float('inf')] * self.V
        distances[source] = 0

        # Step 2: Relax all edges |V| - 1 times
        for _ in range(self.V - 1):
            for u, v, w in self.edges:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

        # Step 3: Check for negative-weight cycles
        for u, v, w in self.edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                print("Graph contains negative weight cycle")
                return None

        return distances

# Example usage
g = Graph(5)
g.add_edge(0, 1, -1)
g.add_edge(0, 2, 4)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(1, 4, 2)
g.add_edge(3, 2, 5)
g.add_edge(3, 1, 1)
g.add_edge(4, 3, -3)

distances = g.bellman_ford(0)

if distances:
    for i, d in enumerate(distances):
        print(f"Distance from source to vertex {i}: {d}")
