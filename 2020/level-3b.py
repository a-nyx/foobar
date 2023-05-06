# Level 3b
# Question:
# Given a list of positive integers, count the triples(x, y, z) that
# x divides y, y divides z and the indices meet the requirement lx<ly<lz

def solution(l):
    allMultiples = {}

    # Store the multiples of each
    for i in range(len(l)):
        multiples = []
        for j in range(i+1, len(l)):
            if l[j] % l[i] == 0:
                multiples.append(j)    
        if multiples:
            allMultiples[i] = multiples

    count = 0
    # if a multiple has its own multiple, increase the count
    for v in allMultiples.values():
        for multiple in v:
            if multiple in allMultiples:
                count += len(allMultiples[multiple])

    return count

# Test Cases
print(solution([1, 2, 3, 4, 5, 6])) #3
print(solution([1, 1, 1]))          #1



