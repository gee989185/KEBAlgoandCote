"""
# set
data = set([1,1,2,3,4,5])
print(data)

data = {1,1,2}
print(data)

a = set([1,2,3,4,5])
b = set([3,4,5,6,7])
print(a) ; print(b)
print(f"a | b(union): {a | b}") # union
print(f"a & b(intersection): {a & b}") # intersection
print(f"a - b(difference): {a - b}") # difference
print(f"a ^ b(symmetric difference): {a ^ b}") # symmetric difference

"""
"""
data = set([1,2,3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

# 새로운 원소 여러개 추가
data.update([5,6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)
"""
# 조건문 
"""
score = int(input(f"점수를 입력하세요: "))
if score >= 90:
  print("학점: A")
elif score >= 80:
  print("학점: B")
elif score >= 70:
  print("학점: C")
else:
  print("학점: F")

if score >=80:
  pass # 나중에 작성할 소스코드
else:
  print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')

if score >=80: result = 'Success'
else: result = 'Fail'

result = 'Success' if score >= 80 else 'Fail'
print(result)
"""
# ----------------------------------------------
"""
a = [1,2,3,4,5,5,5]
remove_set = {3,5}

result = []
for i in a:
  if i not in remove_set:
    result.append(i)

print(result)

result = [i for i in a if i not in remove_set] # list comprehension
print(result)
"""
# ----------------------------------------------
