"""
@Author: Hossein Agharezaei
@Date: 6Jul2022
@Repository: https://github.com/h-agharezaei/quiz-quera-ir
@Links: https://quera.org/problemset/2530/
"""

s = input()
list = []
list.append(s)
for i in range(len(s)):  
  if s[i] == 'T':
    x = s.replace(s[i],'K')
    y = s[:i] + 'K' + s[i+1:]
  elif s[i] == 'D':
    x = s.replace(s[i],'G')
    y = s[:i] + 'G' + s[i+1:]
  elif s[i] == 'L':
    x = s.replace(s[i],'R')
    y = s[:i] + 'R' + s[i+1:]
  elif s[i] == 'F':
    x = s.replace(s[i],'R')
    y = s[:i] + 'R' + s[i+1:]
  z = s.replace('F','R')
  z = z.replace('L','R')

  if x not in list:
    list.append(x)
  if y not in list:
    list.append(y)
  if z not in list:
    list.append(z)

print(len(list))

