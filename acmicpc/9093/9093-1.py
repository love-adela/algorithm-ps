# Stack 활용해서 풀기

N = int(input())

class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Stack(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return not bool(self.head)

    def push(self, item):
        self.head = Node(item, self.head)
        self.count += 1

    def pop(self):
        if self.count > 0:
            node = self.head
            self.head = node.next
            self.count -= 1
            return node.value
        else:
            print('Stack is empty')

    def peek(self):
        if self.count > 0:
            return self.head.value
        else:
            print('Stack is empty')

    def size(self):
        return self.size


def reverse_with_stack(sentence):
    s = Stack()
    for i in range(len(sentence)):

        if sentence[i] == ' ' or sentence[i]=='\n':
            while not s.is_empty():
                print(s.peek(), end='')
                s.pop()
            print(sentence[i], end='')
        else:
            s.push(sentence[i])
                
while N:
    sentence = input()
    sentence += '\n'
    reverse_with_stack(sentence)
    N-=1
