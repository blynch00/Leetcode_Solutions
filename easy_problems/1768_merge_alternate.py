class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr1 = list(word1)
        arr2 = list(word2)
        new_string = ""
        index = 0

        while True:
            if len(arr1) == 0 and len(arr2) == 0:
                break
            if len(arr1) !=0:
                new_string += arr1[index]
                arr1.pop(index)
                print(new_string)
                print(arr1)
            if len(arr2) != 0:
                new_string += arr2[index]
                arr2.pop(index)
                print(new_string)
                print(arr2)
        return new_string