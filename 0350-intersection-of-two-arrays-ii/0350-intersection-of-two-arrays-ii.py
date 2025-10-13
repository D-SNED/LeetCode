class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        """
        4 5 9 
        4 4 8 9 9
        """

        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)

        i = 0
        j = 0

        while i < len(sorted_nums1) and j < len(sorted_nums2):
            if sorted_nums1[i] < sorted_nums2[j]:
                i += 1
            elif sorted_nums1[i] > sorted_nums2[j]:
                j += 1
            else:
                res.append(sorted_nums1[i])
                i += 1
                j += 1

        return res

