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
    