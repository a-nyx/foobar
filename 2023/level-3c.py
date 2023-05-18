#!/usr/bin/env python2.7.13

# Level 3c
# Question: Given a number find the minimum number of operations to reach at 1.
# Operations allowed:
# 1. Subtract 1
# 2. Add 1
# 3. Divide by 2 (only if divisible by 2)
# Maximum input length: 309 digits

try:
    import Queue as queue
except ImportError:
    import queue

def solution(s):
    n = long(s)
    q = queue.Queue()
    visited = { n }
    q.put(( n, 0) )

    while not q.empty():
      number, step = q.get()

      if number == 1:
        return step

      if number - 1 not in visited:
        q.put(( number - 1, step + 1 ))
        visited.add(number - 1)

      if number + 1 not in visited:
        q.put(( number + 1, step + 1 ))
        visited.add(number + 1)

      if number % 2 == 0 and number / 2 not in visited:
        q.put(( number / 2, step + 1 ))
        visited.add(number / 2)


# Test Cases
print(solution('4')) # 2
print(solution('15')) # 5
