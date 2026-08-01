class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if len(str(x)) == 1:
            return True

        new_list = list(str(x))


        start_pointer = 0
        end_pointer = len(new_list) - 1

        while end_pointer >= start_pointer:
            if new_list[end_pointer] != new_list[start_pointer]:
                return False
            start_pointer += 1
            end_pointer -= 1
        return True
                