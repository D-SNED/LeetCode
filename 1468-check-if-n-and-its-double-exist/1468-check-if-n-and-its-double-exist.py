class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for i in range(len(arr)):
            if 2 * arr[i] in seen or arr[i] / 2 in seen:
                return True
            seen.add(arr[i])

        return False