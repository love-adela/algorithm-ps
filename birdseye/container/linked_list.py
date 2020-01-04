# singly linked list

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
        self.head  = Node(item, self.head)
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
        return self.count

    def _printList(self):
        node = self.head
        while node:
            print(node.value, end=' ')
            node = node.next
            print()


