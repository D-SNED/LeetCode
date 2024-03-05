class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        
        for string in operations:
            if string == "--X" or string == "X--":
                res -= 1
            else:
                res += 1
                
        return res