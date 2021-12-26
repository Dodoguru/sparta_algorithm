class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

# index.next = new_node
# new_node.next = next_node
    def add_node(self, index, value):
        new_node = Node(value) # new_node에 새 노드 추가 / [6]

        if index == 0:
            new_node.next = self.head #[6] -> [5] 새로 head로 들어가는 놈의 next가 원래 head이다.
            self.head = new_node
            return

        node = self.get_node(index-1) # 일단 node에 현재 index 저장 /[5]
        next_node = node.next # next_node변수에 현재 노드 다음 노드 저장 / [12]
        node.next = new_node # index에 다음에 new_node를 삽입 / [5] -> [6]
        new_node.next = next_node # 원래 next_node는 new_node.next 다음으로 / [6] -> [12]
        return

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return

        node = self.get_node(index-1) #index=0이면, self.get_node(-1)
        node.next = node.next.next


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.print_all()
linked_list.delete_node(0)
linked_list.print_all()