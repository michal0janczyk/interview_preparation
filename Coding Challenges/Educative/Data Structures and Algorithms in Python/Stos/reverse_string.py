"""Reverse a string using a stack
"""

from stack import Stack


def rev_str(input_str):
    # sourcery skip: inline-immediately-returned-variable, list-comprehension
    stack = Stack()
    for char in input_str:
        stack.push(char)

    res = []
    for _ in range(stack.size()):
        res.append(stack.pop())
    return "".join(res)


def reverse_string(input_str):
    stack = Stack()
    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


if __name__ == "__main__":
    input_str = "Educative"
    print(input_str[::-1])
    print(rev_str((input_str)))
    print(reverse_string((input_str)))
