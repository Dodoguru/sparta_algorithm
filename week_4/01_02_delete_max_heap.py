class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) -1

        while cur_index > 1: #cur_index가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다.
            parent_index = cur_index //2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break
    #1. 루트 노드와 맨 끝에 있는 원소를 교체한다.
    #2. 맨 뒤에 있는 원소를(워래 루트노드)를 삭제한다. 이때, 끝에 반환해줘야 하니까 저장해둡시다.
    #3. 힙의 규칙이 안 지켜진 상태이므로, 변경된 노드와 자식 노드들을 비교한다. 두 자식 중 더 큰 자식과 비교해서 자신보다 자식이 더 크다면 자리를 바꿔준다.
    #4. 자식 노드 둘 보다 부모 노드가 더 크거나, 바닥에 도달하지 않을때까지(자식 노드가 없다면) 멈춰야 한다. 3을 이떄까지 반복한다.
    #5. 2에서 제거한 원래 루트 노드를 반환한다.
    def delete(self):
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        prev_max = self.items.pop()

        cur_index = 1
        while cur_index <= len(self.items) -1:
            left_child_index = cur_index *2
            right_child_index = cur_index*2 + 1
            max_index = cur_index # 이 값을 통해서 왼쪽이 큰지 오른쪽이 큰지. / 이 max_index에는 원래 root와 값을 바꾼 놈이 들어가는 듯

            if left_child_index <= len(self.items) -1 and self.items[left_child_index]>self.items[max_index]:  #현재 왼쪽 자식이 있다는 의미이다. 그리고 부모보다 더 큰 상황이야 교체할지 말지 결정.
                max_index = left_child_index

            if right_child_index <= len(self.items) -1 and self.items[right_child_index] > self.items[max_index]:
                max_index = right_child_index

            if max_index == cur_index:
                print("max index : ", max_index)
                break # 부모노드가 더 크니 멈춰야 함

            self.items[cur_index], self.items[max_index] = self.items[max_index], self.items[cur_index]

        return prev_max

max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(6)
max_heap.insert(7)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items) #[None, 8, 6, 7, 2, 5, 4]
print(max_heap.delete()) # 8을 반환해야 합니다!
print(max_heap.items) # [None, 7, 6, 4, 2, 5]