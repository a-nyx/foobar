# Level 1
# Question: Given a starting index, return the 5 digits of the string formed by concatenating all the prime numbers: "2357111317192329..."

from math import sqrt


def is_prime(n):
    if (n > 1):
        for i in range(2, n):
            if (n % i == 0):
                return False
        return True
    return False


def solution(i):
    index = -1
    id = ''
    k = 2

    while index < 10001:
        if (is_prime(k)):
            index += len(str(k))
            if (index >= i):
                id += str(k)[-(index+1 - i):]

        if (len(id) >= 5):
            return id[:5]

        k += 1


# Test Cases
print(solution(0))  # 23571
print(solution(3))  # 71113
print(solution(5))  # 11317
