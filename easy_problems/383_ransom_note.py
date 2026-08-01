def canConstruct(ransomNote: str, magazine: str) -> bool:
        magazine_seen = {}
        ransomNote_seen = {}

        for i in range(len(magazine)):
            if magazine[i] in magazine_seen:
                magazine_seen[magazine[i]] +=1
            else:
                magazine_seen[magazine[i]] = 1

        for x in range(len(ransomNote)):
            if ransomNote[x] in ransomNote_seen:
                ransomNote_seen[ransomNote[x]] += 1
            else:
                ransomNote_seen[ransomNote[x]] = 1

        for key in ransomNote_seen:
            if key not in magazine_seen:
                 return False
            if ransomNote_seen[key] > magazine_seen[key]:
                 return False
        return True
