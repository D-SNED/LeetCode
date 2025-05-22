class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence_arr = sentence.split(' ')

        for i in range(len(sentence_arr)):
            if sentence_arr[i][0] != sentence_arr[i - 1][-1]:
                return False
        return True
