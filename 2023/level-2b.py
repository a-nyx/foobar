# Level 2b
# Question: calculate the number of salutes
# three chars: > going right, - empty, < going left
# salutes happen when two people cross paths
# everyone will walk to the end of their direction


def solution(s):
    salute = 0
    going_right = 0

    for i in range(len(s)):
      char = s[i]
      if char == '>':
        going_right += 1
      elif char == '<':
        salute += going_right

    return salute * 2

# Test Cases
print(solution(">----<")) # 2
print(solution("<<>><")) # 4
print(solution("--->-><-><-->-")) # 10
