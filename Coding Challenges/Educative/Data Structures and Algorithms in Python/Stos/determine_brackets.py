"""Determine if Brackets are Balanced
"""

from stack import Stack


def is_match(p1, p2):
    # sourcery skip: merge-duplicate-blocks, remove-redundant-if, return-identity
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):  # sourcery skip: return-identity
    stack = Stack()
    index = 0
    is_balanced = True

    while index < len(paren_string) and is_balanced:
        parent = paren_string[index]
        if parent in ["(", "[", "{"]:
            stack.push(parent)
        else:
            if stack.size() == 0:
                is_balanced = False
            else:
                top = stack.pop()
                if not is_match(top, parent):
                    is_balanced = False
        index += 1

    if stack.size() == 0 and is_balanced:
        return True
    else:
        return False


def equation_checker(equation):  # sourcery skip: none-compare, return-identity
    stack = Stack()

    for char in equation:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if stack.pop() is None:
                return False

    if stack.size() == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    print("Pass" if (equation_checker("((3^2 + 8)*(5/2))/(2+6)")) else "Fail")
    print(
        "Pass" if not (equation_checker("((3^2 + 8)*(5/2))/(2+6))")) else "Fail"
    )

    print("String : (((({})))) Balanced or not?")
    print(is_paren_balanced("(((({}))))"))

    print("String : [][]]] Balanced or not?")
    print(is_paren_balanced("[][]]]"))

    print("String : [][] Balanced or not?")
    print(is_paren_balanced("[][]"))
