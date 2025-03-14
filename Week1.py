# 리스트 컴프리헨션
result = [x for x in range(10) if x % 2 == 1]
print(result)

# 리스트 컴프리헨션 2차원 리스트 초기화
n = 3
m = 4
array = [[0]*m]*n
result = [[0]*m for _ in range(n)]
print(array)
print(result)

array[1][1] = 5
print(f"array: {array}")

result[1][1] = 5
print(f"list comprehension: {result}")

array2 = []
for _ in range(n):
  array2.append([0]*m)
array2[1][1] = 5
print(f"array2: {array2}")

# --------------------------
print()

a = [1, 4, 3]
print("기본리스트 : ", a)

# 리스트에 원소 삽입
a.append(2)
print("삽입: ", a)
print(f"삽입: {a}")

# 리스트에 원소 삽입(extend)
a.extend([5, 11])
print("extend: ", a)  

# 오름차순 정렬
a.sort()
print(f"오름차순 정렬 : {a}")

# 내림차순 정렬
a.sort(reverse=True)
print(f"내림차순 정렬 : {a}")

# 리스트 원소 뒤집기
a.reverse()
print(f"원소 뒤집기 : {a}")

# 특정 인덱스에 데이터 추가
a.insert(2, 3)
print(f"인덱스 2에 3 추가 : {a}")

# 특정 값인 데이터 개수 세기
print(f"값이 3인 데이터 개수: {a.count(3)}")

# 특정 값 데이터 삭제
a.remove(1)
print(f"값이 1인 데이터 삭제 : {a}")

# 리스트에서 특정 값을 가지는 원소 모두 제거
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in a if i not in remove_set]
print(result)

# --------------------------
print()

data = "Hello Wolrd"
print(data)

data = "Don't you know \"Python\"?"
print(data)

# 문자열 연산
a = "Hello"
b = "World"
print(a + " " + b)

# 문자열 반복
print(a * 3)

print(a[0:3])

a = ['he','llo']
b = ['wol','rld']
print(a + b)
# --------------------------
print()