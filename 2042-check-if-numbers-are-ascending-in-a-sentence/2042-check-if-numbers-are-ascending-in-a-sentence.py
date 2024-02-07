class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        word_lst = s.split(' ')
        print(word_lst)
        
        result = []
        
        for word in word_lst:
            if word.isdigit():
                result.append(int(word))
                
        for i in range(len(result) - 1):
            if result[i] >= result[i + 1]:
                return False
            
        return True
            
            
                