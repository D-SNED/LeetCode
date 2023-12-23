class Solution:
    def reverseVowels(self, str: str) -> str:
        vowel_lst = []
        str_lst = []
        vowels_lst_index = -1

        for i in range(len(str)):
            if str[i] in "aeiouAEIOU":
                vowel_lst.append(str[i])
                str_lst.append("+")
            else:
                str_lst.append(str[i])

        for i in range(len(str_lst)):
            if str_lst[i] == "+":
                str_lst[i] = vowel_lst[vowels_lst_index]
                vowels_lst_index -= 1

        return "".join(str_lst)