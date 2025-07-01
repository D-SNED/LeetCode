class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target < letters[0] or target >= letters[len(letters) - 1]:
            return letters[0]

        lo = 0
        hi = len(letters) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if target < letters[mid]:
                hi = mid - 1

            if target >= letters[mid]:
                lo = mid + 1

        return letters[lo]
            


     