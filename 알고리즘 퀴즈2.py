##문제 2번
##Q2. 아래 BFS 함수에서, 'A'를 시작 노드로 하여 알파벳 순서로 인접 노드를 정렬한 후 탐색을 진행할 때, 다섯 번째로 방문하는 노드를 구하시오



#주어진 그래프 형식
graph = {
    'A': ['B', 'C'],     # A → B, C
    'B': ['D', 'E'],     # B → D, E
    'C': ['F', 'G'],     # C → F, G
    'D': ['H', 'I'],     # D → H, I
    'E': ['J'],          # E → J
    'F': [], 'G': [], 'H': [], 'I': [], 'J': []
}


##큐를 이용한 탐색 코드 
'''
BFS의 경우에는 시작한 노드의 하위 노드 중 가장 왼쪽에 있는 노드로 왼쪽에서 오른쪽으로 순서대로 탐색하는 알고리즘이다.
즉 나타난 그래프를 BFS로 탐색을 할 때는
시작 A를 시작하고 A의 하위 노드인 B,C 노드를 큐시트에 순차적으로 적립을 한다. 이때 큐에는 [B,C]가 적립되어 있다. 이후에 B노드를 꺼내서 탐색처리를 한다.
후에 B노드의 하위 노드은 D,E 노드가 큐시트에 순차적으로 저장된다. 이때 큐는 [C,D,E]가 저장된다.
위에 처럼 순차적으로 큐 시트에 저장된 노드를 꺼내서 탐색을 하고 노드에 해당하는 하위 노드를 큐시트에 저장하게 되면 5번째 방문하는 노드는 A-B-C-D-E 즉 E를 5번째 노드로 방문한다.
'''

from collections import deque

def bfs_trace(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            # 인접 노드를 알파벳 순으로 정렬해서 큐에 저장
            for neighbor in sorted(graph[node]):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited

##실행
trace = bfs_trace(graph, 'A')
print("전체 방문 순서:", trace)
print("다섯 번째로 방문한 노드:", trace[4])

##실행 결과 - 다섯 번째로 방문한 노드: E