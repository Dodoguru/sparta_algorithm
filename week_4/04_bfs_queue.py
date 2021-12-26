# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2,3,4],
    2: [1,5],
    3: [1,6,7],
    4: [1,8],
    5: [2,9],
    6: [3,10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}
#1. 시작 노드를 큐에 넣습니다.
#2. 현재 큐의 노드를 뺴서 visited에 추가합니다.
#3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가하면 된다.


def bfs_queue(adj_graph, start_node):
    queue = [start_node]
    visited = []
    while queue:
        current_node = queue.pop(0) # 큐는 맨 앞에서부터 뽑아야 해서 0번쨰부터 뽑는 것임.
        #print(current_node)
        visited.append(current_node) # visited[]에 방문한 노드를 추가한다.
        for adjacent_node in adj_graph[current_node]: #반복을 하는데, 반복하는 대상이 인접그래프에서 인접한 노드들만 봐주면 된다.
            #print(adj_graph[current_node])
            #print(adjacent_node)
            if adjacent_node not in visited: #인접한 노드가 방문한 적이 있는지 확인한다.
                #print(adjacent_node)
                queue.append(adjacent_node) #방문하지 않았다면 그 노드를 큐에다가 추가한다.
                print(queue)
    return visited

print(bfs_queue(graph, 1)) #1이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]이 출력되어야 합니다!