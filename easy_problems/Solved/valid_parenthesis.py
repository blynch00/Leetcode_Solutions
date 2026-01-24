class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'(':')','{':'}','[':']'}
        seen = []

        for x in range(len(s)):
            if s[x] in brackets:
                seen.append(s[x])
                continue
            if s[x] in brackets.values():
                if len(seen) == 0:
                    return False
                if brackets[seen[len(seen)-1]] != s[x]:
                    return False
                                
                seen.pop()
                continue




        if len(seen) == 0:
            return True
        return False



sol = Solution()
s = "]" 
print(sol.isValid(s))