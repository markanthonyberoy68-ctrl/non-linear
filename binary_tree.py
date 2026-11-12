from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current.left is None:
                current.left = new_node
                return
            queue.append(current.left)
            if current.right is None:
                current.right = new_node
                return
            queue.append(current.right)

    def bfs(self):
        result = []
        if self.root is None:
            return result
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            result.append(current.data)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def dfs(self):
        result = []

        def visit(node):
            if node is None:
                return
            result.append(node.data)
            visit(node.left)
            visit(node.right)

        visit(self.root)
        return result

    def display(self):
        if self.root is None:
            print("Tree is empty.")
            return
        queue = deque([(self.root, 0)])
        current_level = -1
        while queue:
            node, level = queue.popleft()
            if level != current_level:
                current_level = level
                print(f"\nLevel {level}: ", end="")
            print(node.data, end="  ")
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        print()


def main():
    tree = BinaryTree()
    while True:
        print("\n===== BINARY TREE (BEROY) =====")
        print("1. Build tree from a name (default: BEROY)")
        print("2. Insert a letter")
        print("3. Display tree")
        print("4. BFS traversal")
        print("5. DFS traversal")
        print("0. Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            name = input("Enter name (press Enter for BEROY): ").strip().upper() or "BEROY"
            tree = BinaryTree()
            for letter in name:
                tree.insert(letter)
            print(f"Tree built from {name}.")
        elif choice == "2":
            letter = input("Letter to insert: ").strip().upper()
            if letter:
                tree.insert(letter[0])
                print(f"Inserted {letter[0]}.")
        elif choice == "3":
            tree.display()
        elif choice == "4":
            print("BFS:", " - ".join(tree.bfs()) or "Tree is empty.")
        elif choice == "5":
            print("DFS:", " - ".join(tree.dfs()) or "Tree is empty.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()