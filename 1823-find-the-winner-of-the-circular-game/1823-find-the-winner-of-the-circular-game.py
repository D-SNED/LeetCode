class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
#         nums=[]
#         for i in range(1,n+1):
#             nums.append(i)
#         j=0
#         while len(nums)!=1:
#            j=(j+k-1)%len(nums)
#            nums.remove(nums[j])
#         return nums[0]

#         l = list(range(1, n +1))
#         start = 0
        
#         while len(l) != 1:
#             start = (start + k -1) % len(l)
#             l.pop(start)
#             print(l)
#         return l[0]
                
        arr=[i for i in range(1,n+1)]
        def solve(arr,k,index):
            if len(arr)==1:
                return arr[0] 
            index=(index+(k-1))%len(arr)
            arr.pop(index)
            return solve(arr,k,index)
        return solve(arr,k,0)
        
        
        
            
            
            