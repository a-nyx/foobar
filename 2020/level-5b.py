# Level 5b
# Question:
# Find the sum of
# floor(1*sqrt(2)) + floor(2*sqrt(2)) + floor(3*sqrt(2))...

from decimal import Decimal, getcontext
getcontext().prec = 101


def solution(s):
    # Formula & Proof given here: https://math.stackexchange.com/a/2053713
    n = long(s)

    if n < 1:
        return "0"
    elif n == 1:
        return "1"
    else:
        sq = 1 / (Decimal(2).sqrt() - 1)
        n_ = long(n//sq)
        return str(n*n_ + (n*(n+1))/2 - (n_*(n_+1))/2 - long(solution(n_)))

### TEST CASES ###
print(solution('5'))    #19
print(solution('77'))   #4208
print(solution('777777'))

