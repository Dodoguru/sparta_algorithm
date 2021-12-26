input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                      "t", "u", "v", "w", "x", "y", "z" ]

    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array: # alphabet에 차례대로 alphabet_array의 값을 넣음, 사실 alphabet_array는 고정된 값
        occurrence = 0 # occurrence에 일단 0으로 초기화
        for char in string: # 중첩 for문으로 char이라는 변수에 string의 값을 넣음, 이건 크기가 얼마인지 미정
            if char == alphabet: # 해당하는 알파벳이 나오면
                occurrence +=1 # occurrence를 하나 더 늘림

        if occurrence > max_occurrence: # max_occurrence라는 최대값이 있는데, occurrence 보다 더 크다면
            max_occurrence = occurrence # max_occurrence랑 occurrence랑 교체
            max_alphabet = alphabet # 그 alphabet을 max_alphabet을 넣음

    return max_alphabet

result = find_max_occurred_alphabet(input)
print(result)