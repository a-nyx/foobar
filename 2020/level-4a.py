# Level 4a
# Question:
# Given two points, find the most flow which go to from the start to the end.
# The array gives the corridor capacities.

def solution(entrances, exits, path):
    # Step 1: Find all paths from entrances to exits
    totalFlow = 0
    paths = []
    pathStack = []
    for e in entrances:
        pathStack.append([e])

    while pathStack:
        thePath = pathStack.pop(0)
        lastNode = thePath[-1]
        for nextIndex in range(len(path[lastNode])):
            if path[lastNode][nextIndex] != 0:
                nextPath = thePath[:]
                if nextIndex not in nextPath:
                    nextPath.append(nextIndex)
                    if nextIndex in exits:
                        paths.append(nextPath)
                    else:              
                        pathStack.append(nextPath)
    # print(paths)
    # Step 2: For each path, find the max available flow
    for thePath in paths:
        # Find max available flow on the path
        maxFlow = path[thePath[0]][thePath[1]]
        for nodeIndex in range(1, len(thePath)-1):
            maxFlow = min(maxFlow, path[thePath[nodeIndex]][thePath[nodeIndex+1]])

        # Run the max on that flow and update the capacities
        totalFlow += maxFlow
        for nodeIndex in range(len(thePath)-1):
            path[thePath[nodeIndex]][thePath[nodeIndex+1]] -= maxFlow

    return totalFlow

# Test Cases
# path[A][B] = C => from A to B can fit C bunnies at each time step
print(solution([0, 1], [4, 5],
               [[0, 0, 4, 6, 0, 0],  # Room 0
                [0, 0, 5, 2, 0, 0],  # Room 1
                [0, 0, 0, 0, 4, 4],  # Room 2
                [2, 0, 0, 0, 6, 6],  # Room 3
                [0, 0, 0, 0, 0, 0],  # Room 4
                [0, 0, 0, 0, 0, 0]]))  # Room 5
# Answer: 16

print(solution([0], [3], 
                [[0, 7, 0, 0],  
                 [0, 0, 6, 0], 
                 [0, 0, 0, 8], 
                 [9, 0, 0, 0]]))
# Answer: 6
