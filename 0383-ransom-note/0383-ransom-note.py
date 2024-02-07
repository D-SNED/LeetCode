class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}
        
        for letter in magazine:
            if letter not in magazine_dict:
                magazine_dict[letter] = 0
            magazine_dict[letter] += 1
            
        print(magazine_dict)
            
        for letter in ransomNote:
            if letter in magazine_dict:
                magazine_dict[letter] -= 1
            else:
                return False
            
        print(magazine_dict)
            
        for key in magazine_dict:
            if magazine_dict[key] < 0:
                return False
        return True