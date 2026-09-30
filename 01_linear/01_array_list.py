"""
01_array_list.py
파이썬 리스트(동적 배열)의 주요 연산과 시간 복잡도 정리
"""

# 1. 리스트 생성
arr = [10, 20, 30, 40]
print(f"초기 리스트: {arr}")

# 2. 인덱싱 (Indexing / Access) -> O(1)
# 메모리 주소를 바로 계산해서 접근하므로 요소 개수와 상관없이 즉시 접근
element = arr[2]
print(f"인덱스 2의 요소: {element}  # O(1)")

# 3. 맨 뒤에 추가 (Append) -> O(1)
# 연속된 메모리 공간 끝에 추가하므로 즉시 수행 (가끔 메모리 재할당 발생 시 O(N)이지만 평균적으로 O(1))
arr.append(50)
print(f"append(50) 후: {arr}  # O(1)")

# 4. 맨 뒤 요소 삭제 (Pop) -> O(1)
# 마지막 요소만 제거하면 되므로 O(1)
last_val = arr.pop()
print(f"pop() 후: {arr} (삭제된 값: {last_val})  # O(1)")

# 5. 중간/맨 앞 삽입 (Insert) -> O(N)
# 지정한 인덱스 뒤의 모든 요소들을 한 칸씩 뒤로 밀어내야(Shift) 하므로 O(N)
arr.insert(1, 15)
print(f"insert(1, 15) 후: {arr}  # O(N)")

# 6. 중간/맨 앞 삭제 (Pop with Index) -> O(N)
# 삭제된 빈자리를 채우기 위해 뒤의 모든 요소들을 한 칸씩 앞으로 당겨야 하므로 O(N)
first_val = arr.pop(0)
print(f"pop(0) 후: {arr} (삭제된 값: {first_val})  # O(N)")

# 7. 값으로 탐색 (Search / Index) -> O(N)
# 원하는 값이 나올 때까지 처음부터 끝까지 순회해야 함
idx = arr.index(30)
print(f"값 30의 인덱스: {idx}  # O(N)")