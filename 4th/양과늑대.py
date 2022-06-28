# 루트가 제한적이므로 완전탐색이 가능할 것 같다.
# 갈 수 있는 노드를 넓힌다.
# 인자로 1. 현재 노드, 2. 양수, 3. 늑대수, 4. 가능한 다음노드, 5. 트리, 그리고 6. 늑대와 양의 분포를 받는다.
def subsolution(cur_node, lambs, wolves, nxt_nodes, tree, info):
    # 양 숫자 +1
    if info[cur_node] == 0:
        lambs += 1
    # 늑대 숫자 +1
    else:
        wolves += 1
    # 지금 까지 모은 양의 숫자가 최대치라고 가정
    ans = lambs
    # 만약 이번 노드에서 늑대 숫자가 양수와 같아지면 여태까지 모은 양 수를 반환한다.
    if wolves == lambs:
        return lambs
    # 갈수 있는 노드 중 하나를 선택한다.
    for node in nxt_nodes:
        #선택한 노드는 리스트에서 삭제하고, 그 노드에서 갈 수 있는 노드들을 다음에 갈수있는 노드에 추가한다.
        new_nxt_nodes = nxt_nodes.copy()
        new_nxt_nodes.remove(node)
        for i in range(2):
            try:
                new_nxt_nodes.append(tree[node][i])
            except IndexError:
                pass
        # 그렇게 늘려나가다가 제일 양을 많이 모을 수 있는 경우를 반환한다.
        ans = max(ans, subsolution(node, lambs, wolves, new_nxt_nodes, tree, info))
    return ans


def solution(info, edges):
    answer = 0
    tree= [[] for _ in range(len(info))]
    # 자기 자신의 인덱스가 번호로 하고 값들을 다음 노드로 하는 트리 생성
    for edge in edges:
        tree[edge[0]].append(edge[1])
    # 초깃값 넣기
    answer = subsolution(0, 0, 0, tree[0], tree, info)
    return answer

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info,edges))
info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info,edges))