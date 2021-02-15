from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Queue node for storing a pointer to a tree node and its current depth
class qNode:
    def __init__(self, node=None, depth=None):
        self.node = node
        self.depth = depth


# Recursive function to find the minimum depth of a path starting
# from the given node in a binary tree
def min_depth_dfs(root):
    """Left -> Right -> root"""
    if root is None:
        return 0
    if root:
        left = min_depth_dfs(root.left)
        right = min_depth_dfs(root.right)
        # print(str(root.value) + "-", end="")
        # if the left child does not exist, consider the depth
        # returned by the right subtree
        if root.left is None:
            return 1 + right
        if root.right is None:
            return 1 + left

        return 1 + min(left, right)


def is_leaf(node):
    return node.left is None and node.right is None


# Iterative function to find the minimum depth of a path starting
# from the given node in a binary tree
def min_depth_bfs(root):
    if root is None:
        return 0
    q = deque()
    q.append(qNode(root, 1))
    while q:
        front = q.popleft()
        node = front.node
        depth = front.depth
        if is_leaf(node):
            return depth
        if node.left:
            q.append(qNode(node.left, depth + 1))
        if node.right:
            q.append(qNode(node.right, depth + 1))


if __name__ == "__main__":

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.left.right = Node(8)
    root.left.right.right = Node(9)
    root.right.right.left = Node(10)
    root.right.right.left = Node(11)
    root.left.left.right.right = Node(12)

    print("\nDFS - The minimum depth is", min_depth_dfs(root))
    print("\nBFS - The minimum depth is", min_depth_bfs(root))
