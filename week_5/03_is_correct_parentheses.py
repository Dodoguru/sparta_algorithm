from collections import deque

balanced_parentheses_string = "()))((()"

def get_correct_parentheses(balanced_parentheses_string):
    return

print(get_correct_parentheses(balanced_parentheses_string)) #"()(())()"가 반환 되어야 합니다!


def is_correct_parentheses(string) : #올바른 괄호인지 확인
    stack = []
    for s in string:
        if s == '(':
            stack.append(s)
        elif stack:
            stack.pop()
        return len(stack) == 0

def separate_to_u_v(string): #u, v로 분리
    queue = deque(string)
    left, right = 0,0
    u, v= "", ""

    while queue:
        char = queue.popleft()
        u += char
        if char == '(':
            left+=1
        else:
            right +=1
        if left == right: #단, u는 균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 한다. 즉, 여기서 갈 쌍이 더 생기면 안 된다.
            print(u)
            break

    v = ' '.join(list(queue))
    print(v)
    return u, v

def reverse_parentheses(string): #뒤집기
    reversed_string = ""
    for char in string:
        if char == '(':
            reversed_string += ")"
        else:
            reversed_string =+ "("
    return reversed_string

def change_to_correct_parentheses(string):
    if string == '': #1번
        return ''
    u,v = separate_to_u_v(string) #2번
    if is_correct_parentheses(u): #3번
        return u+change_to_correct_parentheses(v)
    else:
        return '(' + change_to_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])


def get_correct_parentheses(balanced_parentheses_string):
    if is_correct_parentheses(balanced_parentheses_string):
        return balanced_parentheses_string
    else:
        return change_to_correct_parentheses(balanced_parentheses_string)

print(get_correct_parentheses(balanced_parentheses_string))