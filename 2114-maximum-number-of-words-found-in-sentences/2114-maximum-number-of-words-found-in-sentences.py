class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        
        
        for i in range(len(sentences)):
            sub = sentences[i].split()
            if len(sub) > max:
                max = len(sub)
                
        return max
            
            