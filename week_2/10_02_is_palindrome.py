input = "소주만병만주소"


def is_palindrome(string): # is_palindrome("소주만병만주소")
    if len(string) <=1:
        return True

    if string[0] != string[-1]:
        return False

    return is_palindrome(string[1:-1])

# is_palindrome("주만병만주")
# is_palindrome("만병만")
# is_palndrome("병")
# 재귀함수는 문제가 축소되는 것이 보여야 한다.
# 재귀함수는 탈출조건이 있어야 한다.

print(is_palindrome(input))