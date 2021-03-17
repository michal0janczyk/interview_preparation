# A linked list node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Function to print given linked list
def printList(head):
    ptr = head
    while ptr is not None:
        print(ptr.data, end=" -> ")
        ptr = ptr.next

    print("None")


# Function to construct a linked list from given set of keys
def constructList(keys):
    head = None

    # start from end of the list
    for i in reversed(range(len(keys))):
        # Allocate the in the heap and set its data
        head = Node(keys[i], head)

    return head


# Linked List Implementation in Python
if __name__ == "__main__":
    # input keys
    keys = [1, 2, 3, 4]

    # points to the head node of the linked list
    head = constructList(keys)

    # print linked list
    printList(head)
