class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        return

    def pop(self):
        if self.is_empty():
            return "Stack is Empty"

        delete_head = self.head
        self.head = self.head.next
        return delete_head

    def peek(self):
        if self.is_empty():
            return "Stack is Empty"
        return self.head.data #self.head는 그냥 Node 클래스가 나옴


    def is_empty(self):
        return self.head is None



stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
print(stack.pop().data)
print(stack.peek())
print(stack.is_empty())
print(stack.pop().data)
print(stack.is_empty())