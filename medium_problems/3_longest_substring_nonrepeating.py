class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window (Variable)
        # resize window to track current largest string, increasing when new character/decreasing when seen.
        
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1

        # highest_count, curr_count
        highest_count, curr_count = 0, 0

        # use defaultdict(int) to keep count 
        seen = defaultdict(int)
        # left, right; begins at the same element
        left, right = 0,0

        while right < len(s):
            if right == left:
                seen[s[left]] += 1
                curr_count += 1
                right += 1
                continue

            if s[right] in seen:
                highest_count = max(highest_count, curr_count)
                while seen[s[right]] > 0:
                    seen[s[left]] -= 1
                    left += 1
                curr_count = right - left
                seen[s[right]] += 1
                right += 1
                curr_count += 1
            else:
                seen[s[right]] += 1
                curr_count += 1
                right += 1

        return max(curr_count, highest_count)