"""Convert Decimal Integer to Binary
"""

from stack import Stack


def convert_int_to_bin(dec_num):
    stack = Stack()

    if dec_num == 0:
        return 0

    while dec_num > 0:
        rest = dec_num % 2
        stack.push(rest)
        dec_num = dec_num // 2

    bin_num = ""
    while stack.size() > 0:
        bin_num += str(stack.pop())
    return bin_num


if __name__ == "__main__":
    print(convert_int_to_bin(100000))
    print(convert_int_to_bin(56))
    print(convert_int_to_bin(2))
    print(convert_int_to_bin(32))
    print(convert_int_to_bin(10))
