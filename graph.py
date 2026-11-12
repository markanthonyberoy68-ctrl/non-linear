from collections import deque


class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        if v not in self.adjacency[u]:
            self.adjacency[u].append(v)
        if u not in self.adjacency[v]:
            self.adjacency[v].append(u)

    def load_beroy(self):
        self.adjacency = {}
        for v in "BEROY":
            self.add_vertex(v)
        for u, v in [("B", "E"), ("B", "R"), ("E", "O"), ("R", "Y"), ("O", "Y")]:
            self.add_edge(u, v)

    def bfs(self, start):
        if start not in self.adjacency:
            return []
        visited = {start}
        queue = deque([start])
        result = []
        while queue:
            current = queue.popleft()
            result.append(current)
            for neighbor in self.adjacency[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start):
        if start not in self.adjacency:
            return []
        visited = set()
        result = []

        def explore(vertex):
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.adjacency[vertex]:
                if neighbor not in visited:
                    explore(neighbor)

        explore(start)
        return result

    def display(self):
        if not self.adjacency:
            print("Graph is empty.")
            return
        for vertex, neighbors in self.adjacency.items():
            print(f"{vertex}: {', '.join(neighbors) if neighbors else '-'}")


def main():
    graph = Graph()
    graph.load_beroy()
    while True:
        print("\n===== GRAPH (BEROY) =====")
        print("1. Load default BEROY graph")
        print("2. Add vertex")
        print("3. Add edge")
        print("4. Display adjacency list")
        print("5. BFS traversal")
        print("6. DFS traversal")
        print("0. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            graph.load_beroy()
            print("BEROY graph loaded.")
        elif choice == "2":
            v = input("Vertex: ").strip().upper()
            if v:
                graph.add_vertex(v[0])
        elif choice == "3":
            u = input("From vertex: ").strip().upper()
            v = input("To vertex: ").strip().upper()
            if u and v:
                graph.add_edge(u[0], v[0])
                print(f"Edge {u[0]} - {v[0]} added.")
        elif choice == "4":
            graph.display()
        elif choice == "5":
            start = input("Start vertex (default B): ").strip().upper() or "B"
            print("BFS:", " - ".join(graph.bfs(start[0])) or "Vertex not found.")
        elif choice == "6":
            start = input("Start vertex (default B): ").strip().upper() or "B"
            print("DFS:", " - ".join(graph.dfs(start[0])) or "Vertex not found.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()