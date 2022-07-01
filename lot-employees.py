"""
@Author: Hossein Agharezaei
@Date: 1Jul2022
@Repository: https://github.com/h-agharezaei/quiz-quera-ir
@Links: https://quera.org/problemset/10636/
"""
n = int(input())
names = []
max=0
for i in range(n):
  name = input().split()[0]
  names.append(name)
  if names.count(name) > max:
    max = names.count(name)

print(max)