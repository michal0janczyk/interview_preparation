from collections import deque


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def print_nodes(root, start, end):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    level = 0

    while len(queue) > 0:
        size = len(queue)
        level += 1

        while size > 0:
            size -= 1
            node = queue.popleft()

            if start <= level <= end:
                print(node.data, end=" ")

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        if start <= level <= end:
            print()


if __name__ == "__main__":

    root = Node(15)
    root.left = Node(10)
    root.right = Node(20)
    root.left.left = Node(8)
    root.left.right = Node(12)
    root.right.left = Node(16)
    root.right.right = Node(25)
    root.right.right.right = Node(30)

    start = 2
    end = 3
    print_nodes(root, start, end)
