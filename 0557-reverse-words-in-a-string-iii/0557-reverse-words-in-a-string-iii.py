class Solution:
    def reverseWords(self, s: str) -> str:
        split_s = s.split(" ")

        arr = []

        for word in split_s:
            arr.append(word[::-1])

        res = ""

        for i in range(len(arr)):
            if i == len(arr) - 1:
                res += arr[i]
            else:
                res += arr[i] + " "

        return res
