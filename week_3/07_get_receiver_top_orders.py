top_heights = [6, 9, 5, 7, 4]

# [6, 9, 5, 7, 4]
def get_receiver_top_orders(heights):
    answer = [0] * len(heights) # [0, 0, 0, 0, 0, 0]
    while heights:
        height = heights.pop()
        for idx in range(len(heights)-1, 0, -1):
            #print(idx)
            if heights[idx] > height: # heights[3->2->1->1] 이렇게 줄어가는데, heights[idx]가 height보다 더 크면 레이저 송신
            #print(heights[idx])
                answer[len(heights)] = idx+1 #배열의 인덱스가 0부터 시작하니 +1을 더해준 것임
              #print(answer[len(heights)])
                break
    return answer

print(get_receiver_top_orders(top_heights))