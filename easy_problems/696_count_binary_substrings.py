class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 1:
            return 0
        num_count = []

        index = 1
        count = 1
        curr = s[0]
        while index < len(s):
            if s[index] == curr:
                count += 1
                index += 1
            else:
                num_count.append(count)
                curr = s[index]
                count = 1
                index += 1

        num_count.append(count)
        print(num_count)

        total = 0

        for x in range(0, len(num_count) - 1):
            max_count = min(num_count[x], num_count[x+1])
            total += max_count

        return total