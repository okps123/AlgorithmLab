from collections import deque
deque = deque()


def invoke(command, arg=0):
    if command == "push_front":
        deque.appendleft(arg)
    elif command == "push_back":
        deque.append(arg)
    elif command == "pop_front":
        print(deque.popleft() if deque else -1)
    elif command == "pop_back":
        print(deque.pop() if deque else -1)
    elif command == "size":
        print(len(deque))
    elif command == "empty":
        print(0 if deque else 1)
    elif command == "front":
        print(deque[0] if deque else -1)
    elif command == "back":
        print(deque[-1] if deque else -1)


for i in range(int(input())):
    invoke(*input().split())
