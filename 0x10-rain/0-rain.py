#!/usr/bin/python3
""" calculate amount water retained between two walls
"""


def rain(walls):
    """ check how many square units of
    water will be retained after it rains """
    sum = 0
    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])
        sum += (min(left, right) - walls[i])
    return sum
