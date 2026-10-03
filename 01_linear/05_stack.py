"""
class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        # 원래 파이썬은 동적배열 여기선 정적 배열로 구현하기 때문에 [None] * capacity를 이용하여 공간확보
        self.stack = [None] * capacity
        self.top = -1

    def is_full(self):
        return self.top == self.capacity - 1

    def is_empty(self):
        return self.top == -1
    
    def push(self, data):
        if self.is_full():
            return False
        
        self.top += 1
        self.stack[self.top] = data
        return True

    def pop(self):
        if self.is_empty():
            return None
        
        data = self.stack[self.top] # 데이터를 잃어버리지 않게 값 저장

        self.top -= 1 # top -1 하고

        return data # 저장했던 값 출력

    def peek(self):
        if self.is_empty():
            return None

        data = self.stack[self.top]

        return data

    def size(self):
        return self.top + 1

    def display(self):
        if self.is_empty():
            return print("스택 공백")

        elements = [str(self.stack[i]) for i in range(self.top + 1)]

        print(" -> ".join(elements) + " (top)")

s = Stack(3)
print(s.pop())      # None
s.push(1); s.push(2); s.push(3)
print(s.push(4))    # False
s.display()         # 1 -> 2 -> 3 (top)
print(s.pop())      # 3
print(s.peek())     # 2
print(s.size())     # 2
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

        self.count += 1

    def pop(self):
        if self.is_empty():
            return None
        
        data = self.head.data # 똑같이 삭제하기 전에 head 저장
        self.head = self.head.next
        self.count -= 1

        return data

    def peek(self):
        if self.is_empty():
            return None

        return self.head.data

    def size(self):
        return self.count

    def display(self):
        if self.is_empty():
            print("스택 공백")
            return

        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next

        elements.reverse()
        print(" -> ".join(elements) + " (top)")


s = LinkedStack()
print(s.pop())      # None
s.push(1); s.push(2); s.push(3)
s.display()         # 1 -> 2 -> 3 (top)
print(s.pop())      # 3
print(s.peek())     # 2
print(s.size())     # 2