class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
#         result = []
        
#         for arr in image:
#             result.append(arr[::-1])
                
#         for i in range(len(result)):
#             for j in range(len(result[i])):
#                 if result[i][j] == 1:
#                     result[i][j] = 0
#                 else:
#                     result[i][j] = 1
                    
#         return result
                    
        for i in range(len(image)):
            image[i].reverse()
            for j in range(len(image[i])):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1

        return image
            