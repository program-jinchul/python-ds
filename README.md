# python-ds

파이썬으로 직접 구현한 자료구조 모음입니다.
`list`, `collections` 같은 내장 자료구조에 기대지 않고, 노드와 포인터(참조) 수준에서 밑바닥부터 구현했습니다.

## 목적

- 노드 연결과 포인터 재연결 같은 자료구조의 동작 원리를 직접 구현하며 이해
- 연산별 시간복잡도를 코드와 함께 확인

## 구현 현황

**01_linear**
- [x] 단순 연결 리스트 (Singly Linked List)
- [x] 이중 연결 리스트 (Doubly Linked List)
- [x] 원형 연결 리스트 (Circular Linked List)

그 외 자료구조와 알고리즘은 순서대로 추가할 예정입니다.

## 구조

```
python-ds/
├── 01_linear/
│   ├── 02_singly_linked_list.py   # 단순 연결 리스트
│   ├── 03_doubly_linked_list.py   # 이중 연결 리스트
│   └── 04_circular_list.py        # 원형 연결 리스트
└── ...
```

## 연결 리스트 비교

세 리스트는 모두 같은 연산을 제공합니다: `append`, `prepend`, `insert_after`, `search`, `delete`, `display`.
`insert_after`, `search`, `delete`는 성공 여부를 `True` / `False`로 반환합니다.

| 연산 | 단순 | 이중 | 원형 |
|------|------|------|------|
| `append` (맨 뒤 추가) | O(n) | O(1) | O(1) |
| `prepend` (맨 앞 추가) | O(1) | O(1) | O(1) |
| `insert_after` (값 뒤에 삽입) | O(n) | O(n) | O(n) |
| `search` (값 탐색) | O(n) | O(n) | O(n) |
| `delete` (값 삭제) | O(n) | O(n) | O(n) |
| `display` (출력) | O(n) | O(n) | O(n) |

- 단순 리스트의 `append`가 O(n)인 이유: `tail` 포인터 없이 `head`만 가지고 있어서 마지막 노드까지 탐색해야 합니다.
- 이중, 원형 리스트는 `tail` 포인터로 `append`를 O(1)로 최적화했습니다.
- `insert_after`, `delete`는 연결 작업 자체는 O(1)이고, 값으로 노드를 찾는 탐색이 O(n)입니다.

## 실행 방법

```bash
git clone https://github.com/program-jinchul/python-ds.git
cd python-ds/01_linear
python 02_singly_linked_list.py
python 03_doubly_linked_list.py
python 04_circular_list.py
```

각 파일 하단의 `if __name__ == "__main__":` 블록에 동작을 확인하는 테스트 코드가 들어 있습니다.

- 환경: Python 3.x (표준 라이브러리만 사용)

## 실행 예시

```
# 단순 연결 리스트
5 -> 10 -> 20 -> 25 -> 30 -> None

# 이중 연결 리스트 (정방향 / reverse=True)
10 <-> 25 <-> 30 <-> None
30 <-> 25 <-> 10 <-> None

# 원형 연결 리스트
5 -> 10 -> 15 -> 20 -> 25 -> (head)
```

## 구현하면서 신경 쓴 점

- **삭제 케이스 분리**: head 삭제, tail 삭제, 중간 노드 삭제, 노드가 하나뿐인 경우를 나눠서 포인터를 재연결
- **포인터 끊김 방지**: 삽입할 때 새 노드의 `next`를 먼저 연결한 뒤 기존 노드의 `next`를 갱신
- **`tail` 포인터 관리**: 마지막 노드를 삽입하거나 삭제할 때 `tail`도 함께 갱신
- **원형 리스트의 순회 종료 조건**: `None` 대신 `current.next == head`로 한 바퀴를 판단하고, `tail.next`가 항상 `head`를 가리키도록 유지
- **일관된 인터페이스**: 세 리스트의 연산 이름, 반환값, 출력 형식을 통일