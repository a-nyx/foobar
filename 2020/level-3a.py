# Level 3a
# Question:
# Given a map with 0's and 1's. 0's are passables and 1's are walls.
# Find the shortest path from top-left to bottom-right.
# We are allowed to remove 1 wall.
# It's always solvable. Top-left and bottom-right are always 0.
# Height and width can be from 2 to 20. 

try:
    import Queue as queue
except ImportError:
    import queue

class Point:
    def __init__(self, x, y, dist, wall):
        self.x = x
        self.y = y
        self.dist = dist
        # @param "wall" is the flag showing if a wall so far is removed or not
        # for one point, there are two possibilities:
        # reached by or without removing  wall 
        self.wall = wall


def solution(map):
    # Initialization
    rows = len(map)
    cols = len(map[0])
    start = Point(0, 0, 1, 0)
    end = Point(rows-1, cols-1, rows*cols, 0)
    q = queue.Queue(rows*cols)
    q.put(start)
    visited = [[0 for i in range(cols)] for j in range(rows)]
    visited[0][0] = 2 # 0-Not visited 1-Visited by removing one wall 2-Visited w/o removing wall

    # Main Algo
    while not q.empty():

        current = q.get()
        # print("x: " + str(current.x) + ", y: " + str(current.y) + ", dist: " + str(current.dist) + ", wall: " + str(current.wall))

        # If reached the end
        if current.x == end.x and current.y == end.y:
            return current.dist

        # Right
        if current.y < cols-1:
            nextX = current.x
            nextY = current.y + 1
            if current.wall + map[nextX][nextY] < 2 and (visited[nextX][nextY] == 0 or (visited[nextX][nextY] == 1 and current.wall + map[nextX][nextY] == 0)):
                q.put(Point(nextX, nextY, current.dist + 1, current.wall + map[nextX][nextY]))
                visited[nextX][nextY] = 2 - current.wall + map[nextX][nextY]

        # Left
        if current.y > 0:
            nextX = current.x
            nextY = current.y - 1
            if current.wall + map[nextX][nextY] < 2 and (visited[nextX][nextY] == 0 or (visited[nextX][nextY] == 1 and current.wall + map[nextX][nextY] == 0)):
                q.put(Point(nextX, nextY, current.dist + 1, current.wall + map[nextX][nextY]))
                visited[nextX][nextY] = 2 - current.wall + map[nextX][nextY]

        # Down
        if current.x < rows-1:
            nextX = current.x + 1
            nextY = current.y
            if current.wall + map[nextX][nextY] < 2 and (visited[nextX][nextY] == 0 or (visited[nextX][nextY] == 1 and current.wall + map[nextX][nextY] == 0)):
                q.put(Point(nextX, nextY, current.dist + 1, current.wall + map[nextX][nextY]))
                visited[nextX][nextY] = 2 - current.wall + map[nextX][nextY]

        # Up
        if current.x > 0:
            nextX = current.x - 1
            nextY = current.y
            if current.wall + map[nextX][nextY] < 2 and (visited[nextX][nextY] == 0 or (visited[nextX][nextY] == 1 and current.wall + map[nextX][nextY] == 0)):
                q.put(Point(nextX, nextY, current.dist + 1, current.wall + map[nextX][nextY]))
                visited[nextX][nextY] = 2 - current.wall + map[nextX][nextY]

    return "Something went wrong!"

# Test Cases
print(solution([[0, 1, 1, 0],
                [0, 0, 0, 1], 
                [1, 1, 0, 0], 
                [1, 1, 1, 0]]))  # 7

print(solution([[0, 0, 0, 0, 0, 0], 
                [1, 1, 1, 1, 1, 0], 
                [0, 0, 0, 0, 0, 0], 
                [0, 1, 1, 1, 1, 1], 
                [0, 1, 1, 1, 1, 1], 
                [0, 0, 0, 0, 0, 0]]))  # 11

