class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = [char.lower() for char in s if char.isalnum()]
        p1, p2 = 0, len(string) - 1

        while p1 < p2:
            if string[p1] != string[p2]:
                return False
            p1 += 1
            p2 -= 1

        return True
        