"""Binary Tree Implementaion
"""

from collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def inorder_traversal(self, root):
        """Left -> Root -> Right"""
        if root:
            self.inorder_traversal(root.left)
            print(str(root.value) + "-", end="")
            self.inorder_traversal(root.right)

    def postorder_traversal(self, root):
        """Left -> Right -> Root"""
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(str(root.value) + "-", end="")

    def is_leaf(self, root):
        return root.left is None and root.right is None

    def process(self, op, x, y):
        if op == "+":
            return x + y
        if op == "-":
            return x - y
        if op == "*":
            return x * y
        if op == "/":
            return x / y

    def evaluate_tree(self, root):
        if root is None:
            return
        if self.is_leaf(root):
            return int(root.value)

        left = self.evaluate_tree(root.left)
        right = self.evaluate_tree(root.right)
        return self.process(root.value, left, right)

    def get_height(self, root, size=0):
        if root is None:
            return 0, size
        size += 1
        left, size = self.get_height(root.left, size)
        right, size = self.get_height(root.right, size)
        return 1 + max(left, right), size

    def is_skewed_tree(self, root):
        height, size = self.get_height(root)
        return height == size


def is_operator(elem):
    return elem in ["+", "-", "×", "/", "^"]


def construct(postfix, root):
    stack = deque()
    for elem in postfix:
        if is_operator(elem):
            x = stack.pop()
            y = stack.pop()
            node = Node(elem, y, x)
            stack.append(node)
        else:
            stack.append(Node(elem))

    return stack[-1]


# Tree example
#       +
#      / \
#     *   /
#    / \  / \
#   -  5 21  7
#  /    \
# 10    5

if __name__ == "__main__":
    tree = BinaryTree("+")
    tree.root.left = Node("*")
    tree.root.right = Node("/")
    tree.root.left.left = Node("-")
    tree.root.left.right = Node(5)
    tree.root.left.left.left = Node(10)
    tree.root.left.left.right = Node(5)
    tree.root.right.left = Node(21)
    tree.root.right.right = Node(7)
    # tree = BinaryTree(1)
    # tree.root.left = Node(2)
    # tree.root.right = Node(3)
    # tree.root.left.left = Node(4)
    # tree.root.left.right = Node(5)

    print("Inorder: ")
    print(tree.inorder_traversal(tree.root))
    print("Postorder: ")
    print(tree.postorder_traversal(tree.root))
    print("Evaluate Tree:")
    print(tree.evaluate_tree(tree.root))
    root = BinaryTree(15)
    root.right = Node(30)
    root.right.left = Node(25)
    root.right.left.left = Node(18)
    root.right.left.left.right = Node(20)

    isSkewed_tree = tree.is_skewed_tree(tree.root)
    if isSkewed_tree:
        print("The binary tree is skewed")
    else:
        print("The binary tree is NOT skewed")

    isSkewed_root = tree.is_skewed_tree(root.root)
    if isSkewed_root:
        print("The binary tree is skewed")
    else:
        print("The binary tree is NOT skewed")

    postfix = "ab+cde+××"
    # infix = "((a+b)*(c*(d+e)))"
    root = BinaryTree(None)
    print(construct(postfix, root))

    # print("Postfix Expression\t: ", end="")
    # postorder(root)

    # print("\nInfix Expression\t: ", end="")
    # inorder(root)
