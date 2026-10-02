"""
단순 연결 리스트 (Singly Linked List)
 
연산            시간복잡도
append          O(n)   tail 포인터가 없어서 마지막 노드까지 탐색
prepend         O(1)
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
 
 
class SinglyLinkedList:
    def __init__(self):
        self.head = None
 
    def append(self, data):
        node = Node(data)
        # 리스트가 비어있는 경우
        if self.head is None:
            self.head = node
            return
 
        # 마지막 노드까지 탐색
        current = self.head
        while current.next:
            current = current.next
 
        current.next = node
 
    def prepend(self, data):
        node = Node(data)
        node.next = self.head  # 새 노드의 next가 기존 head를 가리키게
        self.head = node       # head를 새 노드로 변경
 
    def insert_after(self, target_data, data):
        # target_data를 가진 노드 탐색
        current = self.head
        while current:
            if current.data == target_data:
                break
            current = current.next
 
        # 못 찾은 경우 (빈 리스트 포함)
        if current is None:
            return False
 
        node = Node(data)
        node.next = current.next  # 오른쪽 노드 연결을 먼저 백업
        current.next = node       # 그 다음 왼쪽 노드가 새 노드를 가리킴
        return True
 
    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False
 
    def delete(self, target):
        # 빈 리스트
        if self.head is None:
            return False
 
        # head를 삭제하는 경우
        if self.head.data == target:
            self.head = self.head.next
            return True
 
        # 중간/마지막 노드를 삭제하는 경우
        prev = self.head
        current = self.head.next
        while current:
            if current.data == target:
                prev.next = current.next  # 삭제할 노드를 건너뛰어 연결
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
        while current:
            elements.append(str(current.data))
            current = current.next
 
        print(" -> ".join(elements) + " -> None")
 
 
if __name__ == "__main__":
    sll = SinglyLinkedList()
 
    print("--- 1. append & prepend 테스트 ---")
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll.prepend(5)
    sll.display()  # 5 -> 10 -> 20 -> 30 -> None
 
    print("\n--- 2. insert_after 테스트 ---")
    print(f"20 뒤에 25 삽입: {sll.insert_after(20, 25)}")  # True
    print(f"99 뒤에 1 삽입: {sll.insert_after(99, 1)}")    # False
    sll.display()  # 5 -> 10 -> 20 -> 25 -> 30 -> None
 
    print("\n--- 3. search 테스트 ---")
    print(f"20 존재 여부: {sll.search(20)}")  # True
    print(f"99 존재 여부: {sll.search(99)}")  # False
 
    print("\n--- 4. delete 테스트 ---")
    sll.delete(5)   # head 삭제
    sll.display()   # 10 -> 20 -> 25 -> 30 -> None
 
    sll.delete(20)  # 중간 노드 삭제
    sll.display()   # 10 -> 25 -> 30 -> None
 
    sll.delete(30)  # 마지막 노드 삭제
    sll.display()   # 10 -> 25 -> None
 
    print(f"없는 값(99) 삭제: {sll.delete(99)}")  # False