"""Exercism Python Track - Grains exercise

Module provides functions that calculate the number of grains on a given chessboard square and 
the total number of grains on the chessboard
"""

def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    return 2 ** 64 - 1
