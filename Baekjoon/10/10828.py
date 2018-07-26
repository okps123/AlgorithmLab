class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop(-1) if not self.isEmpty() else -1

    def getTop(self):
        return self.stack[-1] if not self.isEmpty() else -1

    def getSize(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0

stack = Stack()

n = int(input())
for i in range(n):
    command = input().split(' ')
    if 'push' == command[0]:
        stack.push(command[1])
    elif 'pop' == command[0]:
        print(stack.pop())
    elif 'top' == command[0]:
        print(stack.getTop())
    elif 'size' == command[0]:
        print(stack.getSize())
    elif 'empty' == command[0]:
        print(int(stack.isEmpty()))