# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.

# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


def isHappy(n: int) -> bool:
    if n == 1:
        return True
    seen = set()
    seen.add(n)
    
    while True:
        new_num = 0
        for num_x in str(n):
            new_num += (int(num_x)) * (int(num_x))
        if new_num == 1:
            return True
        elif new_num in seen:
            return False
        else:
            seen.add(n)
            n = new_num
    
print(isHappy(2))