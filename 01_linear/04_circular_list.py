"""
원형 연결 리스트 (Circular Linked List)

tail.next가 항상 head를 가리켜 원형을 유지한다.
tail 포인터를 따로 두어 마지막 노드를 찾는 탐색을 없앴다.

연산            시간복잡도
append          O(1)   tail 포인터 사용
prepend         O(1)   tail 포인터 사용
insert_after    O(n)   target 탐색 O(n) + 연결 O(1)
search          O(n)
delete          O(n)
display         O(n)

모든 변경/탐색 연산은 성공 여부를 True/False로 반환한다.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # tail.next는 항상 head

    def append(self, data):
        node = Node(data)
        # 리스트가 비어있는 경우: 자기 자신을 가리켜 원형 유지
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = node
            return

        node.next = self.head  # 새 노드의 next를 head로
        self.tail.next = node  # 기존 tail이 새 노드를 가리킴
        self.tail = node       # tail 이동

    def prepend(self, data):
        node = Node(data)
        # 리스트가 비어있는 경우
        if self.head is None:
            self.head = node
            self.tail = node
            node.next = node
            return

        node.next = self.head  # 새 노드의 next를 기존 head로
        self.tail.next = node  # tail이 새 노드를 가리킴 (원형 유지)
        self.head = node       # head 이동 (tail은 그대로)

    def _find(self, target_data):
        """target_data를 가진 노드를 반환. 한 바퀴 돌아도 없으면 None."""
        if self.head is None:
            return None

        current = self.head
        while True:
            if current.data == target_data:
                return current
            current = current.next
            if current == self.head:  # 한 바퀴 다 돌았는데 못 찾음
                return None

    def insert_after(self, target_data, data):
        current = self._find(target_data)

        # 못 찾은 경우 (빈 리스트 포함)
        if current is None:
            return False

        node = Node(data)
        node.next = current.next  # 오른쪽 노드 연결을 먼저 백업
        current.next = node       # 왼쪽 노드가 새 노드를 가리킴

        if current == self.tail:  # tail 뒤에 삽입했다면 tail 갱신
            self.tail = node
        return True

    def search(self, target):
        return self._find(target) is not None

    def delete(self, target_data):
        # 빈 리스트
        if self.head is None:
            return False

        # head를 삭제하는 경우
        if self.head.data == target_data:
            if self.head == self.tail:  # 노드가 1개뿐 -> 공백 리스트
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head  # 원형 유지
            return True

        # 중간/마지막 노드를 삭제하는 경우
        prev = self.head
        current = self.head.next
        while current != self.head:  # 한 바퀴 돌 때까지
            if current.data == target_data:
                prev.next = current.next  # 삭제할 노드를 건너뛰어 연결
                if current == self.tail:  # 마지막 노드를 지웠다면 tail 갱신
                    self.tail = prev
                return True
            prev = current
            current = current.next

        # target이 리스트에 없는 경우
        return False

    def display(self):
        if self.head is None:
            print("리스트 공백")
            return

        elements = []
        current = self.head
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:  # 다시 head로 돌아오면 종료
                break

        print(" -> ".join(elements) + " -> (head)")


if __name__ == "__main__":
    cll = CircularLinkedList()

    print("--- 1. append & prepend 테스트 ---")
    cll.append(10)
    cll.append(20)
    cll.prepend(5)
    cll.display()  # 5 -> 10 -> 20 -> (head)

    print("\n--- 2. insert_after 테스트 ---")
    print(f"10 뒤에 15 삽입: {cll.insert_after(10, 15)}")  # True (중간)
    print(f"20 뒤에 25 삽입: {cll.insert_after(20, 25)}")  # True (tail 갱신)
    print(f"99 뒤에 1 삽입: {cll.insert_after(99, 1)}")    # False
    cll.display()  # 5 -> 10 -> 15 -> 20 -> 25 -> (head)

    print("\n--- 3. search 테스트 ---")
    print(f"15 존재 여부: {cll.search(15)}")  # True
    print(f"99 존재 여부: {cll.search(99)}")  # False

    print("\n--- 4. delete 테스트 ---")
    cll.delete(5)   # head 삭제
    cll.display()   # 10 -> 15 -> 20 -> 25 -> (head)

    cll.delete(15)  # 중간 노드 삭제
    cll.display()   # 10 -> 20 -> 25 -> (head)

    cll.delete(25)  # 마지막 노드 삭제
    cll.display()   # 10 -> 20 -> (head)

    print(f"없는 값(99) 삭제: {cll.delete(99)}")  # False

    print("\n--- 5. 삭제 후 tail 동작 확인 ---")
    cll.append(30)  # tail이 제대로 갱신됐다면 20 뒤에 붙음
    cll.display()   # 10 -> 20 -> 30 -> (head)