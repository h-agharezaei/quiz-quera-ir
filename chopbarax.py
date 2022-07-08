"""
@Author: Hossein Agharezaei
@Date: 8Jul2022
@Repository: https://github.com/h-agharezaei/quiz-quera-ir
@Links: https://quera.org/problemset/3405/
"""
list = []
while True:
  n = int(input())
  if n != 0:
    list.append(n)
  else:
    for i in reversed(list):
      print(i)
    break
