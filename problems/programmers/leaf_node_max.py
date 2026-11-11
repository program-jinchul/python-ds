def solution(dist_limit, split_limit):
    max_leaves = 1  # 분배 노드를 0개 쓸 때 루트의 자식 1개가 리프인 경우 (최소 1개)

    def dfs(n_nodes, current_prod, dist_used, current_leaves):
        nonlocal max_leaves
        
        # c: 자식 수 (2 또는 3)
        for c in (2, 3):
            if current_prod * c > split_limit:
                continue
            if dist_used + n_nodes > dist_limit:
                continue
                
            # k_leaf: 현재 노드들의 자식 중 리프가 되는 수 (0부터 c까지 가능)
            for k_leaf in range(c + 1):
                leaves_produced = n_nodes * k_leaf
                next_n_nodes = n_nodes * (c - k_leaf)
                
                total_leaves = current_leaves + leaves_produced
                if total_leaves > max_leaves:
                    max_leaves = total_leaves
                    
                # 다음 레벨로 넘어갈 분배 노드가 있는 경우에만 탐색 지속
                if next_n_nodes > 0:
                    dfs(next_n_nodes, current_prod * c, dist_used + n_nodes, total_leaves)

    # 깊이 1에서 루트의 자식(분배 노드 1개, n_nodes=1, current_prod=1, dist_used=0)으로부터 시작
    dfs(1, 1, 0, 0)
    
    return max_leaves


if __name__ == "__main__":
    assert solution(3, 6) == 6
    assert solution(0, 10) == 1
    assert solution(3, 100) == 7
    assert solution(5, 16) == 9
    print("ALL PASS")
