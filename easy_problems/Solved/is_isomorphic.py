from collections import Counter
def isIsomorphic(s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        print(f" S: {set(s_counter.values())}")
        print(f" T: {set(t_counter.values())}")
        return set(s_counter.values()) == set(t_counter.values())

s = "bbbaaaba"
t = "aaabbbba"
print(isIsomorphic(s,t))