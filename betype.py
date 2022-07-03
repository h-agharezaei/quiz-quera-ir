
"""
@Author: Hossein Agharezaei
@Date: 3Jul2022
@Repository: https://github.com/h-agharezaei/quiz-quera-ir
@Links: https://quera.org/problemset/28948/
"""
s = input()
count_equal = s.count('=')
for i in range(s.count('=')):
  index = s.find('=')
  if index == 0:
    s = s[index + 1::]
  else:
    s = s[0:index - 1:]+s[index + 1::]
print(s)