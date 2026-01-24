#Given an input string s, reverse the order of the words.

#A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

#Return a string of the words in reverse order concatenated by a single space.

#Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

s = "Mary had a    little lamb"
# Create an empty list to store complete words
# Separate the string based on 
sentence_split = s.split(" ")
print(sentence_split)

iterator = len(sentence_split) - 1
new_list = ""
while iterator >= 0:
    if sentence_split[iterator] == "":
        iterator -= 1
        continue

    new_list += " "
    new_list += sentence_split[iterator]
    iterator -=1

print(new_list)

    