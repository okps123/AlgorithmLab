class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        return self.queue.pop(0) if not self.isEmpty() else -1

    def getFront(self):
        return self.queue[0] if not self.isEmpty() else -1
    
    def getBack(self):
        return self.queue[-1] if not self.isEmpty() else -1

    def getSize(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0

queue = Queue()

n = int(input())
for i in range(n):
    command = input().split(' ')
    if 'push' == command[0]:
        queue.enqueue(command[1])
    elif 'pop' == command[0]:
        print(queue.dequeue())

    elif 'front' == command[0]:
        print(queue.getFront())

    elif 'back' == command[0]:
        print(queue.getBack())

    elif 'size' == command[0]:
        print(queue.getSize())

    elif 'empty' == command[0]:
        print(int(queue.isEmpty()))