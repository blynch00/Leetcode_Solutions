from collections import Counter
# Given a string text of words separated by a single space 
# (no leading or trailing spaces) and a string brokenLetters of all 
# distinct letter keys that are broken, return the number of words in text 
# you can fully type using this keyboard.
# Input: text = "hello world", brokenLetters = "ad"
# Output: 1
# Explanation: We cannot type "world" because the 'd' key is broken.
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        word_count = 0
        words = text.split(" ")
        sets = []
        for x in words:
            seen = set(x)
            print(seen)
            sets.append(seen)
        print(sets)
        for x in range(0, len(sets)):
            present = 0
            for y in range(0, len(brokenLetters)):
                if brokenLetters[y] in sets[x]:
                    present += 1
            if present == 0:
                word_count += 1
                
        return word_count


sol = Solution()
text = "leet code"
brokenLetters = "e"
print(sol.canBeTypedWords(text, brokenLetters))