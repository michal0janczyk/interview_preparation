"""Linked List Structure
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def __str__(self):
        res = ""
        ptr = self.head

        while ptr:
            res += str(ptr.data) + ", "
            ptr = ptr.next

        res = res.strip(", ")

        if len(res):
            return "[" + res + "]"
        else:
            return "[]"

    def print_list(self):
        current_node = self.head
        while current_node:
            print("{0}".format(current_node.data))
            current_node = current_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        new_node.next = current_node
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node does not exist!")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

        prev_node = None
        while current_node and current_node.data != key:
            prev_node = current_node
            current_node = current_node.next

        if current_node is None:
            return
        prev_node.next = current_node.next
        current_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            current_node = self.head
            if pos == 0:
                self.head = current_node.next
                current_node = None
                return
            prev_node = None
            count = 0
            while current_node and count != pos:
                prev_node = current_node
                current_node = current_node.next
                count += 1

            if current_node is None:
                return
            prev_node.next = current_node.next
            current_node = None

    def len_iterative(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next

        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = curr_2
            curr_2 = curr_2.next

        if not curr_1 or not curr_2:
            return

        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2

        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1

        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        current_node = self.head
        prev_node = None

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node


if __name__ == "__main__":
    # Create Linked List
    llist = LinkedList()
    # Append
    llist.append("A")
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("C")
    llist.append("D")
    print("Append: {0}".format(llist))
    # Prepend
    llist.prepend(1)
    print("Prepend: {0}".format(llist))
    # Insert Node After
    llist.insert_after_node(llist.head.next, "E")
    print("Insert Node After: {0}".format(llist))
    # Delete Node
    llist.delete_node(1)
    llist.delete_node("E")
    print("Delete Node by Value: {0}".format(llist))
    # Delete Node at Particilar Position
    llist.delete_node_at_pos(0)
    llist.delete_node_at_pos(2)
    print("Delete Node at Particilar Position: {0}".format(llist))
    # Lenght of Linked List
    print(
        "The length of the linked list calculated recursively after inserting ",
        "4 elements is: {0}".format(llist.len_recursive(llist.head)),
    )
    print(
        "The length of the linked list calculated iteratively after inserting ",
        "4 elements is: {0}".format(llist.len_iterative()),
    )
    # Swap Linked List Nodes
    llist.swap_nodes("B", "C")
    print("Swapping nodes B and C that are not head nodes: {0}".format(llist))
    llist.swap_nodes("A", "B")
    print("Swapping nodes A and B where key_1 is head node: {0}".format(llist))
    llist.swap_nodes("D", "B")
    print("Swapping nodes D and B where key_2 is head node: {0}".format(llist))
    llist.swap_nodes("C", "C")
    print("Swapping nodes C and C where both keys are same: {0}".format(llist))
    # Revers Linked List
    llist.reverse_iterative()
    print("Reverse a singly linked list in an iterative way: {0}".format(llist))
