class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == 0 or len(str2) == 0:
            return ""
        # 1) Find shorter string
        str1_len = len(str1)
        str2_len = len(str2)
        if(str1_len <= str2_len):
            shorter = str1
            larger = str2
        else:
            shorter = str2
            larger = str1 
        
        # 2). Add to a set every prefix of shorter string; "ABC" -> "A,AB,ABC"
            # -> Since it must be added upon itself, we know we only need strings that start in the middle or repeat
        
        seen = set()
        substring = ""
        for x in range(0, len(shorter)):
            substring += shorter[x]
            seen.add(substring) 

        #3) For the longer string, find the longest substring in the list and compare size.
        answer_len = 0
        answer = ""

        for x in seen:
            length = len(x)
            # If we cannot use this substring to compose either substring, move on
            if len(shorter) % length != 0 or len(larger) % length != 0:   
                continue
            new_substring1 = x * (len(shorter)//length)
            new_substring2 = x * (len(larger)//length)
            if new_substring1 != shorter or new_substring2 != larger:
                continue
            if len(x) > answer_len:
                answer_len = len(x)
                answer = x

        if answer_len == 0:
            return ""

        return answer

        