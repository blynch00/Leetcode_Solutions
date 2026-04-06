from typing import List
from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_list = []
        seen = set()
       
        for x in range(len(strs)):
            if strs[x] in seen:
                continue
            anagrams = []
            seen.add(strs[x])
            anagrams.append(strs[x])
            for y in range(len(strs)):
                if x == y:
                    continue
                if Counter(strs[x]) == Counter(strs[y]):
                    anagrams.append(strs[y])
                    seen.add(strs[y])
            new_list.append(anagrams)
        
        return new_list


sol = Solution()
strs = [""]
print(sol.groupAnagrams(strs))