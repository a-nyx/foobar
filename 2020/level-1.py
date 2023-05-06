# Level 1
# Question: Given a list, remove the elements occuring more than the given limit

def solution(data, n):
    '''
    Return the updated list
    Time Complexity: O(n)
    '''

    counts = {}
    result = []
    # Count items and store into a dictionary for faster lookup
    for item in data:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1

    # Select the elements met the requirement
    for item in data:
        if counts[item] <= n:
            result.append(item)

    return result


# Test Cases
print(solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1))  # [1, 4]
print(solution([1, 2, 3], 0))                    # []
print(solution([1, 1, 5, 5, 7, 7, 7], 2))        # [1, 1, 5, 5]
