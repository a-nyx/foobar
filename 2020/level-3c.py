# Level 3c
# Question:
# Startin from the pair (1, 1). We can add the left one to the right
# or the right one to the left in each step.
# Given a pair, find the number of steps to reach it.
# Ex: (1, 2) => 1 step, (3, 2) => two steps

def solution(x, y):
    x = int(x)
    y = int(y)
    step = 0
    while x != 1 or y != 1:
        # print(str(x) + "---" + str(y))
        if x == y or x < 1 or y < 1:
            return "impossible"

        if x == 1 or y == 1:
            step += max(x, y) - 1
            break

        if x < y:
            step += int(y/x)
            y = y % x
        else:
            step += int(x/y)
            x = x % y
    
    return str(step)

# Test Cases
print(solution('1', '2'))       # 1
print(solution('90', '1'))      # 89
print(solution('90', '3'))      # impossible
print(solution("5555567", "4"))
