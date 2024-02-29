class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = []
        for i in range(len(s)):
            longest = ""
            for j in range(i, len(s)):
                if s[j] in longest:
                    break
                longest += s[j]
            result.append(longest)
            
        max = 0
        
        for string in result:
            if len(string) > max:
                max = len(string)
        return max
                