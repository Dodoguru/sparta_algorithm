input = 100


# 피보나치 수열 함수 : Fibo(N) = Fibo(N-1) + Fibo(N-2)
# 피보나치 탈출 조건 : Fibo(1) = FIbo(2) = 1
# fibo_recursion(3) = fibo_recursion(2) + fibo_recursion(1) = 1 + 1

def fibo_recursion(n):
    if n == 1 or n==2 :
        return 1
    return fibo_recursion(n-1) + fibo_recursion(n-2)

print(fibo_recursion(input))


# 1.FIbo(3)
# Fibo(2)와 FIbo(1)을 더하면 된다.
# 이는 1,1 -> 연산량 2번

# 2. FIbo(4)를 구한다고 치면
# Fibo(3)과 Fibo(2)를 더하면 된다.
# Fibo(3)은 1번 과정을 반복하면 된다.
# Fibo(2)는 1을 반환하면 된다.
# 즉, Fibo(3)을 구하고, Fibo(2)인 1을 더해주면 된다.
# 그러면, Fibo(3)은 Fibo(2)와 Fibo(1)을 더했다.
# 1+1 이라서 연산량이 2번이다.
# 총 연산량은 연산량이 3번이다.

# Fibo(5)를 구한다고 치면, Fibo(4)와 Fibo(3)을 구하면 된다.
# FIbo(4)는 2의 과정을 반복하면 된다. Fibo(3)은 1의 과정을 반복하면 된다.
# Fibo(4) 구하기 위해서는 Fibo(3)을 구하고 1을 더해주면 된다.
# Fibo(3)을 구하기 위해서는 Fibo(2)와 Fibo(1)을 더해주면 된다.
# Fibo(3)을 구하기 위해서는 Fibo(2)와 Fibo(1)을 더해주면 된다.
# Fibo(3)을 구하는 것이 반복된다. 그리고 똑같은 것을 구하는 것이 여러번 반복된다.
# 이미 시켰던 것은 똑같은대서 하고 있따.
# 우리가 했던 것을 기억하는 동적 계획법이 필요하다.