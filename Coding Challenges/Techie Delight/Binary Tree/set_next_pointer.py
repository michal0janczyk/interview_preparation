# A class to store a binary tree node
class Node:
    def __init__(self, data, left=None, right=None, next=None):
        self.data = data
        self.left = left
        self.right = right
        self.next = next


# Function to set the next pointer of all nodes in a binary tree.
# `curr` —> current node
# `prev` —> previously processed node
def setNextNode(curr, prev):

    # return if the tree is empty
    if curr is None:
        return prev

    # recur for the left subtree
    prev = setNextNode(curr.left, prev)

    # set the previous node's next pointer to the current node
    if prev:
        prev.next = curr

    # update the previous node to the current node
    prev = curr

    # recur for the right subtree
    return setNextNode(curr.right, prev)


# Function to print inorder successor of all nodes of
# binary tree using the next pointer
def inorderSuccessor(curr):

    prev = None

    # set next pointer of all nodes
    setNextNode(curr, prev)

    # go to the leftmost node
    curr = curr.left.left

    # print inorder successor of all nodes
    while curr.next:
        print("The inorder successor of", curr.data, "is", curr.next.data)
        curr = curr.next


if __name__ == "__main__":

    """ Construct the following tree
              1
            /   \
           /     \
          2       3
         /      /  \
        /      /    \
       4      5      6
             / \
            /   \
           7     8
    """

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    inorderSuccessor(root)
