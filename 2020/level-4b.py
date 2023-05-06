# Level 4b
# Question:
# Return the number of nodes can be visited within the time limit.
# Array gives the times spent from one point to another.
# Note that travel one to another can save time!

from itertools import permutations
import copy


def find_shortests_for_one(times, index):
    # initial distances
    s = []
    for i in range(len(times[index])):
        if i == 0:
            s.append(0)
        else:
            s.append(float("inf"))
    
    # Swap nodes and make the index-th one starter
    times_copy = copy.deepcopy(times)
    if index > 0:
        times_copy[0], times_copy[index] = times_copy[index], times_copy[0]
        # swap columns
        for k in range(len(times_copy)):
            times_copy[k][index], times_copy[k][0] = times_copy[k][0], times_copy[k][index]

    # Find shortests: Bellman Ford
    for m in range(len(times_copy)-1):
        for i in range(len(times_copy)):
            for j in range(len(times_copy[i])):
                if s[j] > times_copy[i][j] + s[i] and s[i] != float("inf"):
                    s[j] = times_copy[i][j] + s[i]
    
    # Check if there is negative cycle
    if index == 0:
        for i in range(len(times_copy)):
            for j in range(len(times_copy[i])):
                if s[j] > times_copy[i][j] + s[i] and s[i] != float("inf") and i != j:
                    # Negative cycle!
                    print("negative")
                    return -1
    return s


def find_all_shortests(times):

    s_all = []
    for i in range(len(times)):
        s = find_shortests_for_one(times, i)
        if s == -1:
            # Negative cycle!
            return -1
        else:
            s[i], s[0] = s[0], s[i]
            s_all.append(s)
    return s_all


def find_path_time(shortests, path):
    time = 0
    current = 0
    for i in range(len(path)):
        next = path[i] + 1 # Bunny 0: Index 1
        time += shortests[current][next]
        current = next
    time += shortests[current][len(shortests)-1]
    return time


def solution(times, times_limit):

    if len(times) <= 2:
        return []

    bunnies = [num for num in range(len(times)-2)]

    # Step 1: Find shortest paths between nodes
    shortests = find_all_shortests(times)
    
    # Step 2: Check if there is negative cycle
    if shortests == -1:
        return bunnies

    # Step 3: Compare all chances
    answer = []
    for i in range(len(bunnies), 1, -1):
        perm = permutations(bunnies, i)
        for p in list(perm):
            time = find_path_time(shortests, p)
            if time <= times_limit:
                l = sorted(p)
                if not answer:
                    answer = l
                else:
                    # Pick one with lowest indexes
                    for n in range(len(l)):
                        if answer[n] > l[n]:
                            answer = l
                            break
                        elif l[n] > answer[n]:
                            break
        if answer:
            return answer
    return []

# TEST CASES
# case1 = [[0, 1, 1, 1, 1],
#          [1, 0, 1, 1, 1],
#          [1, 1, 0, 1, 1],
#          [1, 1, 1, 0, 1],
#          [1, 1, 1, 1, 0]]
# print("CASE 1:", end=" ")
# print(solution(case1, 3))

case2 = [[0, 2, 2, 2, -1],
         [9, 0, 2, 2, -1],
         [9, 3, 0, 2, -1],
         [9, 3, 2, 0, -1],
         [9, 3, 2, 2, 0]]
print("")
print("CASE 2:")
print(solution(case2, 1)) # [1, 2]

# case3 = [[0, 2, 2, 2, -1],
#          [9, 0, 2, 2, 0],
#          [9, 3, 0, 2, 0],
#          [9, 3, 2, 0, 0],
#          [-1, 3, 2, 2, 0]]
# print("CASE 3:", end=" ")
# print(solution(case3, -500))

# case4 = [[1, 1, 1, 1, 1, 1, 1],
#          [1, 1, 1, 1, 1, 1, 1],
#          [1, 1, 1, 1, 1, 1, 1],
#          [1, 1, 1, 1, 1, 1, 1],
#          [1, 1, 1, 1, 1, 1, 1],
#          [1, 1, 1, 1, 1, 1, 1],
#          [1, 1, 1, 1, 1, 1, 1]]
# print("CASE 4:", end=" ")
# print(solution(case4, 1))

# case5 = [[1, 1, 1],
#          [1, 1, 1],
#          [1, 1, 1]]
# print("CASE 5:", end=" ")
# print(solution(case5, 2))

case6 = [[0, 5, 11, 11, 1],
         [10, 0, 1, 5, 1],
         [10, 1, 0, 4, 0],
         [10, 1, 5, 0, 1],
         [10, 10, 10, 10, 0]]

print("CASE 6:")
print(solution(case6, 10)) # [0,1]

# case7 = [[0, 10, 10, 10, 1],
#          [0, 0, 10, 10, 10],
#          [0, 10, 0, 10, 10],
#          [0, 10, 10, 0, 10],
#          [1, 1, 1, 1, 0]]
# print("CASE 7:", end=" ")
# print(solution(case7, 5))

# case8 = [[0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0]]
# print("CASE 8:", end=" ")
# print(solution(case8, 1))

# case9 = [[2, 2],
#          [2, 2]]
# print("CASE 9:", end=" ")
# print(solution(case9, 1))

# case10 = [[0, 10, 10, 1, 10],
#           [10, 0, 10, 10, 1],
#           [10, 1, 0, 10, 10],
#           [10, 10, 1, 0, 10],
#           [1, 10, 10, 10, 0]]
# print("CASE 10:", end=" ")
# print(solution(case10, 6))

