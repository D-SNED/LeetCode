class Solution(object):
    def isPalindrome(self, x):
        copy = x
        copy = str(copy)
        result = ""
        for index in range(len(copy) - 1, -1, -1):
            result += copy[index]
            
        if result == copy:
            return True
        return False
            
        