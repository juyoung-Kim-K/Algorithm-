##문제 1번
##Q1. 아래 DFS 함수 실행 시, 'A'에서 시작했을 때 **출력되는 첫 번째 경로(trace)**를 구하시오.


#주어진 그래프 형식
graph = {
    'A': ['B', 'C'],     # A → B, C
    'B': ['D', 'E'],     # B → D, E
    'C': ['F', 'G'],     # C → F, G
    'D': ['H', 'I'],     # D → H, I
    'E': ['J'],          # E → J
    'F': [], 'G': [], 'H': [], 'I': [], 'J': []
}

##첫번째 경로 찾아내는 코드 구현

'''
A에서 선택할 수 있는 선택지가 B,C로 지정되어있고, 가장 첫번째로 DFS 알고리즘 특성상 가장 깊은 노드까지 탐색하고 후에 다시 순차적으로 탐색하는 알고리즘으로,
왼쪽에 놓여진 B를 먼저 탐색한다. 이후에도 B를 타고 들어가면 선택지가 D,E가 있고 알고리즘 특성에 맞게 D를 물고 탐색하게 된다.
후에는 D에 포함된 H,I에서 H를 탐색하게 되고 H에는 아무것도 없기에 상위 포지션인 D를 타고간다. 탐색한 node는 무시하고, 탐색하지 않은 node를 순차적으로 탐색한다.
'''

def dfs_first_trace(graph, node, trace):
    trace.append(node)
    if graph[node]:  # 자식 노드가 있다면
        dfs_first_trace(graph, graph[node][0], trace)  # 가장 왼쪽 자식만 탐색
    return trace

# 실행
trace = dfs_first_trace(graph, 'A', [])
print("첫 번째 경로:", trace)

##결과물 
##첫 번째 경로: ['A', 'B', 'D', 'H']