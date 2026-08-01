class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        string_1 = {}
        string_2 = {}


        for letter in range(len(s)):
            if s[letter] in string_1:
                string_1[s[letter]] += 1
            else:
                string_1[s[letter]] = 1
        print(string_1)

        for letter in range(len(t)):
            if t[letter] in string_2:
                string_2[t[letter]] += 1
            else:
                string_2[t[letter]] = 1
        print(string_2)

        print(f"Anagram: {string_1 == string_2}")