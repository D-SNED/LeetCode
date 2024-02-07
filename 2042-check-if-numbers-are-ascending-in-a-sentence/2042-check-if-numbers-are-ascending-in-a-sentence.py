class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        word_lst = s.split(' ')
        print(word_lst)
        
        ref = 0
        
        for word in word_lst:
            if word.isdigit():
                if int(word) <= ref:
                    return False
                ref = int(word)
                
        return True
            
            
                