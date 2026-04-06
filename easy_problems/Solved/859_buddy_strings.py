from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
       # Return False if string is less than 2 characters
        if len(s) < 2:
            return False
        if len(goal) != len(s):
            return False

        # First, we can check if all but 2 letters are correct, or if 2 letters are the same;

        letters = []
        for x in range (0, len(s)):
            if s[x] != goal[x]:
                letters.append(x)
        
        if len(letters) != 2:
            if len(letters) != 0:
                return False

        # Case 1: Strings match entirely
            # Check if there are 2 of the same letter, so they can be switched
        if len(letters) == 0:
            count = Counter(s)
            for x in count:
                print(x)
                if count[x] >= 2:
                    return True
            return False
        # Case 2: 2 Characters are swapped
            # Check if switching them matches goal
        else:
            index_1 = letters[0]
            index_2 = letters[1]
            swapped_str = list(s)
            swapped_str[letters[0]] = s[index_2]
            swapped_str[letters[1]] = s[index_1]
            final_str = "".join(swapped_str)
            return final_str == goal