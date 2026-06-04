class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Start in the top right corner
        # Two directions; down and left
        # If the number is larger than target, we are higher, and move left
        # If the number is smaller, we move down
        # If the number matches, return True
        # If the number we are on is not the number we are looking for, the number left is smaller, and below is larger, return False


        row, column = 0, len(matrix[0]) - 1

        while row >= 0 and column >= 0:
            num = matrix[row][column]
            if num == target:
                return True
            if num > target:
                column -= 1
                if column < 0:
                    return False
            elif num < target:
                row += 1
                if row > len(matrix) - 1:
                    return False
            else:
                return False
        return False