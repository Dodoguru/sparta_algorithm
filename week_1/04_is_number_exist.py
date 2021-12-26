input = [3, 5, 6, 1, 2, 4]

def is_number_exist(number, array):
    for element in array:  #for문이 돌면서 array의 길이만큼 아래 연산을 실행
        if number == element:  # 조건문에서 비교를 하면서, 비교 연산을 한 번 수행
            return True  # N*1 = N만큼 수행

    return False

result = is_number_exist(3, input)
print(result)