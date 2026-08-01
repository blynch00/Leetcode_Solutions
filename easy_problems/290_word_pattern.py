from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new_s = s.split(" ")
        new_string = Counter(new_s)
        print(new_string)
        return Counter(pattern)
