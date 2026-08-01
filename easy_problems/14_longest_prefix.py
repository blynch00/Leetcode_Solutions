#Write a function to find the longest common prefix string amongst an array of strings.

#If there is no common prefix, return an empty string "".
#Input: strs = ["flower","flow","flight"]
#Output: "fl"     

def longestCommonPrefix(strs: list[str]) -> str:
    prefix = ""
    index = 0
    if len(strs) == 0:
        return prefix
    # for each character in the first word:
    for char in strs[0]:
        print(char)
    # for each word in the list;
        for word in strs:
            if index > len(word) - 1 or word[index]!= char:
                return prefix
        prefix += char
        index += 1
        # If the word is shorter than current index or current index != character:
            # return string
        # Else append and continue
    return prefix
