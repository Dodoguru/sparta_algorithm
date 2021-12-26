input = "011110"
# 이거 딱 봐도, 0 -> 1로 뒤집으면 두 번 뒤집어야 하는데, 1 -> 0은 한번만 뒤집어도 되는 것을 알 수 잇음
# 0을 뒤집는 횟수를 카운트하는 변수, 1을 뒤집는 횟수를 카운트하는 변수를 알아야 한다.
# 그 다음에 처음이 0이냐, 1이냐 그것을 알아야 한다.
# 그 다음에 다음에 나오는 수가 같은 수인지 아닌 지를 알아야 한다.

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    count_to_all_zero = 0
    count_to_all_one = 0

    if string[0] == '0': # 배열의 첫 번째 수가 0일 경우
        count_to_all_one += 1 #배열의 첫번째 원소가 0이 나오면 1로 바꿔줘야 하므로 1의 카운트를 늘려준다.
    elif string[0] == '1': # 배열의 첫 번쨰 수가 1일 경우
        count_to_all_zero += 1 #배열의 첫번째 원소가 1이 나오면 0으로 바꿔줘야 하므로 0의 카운트를 늘린다.
        #이걸 안 해주면 count_to_all_one도 1이 나옴. 0번째 원소가 1인지 0인지를 파악하기 위한것인가?

    print("배열의 첫 인덱스에 들은 수는?", string[0])
    for i in range(len(string) -1):
        print(i)
        print("count_to_all_one=", count_to_all_one, "count_to_all_zero=", count_to_all_zero)
        if string[i] != string[i+1]:
            print("앞에 값과, 뒤에 값이 다르다!")
            if string[i+1] == '0':
                print("숫자를 뒤집는다!")
                count_to_all_one += 1
                print("count_to_all_one은?", count_to_all_one)
            if string[i+1] == '1':
                print("숫자를 뒤집는다!")
                count_to_all_zero += 1
                print("count_to_all_zero?", count_to_all_zero)

    return min(count_to_all_one, count_to_all_zero)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)