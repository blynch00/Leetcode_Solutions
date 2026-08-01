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
