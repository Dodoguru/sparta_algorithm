class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        new_node = Node(value)  # 새로운 노드 삽입
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node # 테일 다음에 노드에 new_node 대입
        self.tail = new_node #테일을 이제 new_node로 바꿈

    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        delete_head = self.head # 반환하는 것을 미리 다른 변수에 저장. 안 그러면 포인터를 잃어버릴 수 있음.
        self.head = self.head.next

        return delete_head.data

    def peek(self):
        if self.is_empty():
            return "Queue is Empty"
        return self.head.data

    def is_empty(self):
        return self.head is None

queue = Queue()
queue.enqueue(3)
print(queue.peek())
queue.enqueue(4)
print(queue.peek())
queue.enqueue(5)
print(queue.peek())
print(queue.dequeue())
print(queue.peek())
print(queue.is_empty())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())