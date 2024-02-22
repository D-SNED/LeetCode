class Solution:
    def longestPalindrome(self, s: str) -> str:
        # iterate for index in first loop
            # create substring var
            # create length var = length of string
            # iterate for index in second loop while length > 0
                # if string = backwards string
                    # append into result
                    
        
        substring = []
        for i in range(len(s)):
            
            copy = s[i::]
            # print("first: ",copy)
            length = len(copy)
            while length > 0:
                if copy == copy[::-1]:
                    substring.append(copy)
                copy = copy[:len(copy) - 1]
                length -= 1
                # print("while: ", copy)
        
        max = ""
        for string in substring:
            if len(string) > len(max):
                max = string
        return max
                
        
            
                        
        
                
                
                