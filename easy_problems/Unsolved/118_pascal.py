from typing import List
def generate(numRows: int) -> List[List[int]]:

    return_arr = [[None]*x for x in range(1, numRows + 1)]

    # Set first value of an array to 1;  numRows >= 1 
    return_arr[0][0] = 1

    for x in range(1,numRows):
        for y in range(len(return_arr[x])):
            # Case for edges
            if y == 0 or y == len(return_arr[x])-1:
                return_arr[x][y] = 1
            # Case for internals
            else:
                return_arr[x][y] = return_arr[x-1][y-1] + return_arr[x-1][y]




    return(return_arr)

numRows = 5
triangle = generate(5)

for x in range(0, len(triangle)):
    print(f"{triangle[x]}\n")