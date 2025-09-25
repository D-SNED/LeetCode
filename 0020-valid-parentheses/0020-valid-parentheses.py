class Solution:
    def isValid(self, s: str) -> bool:
        res = []

        values = {")":"(", "}": "{", "]":"["}

        for char in s:
            if char in values:
                if len(res) > 0 and res[-1] == values[char]:
                    res.pop()
                else:
                    return False
            else:
                res.append(char)
        
        if len(res) == 0:
            return True
        else:
            return False
                    