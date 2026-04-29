class Solution:
    def reverseWords(self, s: str) -> str:
        final_sentence = ""

        words = s.split(" ")
        print(f"Start: {words}")
        words = [x for x in words if x != ""]
        print(f"End: {words}")

        p1 = 0
        p2 = len(words) - 1

        while p1 < p2:
            temp = words[p1]
            words[p1] = words[p2]
            words[p2] = temp 
            p1 += 1
            p2 -= 1

        for x in range(len(words)):
            final_sentence += f"{words[x]}"
            if x != len(words) -1 :
                final_sentence += " "
        return final_sentence
    
sol = Solution()
words = "Oracle will be tough to interview at!"
words2 = "  hello world  "
print(sol.reverseWords(words))