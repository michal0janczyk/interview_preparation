from Stack import MyStack


def evaluate_post_fix(exp):
    num_stack = MyStack()
    for i in exp:
        if i.isdigit():
            num_stack.push(i)
        else:
            a = num_stack.pop()
            b = num_stack.pop()
            eq = str(a) + str(i) + str(b)
            print(eq)
            res = eval(eq)
            print(res)
            print(a)
            print(i)
            print(b)
    print(num_stack)


def next_greater_element(lst):
    s = MyStack()
    res = [-1] * len(lst)
    print(res)

    for i in range(len(lst) - 1, -1, -1):
        print(i)
        if not s.is_empty():
            while not s.is_empty() and s.top() <= lst[i]:
                s.pop()

        if not s.is_empty():
            res[i] = s.top()

        s.push(lst[i])

    return res


next_greater_element([4, 6, 3, 2, 8, 1])

# expr = "921*-8-4+"
# evaluate_post_fix(expr)
# output 3
