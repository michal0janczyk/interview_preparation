"""Binary Tree Implementaion
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

    # Search
    def search(self, find_val, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_search(tree.root, find_val)
        elif traversal_type == "inorder":
            return self.inorder_search(tree.root, find_val)
        elif traversal_type == "postorder":
            return self.postorder_search(tree.root, find_val)
        else:
            print("Traversal type " + str(traversal_type) + " not recognized.")
            return False

    def print_tree(self, traversal_type):
        # Recursive traversals
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        # Iterative traversals
        elif traversal_type == "levelorder":
            return self.levelorder_print()
        elif traversal_type == "reverseorder":
            return self.reverse_levelorder_print()
        elif traversal_type == "preorder_iterative":
            return self.preorder_iterative()
        elif traversal_type == "inorder_iterative":
            return self.inorder_iterative()
        elif traversal_type == "postorder_iterative":
            return self.postorder_iterative()

        else:
            print("Traversal type " + str(traversal_type) + " not recognized.")
            return False

    # Search
    def preorder_search(self, root, find_val):
        """Root->Left-Right"""
        if root:
            if root.value == find_val:
                return True
            else:
                return self.preorder_search(
                    root.left, find_val
                ) or self.preorder_search(root.right, find_val)
        return False

    def inorder_search(self, root, find_val):
        """Left->Root->Right"""
        pass

    def postorder_search(self, root, find_val):
        """Left->Root->Right"""
        pass

    # Recursive traversals
    def preorder_print(self, root, traversal):
        """Root -> Left -> Right"""
        if root:
            traversal += str(root.value) + "-"
            traversal = self.preorder_print(root.left, traversal)
            traversal = self.preorder_print(root.right, traversal)
        return traversal

    def inorder_print(self, root, traversal):
        """Left -> Root -> Right"""
        if root:
            traversal = self.inorder_print(root.left, traversal)
            traversal += str(root.value) + "-"
            traversal = self.inorder_print(root.right, traversal)
        return traversal

    def postorder_print(self, root, traversal):
        """Left -> Right -> Root"""
        if root:
            traversal = self.postorder_print(root.left, traversal)
            traversal = self.postorder_print(root.right, traversal)
            traversal += str(root.value) + "-"
        return traversal

    # Iterative traversals
    def levelorder_print(self):
        if self.root is None:
            return
        queue = Queue()
        queue.enqueue(self.root)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def reverse_levelorder_print(self):
        if self.root is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(self.root)
        traversal = ""

        while len(queue):
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

    def preorder_iterative(self):
        """Root -> Left -> Right"""
        stack = Stack()
        is_done = False
        current_node = self.root
        traversal = ""

        while not is_done:
            if current_node is not None:
                traversal += str(current_node.value) + "-"
                stack.push(current_node)
                current_node = current_node.left
            elif stack.size() > 0:
                current_node = stack.pop()
                current_node = current_node.right
            else:
                is_done = True
        return traversal

    def inorder_iterative(self):
        """Left -> Root -> Right"""
        stack = Stack()
        is_done = False
        current_node = self.root
        traversal = ""

        while not is_done:
            if current_node is not None:
                stack.push(current_node)
                current_node = current_node.left
            elif stack.size() > 0:
                current_node = stack.pop()
                traversal += str(current_node.value) + "-"
                current_node = current_node.right
            else:
                is_done = True
        return traversal

    def postorder_iterative(self):
        """Left -> Right -> Root"""
        stack = Stack()
        is_done = False
        current_node = self.root
        traversal = ""

        while not is_done:
            while current_node is not None:
                stack.push(current_node)
                stack.push(current_node)
                current_node = current_node.left

            if len(stack) == 0:
                is_done = True
                return traversal

            current_node = stack.pop()
            if len(stack) > 0 and stack.peek() == current_node.value:
                current_node = current_node.right
            else:
                traversal += str(current_node.value) + "-"
                current_node = None

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_hight = self.height(node.right)
        return 1 + max(left_height, right_hight)

    def size_iterative(self):
        if self.root is None:
            return False

        stack = Stack()
        stack.push(self.root)
        size_counter = 0
        while stack.size() > 0:
            node = stack.pop()
            size_counter += 1
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)
        return size_counter

    def size_recursive(self, root):
        if root is None:
            return 0
        return (
            1 + self.size_recursive(root.left) + self.size_recursive(root.right)
        )

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_helper(self.root, data)

    def insert_helper(self, current_node, data):
        if current_node.value > data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self.insert_helper(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self.insert_helper(current_node.right, data)

    def is_identical_recursive(self, fst_tree, snd_tree):
        if fst_tree is None and snd_tree is None:
            return True

        return (
            (fst_tree and snd_tree)
            and (fst_tree.value == snd_tree.value)
            and self.is_identical_recursive(fst_tree.left, snd_tree.left)
            and self.is_identical_recursive(fst_tree.right, snd_tree.right)
        )

    def is_identical_iterative(self, fst_tree, snd_tree):
        if fst_tree is None and snd_tree is None:
            return True
        if fst_tree is None:
            return False
        if snd_tree is None:
            return False
        stack = Stack()
        stack.push((fst_tree.value, snd_tree.value))

        while stack.size() > 0:
            fst_curr_node, snd_curr_node = stack.pop()

            if fst_curr_node == snd_curr_node:
                return False

            if fst_curr_node.left and snd_curr_node.left:
                stack.push((fst_curr_node.left, snd_curr_node.left))
            elif fst_curr_node.left or snd_curr_node.left:
                return False

            if fst_curr_node.right and snd_curr_node.right:
                stack.push((fst_curr_node.right, snd_curr_node.right))
            elif fst_curr_node.right or snd_curr_node.right:
                return False
        return True

    def spiral_level_right_to_left(self, root, level):
        if root is None:
            return
        traversal = ""
        if level == 1:
            traversal += str(root.value) + "-"
            return True
        left = self.spiral_level_right_to_left(root.left, level - 1)
        right = self.spiral_level_right_to_left(root.right, level - 1)

        return traversal and left or traversal and right

    def spiral_level_left_to_right(self, root, level):
        if root is None:
            return
        traversal = ""
        if level == 1:
            traversal += str(root.value) + "-"
            return True
        left = self.spiral_level_left_to_right(root.left, level - 1)
        right = self.spiral_level_left_to_right(root.right, level - 1)

        return traversal and left or traversal and right

    def spiral_order_traversal(self):
        if self.root is None:
            return
        level = 1
        is_done = False
        while not is_done:
            is_done = self.spiral_level_left_to_right(self.root, level)
            level += 1
            if is_done:
                is_done = self.spiral_level_right_to_left(self.root, level)
                level += 1


# Calculate size of binary tree:
#     1
#    / \
#   2  3
#  / \
# 4  5

if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.insert(16)

    # Search
    print("\tBinary Tree")
    print("Searchs")
    print("\tPre-Order-Search: {0}".format(tree.search(3, "preorder")))
    print("\tIn-Order-Search: {0}".format(tree.search(3, "inorder")))
    print("\tPost-Order-Search: {0}".format(tree.search(3, "postorder")))
    # Traversal
    print("Recursive Traversals")
    print("\tPre-Order: {0}".format(tree.print_tree("preorder")))
    print("\tIn-Order: {0}".format(tree.print_tree("inorder")))
    print("\tPost-Order: {0}".format(tree.print_tree("postorder")))

    print("Iterative Traversals")
    print("\tLevel-Order: {0}".format(tree.print_tree("levelorder")))
    print("\tReverse-Order: {0}".format(tree.print_tree("reverseorder")))
    print("\tPre-Order: {0}".format(tree.print_tree("preorder_iterative")))
    print("\tIn-Order: {0}".format(tree.print_tree("inorder_iterative")))
    print("\tPost-Order: {0}".format(tree.print_tree("postorder_iterative")))

    print("Height")
    print("\tTree Height: {0}".format(tree.height(tree.root)))

    print("Size")
    print("\tSize Iterative: {0}".format(tree.size_iterative()))
    print("\tSize Recursive: {0}".format(tree.size_recursive(tree.root)))

    # construct the first tree
    tree_first = BinaryTree(1)
    tree_first.root.left = Node(2)
    tree_first.root.right = Node(3)
    tree_first.root.left.left = Node(4)
    tree_first.root.left.right = Node(5)
    # construct the first tree
    tree_second = BinaryTree(1)
    tree_second.root.left = Node(2)
    tree_second.root.right = Node(3)
    tree_second.root.left.left = Node(4)
    tree_second.root.left.right = Node(5)

    if tree.is_identical_recursive(tree_first.root, tree_second.root):
        print("The given binary trees are IDENTICAL - recursive")
    else:
        print("The given binary trees are NOT IDENTICAL - recursive")

    if tree.is_identical_iterative(tree_first.root, tree_second.root):
        print("The given binary trees are IDENTICAL - iterative")
    else:
        print("The given binary trees are NOT IDENTICAL - iterative")
