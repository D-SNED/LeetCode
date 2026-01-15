class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_m = Counter(magazine)

        for char in ransomNote:
            if char not in count_m:
                return False
            elif char in count_m and count_m[char] == 0:
                return False
            count_m[char] -= 1

        return True
            