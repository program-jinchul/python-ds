class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # 다음 노드를 가리킬 포인터
        self.prev = None  # 이전 노드를 가리킬 포인터


class DoublyLinkedList:
    def __init__(self):
        self.head = None  # 리스트의 첫 번째 노드를 가리키는 포인터
        self.tail = None  # 리스트의 맨 끝 노드를 추적하는 포인터 (append O(1) 최적화)

    def append(self, data):
        node = Node(data)
        # 리스트가 비어있는 경우 head와 tail 모두 새 노드를 가리킴
        if self.head is None:
            self.head = node
            self.tail = node
        # 리스트에 노드가 존재하는 경우 tail 뒤에 연결
        else:
            self.tail.next = node  # 기존 tail의 next를 새 노드로 지정
            node.prev = self.tail  # 새 노드의 prev를 기존 tail로 지정
            self.tail = node       # tail 명찰을 새 노드로 이동

    def prepend(self, data):
        node = Node(data)
        # 리스트가 비어있는 경우 head와 tail 모두 새 노드를 가리킴
        if self.head is None:
            self.head = node
            self.tail = node
        # 리스트에 노드가 존재하는 경우 head 앞에 연결
        else:
            node.next = self.head  # 새 노드의 next를 기존 head로 지정
            self.head.prev = node  # 기존 head의 prev를 새 노드로 지정
            self.head = node       # head 명찰을 새 노드로 이동

    def insert_after(self, target_data, data):
        # 1. 예외 처리: 리스트가 공백인 경우
        if self.head is None:
            print("리스트 공백")
            return False

        # target_data를 들고 있는 노드 탐색
        current = self.head
        while current:
            if current.data == target_data:
                break
            current = current.next

        # 2. 예외 처리: 찾는 target_data가 리스트에 없어서 current가 None이 된 경우
        if current is None:
            print(f"대상 노드({target_data})를 찾을 수 없음.")
            return False

        # 3. 정상적으로 노드를 찾은 경우 (current 뒤에 새 노드 삽입)
        node = Node(data)

        # 3-1: 새 노드의 next를 기존 current의 next로 연결
        node.next = current.next

        # 3-2: 새 노드의 prev를 current로 연결
        node.prev = current

        # 3-3: current의 다음 노드가 존재하는지 확인 (중간 삽입 vs 맨 끝 삽입)
        if current.next is not None:
            current.next.prev = node  # 오른쪽 노드의 prev를 새 노드로 변경
        else:
            self.tail = node          # current가 맨 끝(tail)이었다면 tail을 새 노드로 갱신

        # 3-4: current의 next를 새 노드로 최종 연결 (포인터 끊김 방지를 위해 마지막에 처리)
        current.next = node
        return True

    def delete(self, target_data):
        # 1. 예외 처리: 리스트가 비어있는 경우
        if self.head is None:
            print("리스트가 비어 있어 삭제할 수 없습니다.")
            return False

        current = self.head

        # target_data를 가진 노드 찾기
        while current:
            if current.data == target_data:
                break
            current = current.next

        # 2. 예외 처리: target_data를 찾지 못한 경우
        if current is None:
            print(f"삭제할 노드({target_data})를 찾을 수 없습니다.")
            return False

        # 3. 노드를 찾은 경우 - 삭제 케이스별 포인터 재연결
        
        # 케이스 A: 삭제할 노드가 head인 경우
        if current == self.head:
            self.head = current.next
            if self.head is not None:
                self.head.prev = None
            else:
                self.tail = None  # 노드가 1개뿐이었는데 삭제되어 공백 리스트가 된 경우

        # 케이스 B: 삭제할 노드가 tail인 경우 (elif 처리)
        elif current == self.tail:
            self.tail = current.prev
            if self.tail is not None:
                self.tail.next = None

        # 케이스 C: 중간 노드를 삭제하는 경우
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

        print(f"노드 {target_data} 삭제 완료.")
        return True

    def display(self, reverse=False):
        # 1. 예외 처리: 리스트가 비어있는 경우
        if self.head is None:
            print("리스트 공백")
            return

        elements = []

        # 2. 역방향 출력 (tail부터 prev 타고 이동)
        if reverse:
            current = self.tail
            while current:
                elements.append(str(current.data))
                current = current.prev
            print("None <-> " + " <-> ".join(elements))

        # 3. 정방향 출력 (head부터 next 타고 이동)
        else:
            current = self.head
            while current:
                elements.append(str(current.data))
                current = current.next
            print(" <-> ".join(elements) + " <-> None")


if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.prepend(5)
    dll.insert_after(20, 25)

    print("--- 초기 리스트 ---")
    dll.display()  # 5 <-> 10 <-> 20 <-> 25 <-> 30 <-> None

    print("\n--- 중간 노드(20) 삭제 테스트 ---")
    dll.delete(20)
    dll.display()  # 5 <-> 10 <-> 25 <-> 30 <-> None

    print("\n--- 맨 앞 노드(5) 삭제 테스트 ---")
    dll.delete(5)
    dll.display()  # 10 <-> 25 <-> 30 <-> None

    print("\n--- 맨 뒤 노드(30) 삭제 테스트 ---")
    dll.delete(30)
    dll.display()  # 10 <-> 25 <-> None

    print("\n--- 역방향 출력 확인 ---")
    dll.display(reverse=True)  # None <-> 25 <-> 10