from typing import *
from collections import *
from random import randint
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess(num:int)-> int:
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        middle = (low + high) //2

        while True:
            middle = (low + high) // 2
            if guess(middle) == -1:
                high = middle -1
            elif guess(middle) == 1:
                low = middle + 1
            else:
                return middle

        return middle
        