def push(stack, value):
    stack.append(value)


def pop_item_stack(stack):
    if not stack:
        print("\nStack is Empty")
        return None

    return stack.pop()


def peek_stack(stack):
    if not stack:
        print("\nStack is Empty")
        return None

    return stack[-1]


def reverse_text(text):
    stack = []

    for character in text:
        stack.append(character)

    result = ""

    while stack:
        result += stack.pop()

    print("\n--- Reverse Text Using Stack ---")
    print("Original Text:", text)
    print("Reversed Text:", result)


def stack_operations():
    stack = []

    # PUSH
    push(stack, 20)
    push(stack, 30)
    push(stack, 40)

    print("\n--- Stack Operations ---")
    print("Initial Stack:", stack)

    # PEEK
    print("Top Element:", peek_stack(stack))

    # POP
    removed = pop_item_stack(stack)
    print("Removed Element:", removed)

    print("Stack After POP:", stack)

    # STACK SIZE
    print("Stack Size:", len(stack))

    # Another Stack Example
    stack = []

    stack.append(40)
    stack.append(67)
    stack.append(56)

    print("\n--- Direct Stack Operations ---")
    print("Initial Stack:", stack)
    print("Top Element:", stack[-1])

    removed = stack.pop()

    print("LIFO Removed Element:", removed)
    print("Stack After POP:", stack)

    # Reverse text
    reverse_text("python")


stack_operations()
