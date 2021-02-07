"""Linked List Structure
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

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


if __name__ == "__main__":
    llist = LinkedList()
    llist.append("A")
    llist.append("A")
    llist.append("B")
    llist.append("C")
    llist.append("C")
    llist.append("D")
    llist.prepend(1)
    llist.insert_after_node(llist.head.next, "E")
    llist.delete_node(1)
    llist.delete_node("E")
    print(llist)
    llist.delete_node_at_pos(0)
    llist.delete_node_at_pos(2)
    print(llist)
    print(
        "The length of the linked list calculated recursively after inserting 4 elements is:"
    )
    print(llist.len_recursive(llist.head))
    print(
        "The length of the linked list calculated iteratively after inserting 4 elements is:"
    )
    print(llist.len_iterative())
