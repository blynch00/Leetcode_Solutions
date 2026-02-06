# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter 
# in pattern and a non-empty word in s. Specifically:

# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new_s = s.split(" ")
        new_string = Counter(new_s)
        print(new_string)
        return Counter(pattern)

sol = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(sol.wordPattern(pattern, s))