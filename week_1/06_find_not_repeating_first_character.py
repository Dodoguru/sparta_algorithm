input  = "abadabac"

def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0]*26 # 문자열을 입력받아서 alphabet_occurrence_array에 하나하나 추가해나감
    #a, b, c, d 순서대로 저장한다고 생각함
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a") # char이 알파벳이면 아스키 코드를 이용해서 변형
        alphabet_occurrence_array[arr_index] +=1
        print(alphabet_occurrence_array)
    not_repeating_character_array = [] #하나만 나오는 놈들 집어넣는 곳
    for index in range(len(alphabet_occurrence_array)): # 알파벳의 길이만큼 반복을해줌, 26번 반복함
        alphabet_occurrence = alphabet_occurrence_array[index]
        print(alphabet_occurrence)
        if alphabet_occurrence == 1: # 알파벳이 한 번 넣으면 아래 배열에다 append 함수 이용해서 집어 넣음
            not_repeating_character_array.append(chr(index + ord("a"))) # 인덱스를 알파벳으로 전환시켜주는 과정
    #print(not_repeating_character_array) # not_repeating_character_array는 기존 input의 순서 보장 안함


    for char in string:
        if char in not_repeating_character_array: # 그 찾고자 하는 char의 값(한 번만 나오는 값)을 찾으면 바로 반환
             return char

result = find_not_repeating_first_character(input)
print(result)