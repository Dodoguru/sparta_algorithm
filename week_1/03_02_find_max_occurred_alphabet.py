input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string: # string에 있는 값을 char에다 넣음
        if not char.isalpha(): # char에 있는 것이 알파벳인지 검사
            continue # alphabet이 아니면 그냥 계속 다음. 즉, 스페이스바이면 통과.
        arr_index = ord(char) - ord("a") # char에 있는 것 - ord("a")하면 0이 나옴. a면 0번, b면 1번, c면 2번 인덱스
        alphabet_occurrence_array[arr_index] += 1 # a가 맨 앞, b가 2번쨰칸인데, 각 알파벳 하나 나올떄마다 값 하나 증가 시킴

    max_occurrence = 0 # 제일 많이 나오는 알파벳이 들어가는 변수를 0으로 초기화
    max_alphabet_index = 0 # 제일 많이 나오는 알파벳 값

    for index in range(len(alphabet_occurrence_array)): #index에 len 함수의 길이만큼
        # index 0 -> alphabet_occurrence is 3, because a appeared 3 times
        alphabet_occurrence = alphabet_occurrence_array[arr_index] # 알파벳 등장율에 알파벳 등장 배열을 넣음

        if alphabet_occurrence > max_occurrence: # 알파벳 등장하는 것이 max_occurrence보다 더 많으면
            max_alphabet_index = index # 젤 많이 나오는 알파벳의 인덱스를 이 max_alphabet_index에 넣음
            max_occurrence = alphabet_occurrence # max_occurrence에 alphabet_occurrence(제일 많이 나온 알파벳이 든 변수) 넣음
        print(max_alphabet_index)
        return chr(max_alphabet_index+ord("a")) #chr 함수로 인해 max_alphabet_index와 ord("a")의 값을 더하면 그 알파벳이 나옴


result = find_max_occurred_alphabet(input)
print(result)