import sys
read = lambda: sys.stdin.readline()
class Queue:
    def __init__(self):
        self.lst = []
        
    def push(self, x):
        self.lst.append(x)
        
    def pop(self):
        if self.empty():
            return -1
        else:
            output = self.lst[0]
            self.lst = self.lst[1:]
            return output

    def empty(self):
        return 1 if len(self.lst) == 0 else 0
    
    def size(self):
        return len(self.lst)
    
    def front(self):
        if self.empty():
            return -1
        else:
            return self.lst[0]
        
    def back(self):
        if self.empty():
            return -1
        else:
            return self.lst[-1]
        
N = int(read())
queue = Queue()

while N:
    N -= 1
    elem = read().split()
    cmd = elem[0]
    
    if cmd == 'push':
        queue.push(elem[1])
    elif cmd == 'pop':
        print(queue.pop())
    elif cmd  == 'size':
        print(queue.size())
    elif cmd == 'empty':
        print(queue.empty())
    elif cmd == 'front':
        print(queue.front())
    elif cmd == 'back':
        print(queue.back())
    else:
        print()
