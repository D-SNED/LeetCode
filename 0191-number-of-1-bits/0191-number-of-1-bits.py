class Solution:
    def hammingWeight(self, n: int) -> int:
        n = bin(n)
    
        num_1s = 0
        
        for el in n:
            print(el)
            if el == "1":
                num_1s += 1
                
        return num_1s