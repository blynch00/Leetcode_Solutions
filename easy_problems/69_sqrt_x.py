def mySqrt(x: int) -> int:
    for index in range (0, x+1):
        if index * index < x:
            continue
        elif index * index == x:
            return index
        else: # It's larger
            if (index-1) * (index-1) < x:
                return (index - 1 )
    return 0
