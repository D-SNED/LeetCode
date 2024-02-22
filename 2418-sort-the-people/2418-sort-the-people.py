class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        
        for i in range(len(heights)):
            max_index = i
            for j in range(i + 1, len(heights)):
                if heights[j] > heights[max_index]:
                    max_index = j
                    
            if i != max_index:
                temp = heights[i]
                temp2 = names[i]
                heights[i] = heights[max_index]
                names[i]= names[max_index]
                heights[max_index] = temp
                names[max_index] = temp2
                
        return names