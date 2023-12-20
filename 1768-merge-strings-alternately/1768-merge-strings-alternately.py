class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # create result list
        # create biggest word variable = largest length of both words
        # iterate through largest range for index
        # if index is less than word1 length append letter
        # if index is less than word2 length append letter
        # join result list to create string

        result = []

        largest_word = max(len(word1), len(word2))

        for i in range(largest_word):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])

        return "".join(result)