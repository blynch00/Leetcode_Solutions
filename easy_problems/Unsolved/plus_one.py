from typing import List
import collections

def plusOne(digits: List) -> List[int]:
    if len(digits) == 1 and digits[0] == 9:
        digits.pop()
        digits.append(1)
        digits.append(0)
        return digits
    final_index = len(digits) - 1
    if digits[final_index] == 9:
        while final_index >= 0:
            if digits[final_index] == 9:
                digits[final_index] = 0
                final_index -=1
            else:
                digits[final_index] += 1
                return digits
        if final_index <= 0:
            digits.insert(0, 1)
        
    else:
        digits[final_index] += 1
    return digits


list = [9,9,9]
print(plusOne(list))