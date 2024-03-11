class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs[0] == "":
            return ""
        
        def all_match(idx, strs):
            ref = strs[0][idx]
                
            for word in strs:
                if word[idx] != ref:
                    return False
            return True
            
            
        try:
            result = ""

            for i in range(len(strs[0])):
                helper = all_match(i, strs)

                if helper:
                    result += strs[0][i]
                else:
                    return result

            return result
        except IndexError:
            return result


        