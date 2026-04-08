class Solution:
    def encode(self, strs):
        result = []

        for s in strs:
            result.append(str(len(s)) + "#" + s)   # __define-ocg__

        return "".join(result)

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i

            # move j until we find '#'
            while s[j] != "#":
                j += 1

            # number before '#' is the length of the word
            varOcg = int(s[i:j])

            # actual word starts after '#'
            word = s[j + 1 : j + 1 + varOcg]
            result.append(word)

            # move i to the start of the next encoded word
            i = j + 1 + varOcg

        return result