"""""""""""
단일 구조 리스트
"""""""""""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)
        # 1. 리스트가 비어있는 경우(head가 None)
        if self.head is None:
            self.head = node
            return

        # 2. 노드가 이미 있으면 head부터 탐색 시작
        current = self.head

        # current.next가 None이 아닐 때까지 탐색
        while current.next:
            current = current.next

        # 마지막 노드의 next에 새 노드 연결
        current.next = node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head # 새 노드 next가 head 가리키게
        self.head = new_node # head의 주소를 새 노드로 변경

    def display(self):
        current = self.head

        # 순회하면서 노드의 data를 담을 리스트
        elements = []

        # current가 None이 될 때까지 이동
        while current:
            elements.append(str(current.data))
            current = current.next

        # 출력
        elements.append("None")
        print("->".join(elements))

    def search(self, target):
        current = self.head

        while current:
            if current.data == target:
                return True
            current = current.next
            
        return False

    def delete(self, target):
        # 리스트가 비어있는 경우
        if self.head is None:
            return False

        # 삭제할게 head인 경우
        if self.head.data == target:
            self.head = self.head.next # head를 다음 노드로 변경
            return True

        # 중간이나 맨 끝의 노드를 삭제하는 경우
        prev = None
        current = self.head

        while current:
            if current.data == target:
                # 이전 노드의 next를 삭제할 노드의 next로 연결
                prev.next = current.next
                return True
            
            # 탐색을 위해 이전 노드와 현재 노드를 한 칸씩 이동
            prev = current
            current = current.next
        
        # 지우려는 target이 리스트에 존재하지 않는 경우
        return False


if __name__ == "__main__":
    sll = SinglyLinkedList()
    
    # 1. 요소 추가
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll.prepend(5)
    print("초기 리스트:")
    sll.display()  # 출력: 5 -> 10 -> 20 -> 30 -> None

    # 2. 탐색
    print(f"20 존재 여부: {sll.search(20)}")  # True
    print(f"99 존재 여부: {sll.search(99)}")  # False

    # 3. head 삭제 (5 삭제)
    sll.delete(5)
    print("head(5) 삭제 후:")
    sll.display()  # 출력: 10 -> 20 -> 30 -> None

    # 4. 중간 노드 삭제 (20 삭제)
    sll.delete(20)
    print("중간 노드(20) 삭제 후:")
    sll.display()  # 출력: 10 -> 30 -> None

    # 5. 마지막 노드 삭제 (30 삭제)
    sll.delete(30)
    print("마지막 노드(30) 삭제 후:")
    sll.display()  # 출력: 10 -> None