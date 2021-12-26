input = 20


def find_prime_list_under_number(number):
    prime_number_list = [] # 소수가 들어갈 배열
    for n in range(2, number+1): # 2부터 number+1까지 돌린다. range 함수는 자기보다 하나 작은 것까지 출력.
        print("1째 for문", n, number+1)
        for i in prime_number_list: #소수인 수들만 가지고 확인.
            print("2째 for문", i, prime_number_list)
            if n % i == 0 and i*i<=n: # 소수는 나눠 떨어지지 않는 수이거나 n이 n의 제곱근보다 크지 않는 수
                break
        else:
            print("소수", n,"이(가) 들어갔습니다!")
            print("")
            prime_number_list.append(n) #소수인 것이 판별되면 prime_number_list.append(n) 배열에 삽입

    return prime_number_list #소수가 들어 있는 배열을 반환한다.


result = find_prime_list_under_number(input) # 함수의 return 값을 result에다 담는다.
print(result)