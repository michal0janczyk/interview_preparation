"""Stack Data Structure
"""


class Stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.size() == 0:
            return None
        else:
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def get_stack(self):
        return self.items


if __name__ == "__main__":
    stack = Stack()
    stack.push("M")
    stack.push("O")
    stack.push("N")
    stack.push("I")
    stack.push("Q")
    print(stack.get_stack())
