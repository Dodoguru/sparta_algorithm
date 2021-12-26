#"aabbaccc" # -> 7
#"ababcdcdababcdcd" # -> 9
#"abcabcdede" # -> 8
#"abcabcabcabcdededededede" # -> 14
#"xababcdcdababcdcd" # -> 17

input = "abcabcabcabcdededededede"
# 1로 잘라야 할지, 2로 잘라야 할지
# 모든 경우의 수를 파악해야 한다.

def string_compression(string):
    n = len(string)
    compression_length_array = [] # 1~len까지 압축했을때 길이 값

    for split_size in range(1, n // 2 + 1):
        compressed = ""
        # string 갯수 단위로 쪼개기
        print("split_size : ", split_size)
        splited = [
            string[i:i + split_size] for i in range(0, n, split_size)
        ]
        print(splited)
        count = 1
        # for i in range(0, n, split_size)
        # 0, 2, 4, ... n까지 i가 나오게 된다.
        # 이걸 이용해서 문자열에 i번째부터, i+split_size까지, string[i:i + split_size]이므로 2단위로 쪼갤 수 있다.
        # 이걸 splited에 추가하면 된다.
        # 이걸 splited.aopend(string[i:i + splitsize)이다,
        # splited 배열 안에 다가 string을 어떻게 정의할지 정의한다.
        # splited 안에다가 써 준다.
        # for문의 조건을 string[i:i +  split_size] 안에다 쓴다.

        for j in range(1, len(splited)):
            prev, cur = splited[j-1], splited[j]
            if prev == cur:
                count+=1
            else : #이전 문자와 다르다면
                if count > 1: #문자가 반복되는 경우
                    compressed += (str(count) + prev)
                else : #문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
                    compressed += prev
                count = 1 # 초기화
        if count > 1 :
            compressed += (str(count) + splited[-1])
        else: # 문자가 반복되지 않아 한번만 나타난 경우 1은 생략함
              # splited[-1]은 꼬다리 값
            compressed += splited[-1]
        compression_length_array.append(len(compressed))
        print("compression_length_array", compression_length_array)

    return min(compression_length_array) # 최솟값 리턴

print(string_compression(input)) # 14가 출력되어야 합니다.