"""Binary Trees and their implementation in Python
"""

from queue import Queue
from stack import Stack


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "reverseorder":
            return self.reverse_levelorder_print(tree.root)
        else:
            print(
                "Traversal type " + str(traversal_type) + " is not supported."
            )
            return False

    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += str(start.value) + "-"
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += str(start.value) + "-"
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += str(start.value) + "-"
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return

        stack = Stack()
        queue = Queue()
        queue.enqueue(start)
        traversal = ""

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        while stack.size() > 0:
            traversal += str(stack.peek()) + "-"
            stack.pop()

        return traversal

    def height(self, start):
        if start is None:
            return -1
        left_height = self.height(start.left)
        right_height = self.height(start.right)
        return 1 + max(left_height, right_height)

    def size(self):
        if self.root is None:
            return

        stack = Stack()
        stack.push(self.root)
        size = 1

        while stack.size() > 0:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

    def size_(self, node):
        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)


if __name__ == "__main__":
    #               1
    #           /       \
    #          2          3
    #         /  \      /   \
    #        4    5     6   7

    # Set up tree:
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print("Pre-Order: {0}".format(tree.print_tree("preorder")))
    print("In-Order: {0}".format(tree.print_tree("inorder")))
    print("Post-Order: {0}".format(tree.print_tree("postorder")))
    print("Level-Order: {0}".format(tree.print_tree("levelorder")))
    print("Reverse-Order: {0}".format(tree.print_tree("reverseorder")))
    print(tree.height(tree.root))
    print(tree.size())
