class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_m = Counter(magazine)

        for char in ransomNote:
            if char not in count_m:
                return False

            count_m[char] -= 1

        for num in count_m.values():
            if num < 0:
                return False
        return True