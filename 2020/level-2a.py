# Level 2a
# Question: 
# The numbers go in a triangle this way:
#   7 
#   4  8
#   2  5  9
#   1  3  6  10
#
#   The bottom-left point has the coordinates (1, 1).
#   Given the coordinates, find the number and return as string

def solution(x, y):
    return str(int((x*x + y*y + 2*x*y - x - 3*y + 2)/2))

# Test Cases
print(solution(5,10))  # 96
print(solution(3, 2))  # 9

