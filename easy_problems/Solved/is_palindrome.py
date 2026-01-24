
def isPalindrome (s: str) -> bool:
    new_string = "".join(char for char in s if char.isalnum()).lower()
    p1, p2 = 0, len(new_string) - 1

    while p2 > p1:
        if new_string[p2] != new_string[p1]:
            return False
        p2 -= 1
        p1  += 1

    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))