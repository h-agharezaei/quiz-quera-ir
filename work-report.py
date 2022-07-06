"""
@Author: Hossein Agharezaei
@Date: 7Jul2022
@Repository: https://github.com/h-agharezaei/quiz-quera-ir
@Links: https://quera.org/problemset/49535/
"""
n, k = map(int, input().split())
result = 'YES'
c = 0
for i in range(n):
  c += int(input())
  if k > c:
    result = 'NO'
  else:
    result = 'YES'
print(result)
