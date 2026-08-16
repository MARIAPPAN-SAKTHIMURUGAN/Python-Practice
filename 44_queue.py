from collections import deque


def enqueue(queue, value):
    queue.append(value)


def dequeue(queue):
    if not queue:
        print("Queue is empty")
        return None

    return queue.popleft()


def peek_queue(queue):
    if not queue:
        print("Queue is empty")
        return None

    return queue[0]


def queue_operations():
    queue = deque()

    # Enqueue
    queue.append(45)
    queue.append("yu")
    queue.append(67)

    print("\n--- Queue Operations ---")
    print("Initial Queue:", queue)

    # Peek
    print("First Item:", queue[0])

    # Dequeue
    removed = queue.popleft()

    print("Removed Item:", removed)
    print("Queue After Dequeue:", queue)

    print("Next Item:", queue[0])

    # appendleft() demonstration
    queue.appendleft("left")

    print("\n--- Deque appendleft() ---")
    print("After appendleft():", queue)


def queue_function_operations():
    queue = deque()

    # Enqueue using function
    enqueue(queue, 23)
    enqueue(queue, "at")
    enqueue(queue, "mm")
    enqueue(queue, 27)

    print("\n--- Queue Functions ---")
    print("Initial Queue:", queue)

    # Peek
    print("First Item:", peek_queue(queue))

    # Dequeue
    print("Removed Item:", dequeue(queue))

    print("Final Queue:", queue)


queue_operations()
queue_function_operations()
