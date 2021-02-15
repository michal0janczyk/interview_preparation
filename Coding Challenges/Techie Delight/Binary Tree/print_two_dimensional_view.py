class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def printBinaryTree(root, space, height):
    if root is None:
        return
    # increase distance between levels
    space += height

    if root:
        printBinaryTree(root.left, space, height)
        print()
        for _ in range(height, space):
            print(" ", end=" ")
        print(root.data, end=" ")
        print()
        printBinaryTree(root.right, space, height)


if __name__ == "__main__":

    """ Construct the following tree
              1
            /   \
           /     \
          2       3
         / \     / \
        /   \   /   \
       4     5 6     7
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # print binary tree
    space = 0
    height = 10
    printBinaryTree(root, space, height)
