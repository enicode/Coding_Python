# 갈 수 있는 노드를 넓힌다.
def subsolution(cur_node, lambs, wolves, nxt_nodes, tree, info):
    # 양숫자
    if info[cur_node] == 0:
        lambs += 1
    else:
        wolves += 1
    ans = lambs
    # 만약 이번 노드에서 늑대 숫자가 양수와 같아지면 여태까지 모은 양 수를 반환한다.
    if wolves == lambs:
        return lambs
    # 갈수 있는 노드 중 하나를 선택한다.
    for node in nxt_nodes:
        #선택한 노드는 리스트에서 삭제하고, 그 노드에서 갈 수 있는 노드들을 추가한다.
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
    for edge in edges:
        tree[edge[0]].append(edge[1])
    
    answer = subsolution(0, 0, 0, tree[0], tree, info)
    return answer

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info,edges))
info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info,edges))