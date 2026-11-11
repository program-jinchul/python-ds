def _cost(s, a):
    """2-깊이 a개를 써서 마지막 2-깊이에 분배 노드 s개를 만들 때 필요한 최소 분배 노드 수."""
    total = 0
    for _ in range(a):
        total += s
        s = max((s + 1) // 2, 1)
    return total


def solution(dist_limit, split_limit):
    # 같은 깊이의 분배 노드는 자식 수가 같으므로 트리는 깊이별 자식 수 수열로 결정된다.
    # 순서는 2를 모두 앞에, 3을 모두 뒤에 두는 2^a 3^b로 고정한다.
    D = dist_limit
    best = 1
    a, p2 = 0, 1
    while p2 <= split_limit:
        b, p = 0, p2
        while p * 3 <= split_limit:
            b, p = b + 1, p * 3
        K = 3 ** b - 1  # 2-단계 끝 분배 노드 s개 → 3-단계 수용량 s*K
        if a == 0:
            best = max(best, 1 + 2 * min(D, K // 2))
        elif _cost(1, a) <= D:
            lo, hi = 1, 2 ** (a - 1)
            # D - cost(s) >= K*s 를 만족하는 최대 s
            if D - _cost(1, a) >= K:
                while lo < hi:
                    mid = (lo + hi + 1) // 2
                    if D - _cost(mid, a) >= K * mid:
                        lo = mid
                    else:
                        hi = mid - 1
            for s in (lo, lo + 1):
                if s <= 2 ** (a - 1) and _cost(s, a) <= D:
                    x = _cost(s, a)
                    used3 = min(D - x, K * s)
                    # 남은 예산은 앞쪽 2-깊이(용량 2^(i-1))의 빈자리에 추가 분할로 사용
                    extra = min(D - x - used3, (2 ** (a - 1) - 1) - (x - s))
                    best = max(best, 1 + x + 2 * used3 + extra)
        a, p2 = a + 1, p2 * 2
    return best


if __name__ == "__main__":
    assert solution(3, 6) == 6
    assert solution(0, 10) == 1
    assert solution(3, 100) == 7
    assert solution(5, 16) == 9
    print("ALL PASS")
