from typing import List
def getRow(rowIndex: int) -> List[int]:
    triangle_arr = [[0] * x for x in range(1, rowIndex + 2)]
    triangle_arr[0] = [0]
    
    for x in range(1, rowIndex + 2):
        for y in range(0, x):
            if y == 0 or y == x-1:
                triangle_arr[x-1][y] = 1
            else:
                triangle_arr[x-1][y] = triangle_arr[x-2][y] + triangle_arr[x-2][y-1]
    print(triangle_arr)
    return triangle_arr[rowIndex]

print(getRow(3))