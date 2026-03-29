class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        temp = strs[0]
        for char in strs[1:]:
            while char[:len(temp)] != temp:
                temp = temp[:-1]
                if temp == "":
                    return ""
        return temp



        