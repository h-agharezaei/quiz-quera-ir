"""
@Author: Hossein Agharezaei
@Date: 7Jul2022
@Repository: https://github.com/h-agharezaei/quiz-quera-ir
@Links: https://quera.org/problemset/26651/
"""
n = int(input())
a =  input().split()
b =  input().split()
c = 0
for i in range(n):
  c += int(a[i]) * int(b[i])
print(c)
