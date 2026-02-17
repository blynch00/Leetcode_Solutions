# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max = 0
        for x in range(0, len(s)):
            seen = set()
            current_substring = 0
            for y in range(x, len(s)):
                if s[y] not in seen:
                    seen.add(s[y])
                    current_substring += 1
                else:
                        break
            if current_substring > max:
                max = current_substring
        return max
                

sol = Solution()
s = "dvdf"
print(sol.lengthOfLongestSubstring(s))