# You are given a string s consisting of the following
#  characters: '(', ')', '{', '}', '[' and ']'.

# The input string s is valid if and only if:
#   1. Every open bracket is closed by the same type of close bracket.
#   2. Open brackets are closed in the correct order.
#  3. Every close bracket has a corresponding open bracket of the same type.
# 
# Return true if s is a valid string, and false otherwise.

def isValid(s: str) -> bool:
    pairs = {'(':')', '{':'}', '[':']'}
    stacks = []
    print(pairs.items())
    for x in range(len(s)):
        if x == 0 and len(stacks)==0:
            stacks.append(s[x])
            continue
        print(stacks)
        if s[x] in pairs.keys():
            stacks.append(s[x])
            print(stacks)
            print(f"{s[x]}", f"{stacks[len(stacks) - 1]}")
            continue
        
        elif (s[x], stacks[len(stacks)-1]) in pairs.items():
            stacks.pop()
            print((s[x], stacks[len(stacks)-1]))
        else: 
            return False
    if len(stacks) == 0:
        return True
    else:
        return False


s = "([{}])"
print(isValid(s))