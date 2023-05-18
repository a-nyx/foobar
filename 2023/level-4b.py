#!/usr/bin/env python2.7.13

# Level 4b
# Question: Given a room, your position, trainer's position, and the distance you can shoot...
# Return the number of distinct directions you can hit the trainer with a laser gun.
# The walls are mirrors, so the laser will bounce off the walls.

import math

try:
    import Queue as queue
except ImportError:
    import queue

def get_distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def get_angle(x1, y1, x2, y2):
    return math.atan2(y2-y1, x2-x1)

def get_4_reflections(x, y, top, right, bottom, left, max_distance, origin_x, origin_y):
    reflections = set()

    bottom = (x, y - 2*(y-bottom))
    if get_distance(origin_x, origin_y, bottom[0], bottom[1]) <= max_distance:
        reflections.add(bottom)

    top = (x, y + 2*(top-y))
    if get_distance(origin_x, origin_y, top[0], top[1]) <= max_distance:
        reflections.add(top)

    left = (x - 2*(x-left), y)
    if get_distance(origin_x, origin_y, left[0], left[1]) <= max_distance:
        reflections.add(left)

    right = (x + 2*(right-x), y)
    if get_distance(origin_x, origin_y, right[0], right[1]) <= max_distance:
        reflections.add(right)

    return reflections

def get_all_reflections(dimensions, your_position, trainer_position, distance):
    reflections = {}
    q = queue.Queue()
    visited = set()

    q.put((your_position[0], your_position[1], 500))
    visited.add((your_position[0], your_position[1]))
    reflections[999] = (your_position[0], your_position[1], 0, 500)

    angle = get_angle(your_position[0], your_position[1], trainer_position[0], trainer_position[1])
    diff = get_distance(your_position[0], your_position[1], trainer_position[0], trainer_position[1])
    q.put((trainer_position[0], trainer_position[1], 600))
    visited.add((trainer_position[0], trainer_position[1]))
    reflections[angle] = (trainer_position[0], trainer_position[1], diff, 600)

    while not q.empty():
        current = q.get()
        four_reflections = get_4_reflections(current[0], current[1], dimensions[1], dimensions[0], 0, 0, distance, your_position[0], your_position[1])

        for reflection in four_reflections:
            if reflection in visited:
                continue

            visited.add(reflection)
            angle = get_angle(your_position[0], your_position[1], reflection[0], reflection[1])
            diff = get_distance(your_position[0], your_position[1], reflection[0], reflection[1])

            if angle in reflections:
              if reflections[angle][2] < distance:
                  if not (reflections[angle][0] == your_position[0] and reflections[angle][1] == your_position[1]):
                      continue

            reflections[angle] = (reflection[0], reflection[1], diff, current[2])
            q.put((reflection[0], reflection[1], current[2]))

    return reflections

def solution(dimensions, your_position, trainer_position, distance):
    if get_distance(your_position[0], your_position[1], trainer_position[0], trainer_position[1]) > distance:
        return 0

    reflections = get_all_reflections(dimensions, your_position, trainer_position, distance)
    count = 0

    for reflection in reflections:
        if reflections[reflection][3] == 600:
            count += 1

    return count

print(solution([3,2], [1,1], [2,1], 4)) # 7
print(solution([300,275], [150,150], [185,100], 500)) # 9
print(solution([10, 10], [9,9], [1,1], 2)) # 0
print(solution([10, 10], [9,9], [1,1], 10000))
