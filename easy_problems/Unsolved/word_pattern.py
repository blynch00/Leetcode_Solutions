# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter 
# in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        seen = {}
        index = 0
        new_list = s.split(' ')
        for x in new_list:
            if pattern[index] not in seen:
                pattern[index] = new_list[0]
            else:
                if pattern[index] != new_list[0]:
                    return False
            index +=1
            

sol = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(sol.wordPattern(pattern, s))