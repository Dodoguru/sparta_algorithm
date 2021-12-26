class MaxHeap:
    def __init__(self):
        self.items = [None]
    #1. 새노드를 맨 끝에 추가한다.
    #2. 지금 넣은 새노드를 부모와 비교한다. 만약 부모보다 크가면 교체한다.
    #3. 이 과정을 꼭대기까지 반복한다.

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) -1
       # print(cur_index)

        while cur_index > 1:
            print("cur_index : ", cur_index)
            parent_index = cur_index //2
            print("parent_index : ", parent_index)
            if self.items[cur_index] > self.items[parent_index]:
                print("부모노드, 자식 노드 교환")
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index # 도대체 너는 왜 있니? parent_index와 cur_index가 자리 바꿨으니 원래 parent_index가 있던 자리에 cur_index가 들어감.
            else:
                break

        return

#print("시작한다")
max_heap = MaxHeap()
#print("힙에 값들 들어가기 시작!")
print("3삽입")
max_heap.insert(3) #1개 들어가니까 길이가 1이 됨
print("4삽입")
max_heap.insert(4) #2개 들어가니까 길이가 2가 됨
print("2삽입")
max_heap.insert(2) #3개 들어가니까 길이가 3이 됨
print("중간 결과 : ", max_heap.items)
print("9삽입")
max_heap.insert(9) #4개 들어가니까 길이가 4가 됨
print("8삽입")
max_heap.insert(8)
print("6삽입")
max_heap.insert(6)
print("1삽입")
max_heap.insert(1)
print("최종 결과", max_heap.items) # [None, 9, 4, 2, 3]가 출력되어야 합니다.


# 코드 설명 (찔문 필요)
# 1. 3만 넣었을 때는, cur_index = 1 이라서 while문의 cur_index > 1가 실행이 안 됨. [None]이 0 번째 인덱스에 들어가 있다고 가정하는지?
# 2. 이거 읽는 순서가 전위순회인지? 해결됨 -> 그냥 루트부터 왼쪽 - 오른쪽 순서대로 레벨오더 순회 방식임
# 3. 마지막에 cur_index와 parent_index가 하는 역할이 뭔지?
# cure_index의 역할은 삽입한 숫자를 가리키는 포인터의 역할. 그 숫자가 자기 자리를 찾아갈떄까지 필요한 것.
