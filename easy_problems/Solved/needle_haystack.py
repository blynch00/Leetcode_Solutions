class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
        # or -1 if needle is not part of haystack.

        ## SLIDING WINDOW: look at the the string from current position to len(needle) - 1, if still within string
            # If all positions match up, return current index
            # Otherwise, increment current index and check there

        # Can use string splicing: [start index : end index]

        for x in range(len(haystack)):
            #print(f"X:{x}")
            if x + len(needle) - 1 <= len(haystack) - 1:
                index = 0
                substring = ""
                while x + index <= len(haystack)-1 and index <= len(needle) - 1 and haystack[x + index] == needle[index]:
                    substring += haystack[x + index]
                    index += 1
                    #print(f"Substring: {substring}")
                if substring == needle:
                    return x
                                    
        
        return -1

sol = Solution()
haystack = "leetcode"
needle = "leeto"
print(sol.strStr(haystack, needle))