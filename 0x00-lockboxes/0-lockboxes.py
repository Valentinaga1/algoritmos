#!/usr/bin/python3
"""
    Determine if the boxes can be unlocked by other boxes' values
    @boxes: 2d array of boxes with values inside them
    Returns: True or False
"""


def canUnlockAll(boxes):
    """
    boxes --> List of Lists, it contains the boxes with keys
    Reurn boolean
    """
    myKeys = [0]
    for key in myKeys:
        for boxKey in boxes[key]:
            if boxKey not in myKeys and boxKey < len(boxes):
                myKeys.append(boxKey)
    if len(myKeys) == len(boxes):
        return True
    return False