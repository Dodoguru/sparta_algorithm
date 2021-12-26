#위의 그래프를 예시로 삼이서 인접 리스트 방식으로 표현했습니다.
graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2,4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}
visited = []

#1. 시작 노드(루트 노드)인 1부터 탐색합니다.
#2. 현재 방문한 노드를 visited에 추가한다.
#3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드에 방문한다.
# visited_array = [1]

def dfs_recursion(adjacent_graph, cur_node, visited_array): # cur_node는 시작하느 노드인데 root가 1인데, 1부터 시작함. 그래서 1 넣음. / # visited_array는 밖의 빈 노드
    visited_array.append(cur_node) # 시작 노드를 visited_array에 추가. 2번 작업이 마침.
    for adjacent_node in adjacent_graph:
        #print(adjacent_node)
        if adjacent_node not in visited_array:
            print(adjacent_node)
            dfs_recursion(adjacent_graph, adjacent_node, visited_array)

    return

dfs_recursion(graph, 1, visited) #1이 시작노드입니다! 여기서 1번 작업 마침.
print(visited) #[1,2,3,4,5,6,7,8,9,10] 이 출력됩니다.