class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def common(s1, s2):
            min_ = min(len(s1), len(s2))
            res = ""
            for i in range(min_):
                if s1[i] == s2[i]:
                    res += s1[i]
                else:
                    break
            return res

        word1 = strs[0]
        for i in range(1, len(strs)):
            word1 = common(word1, strs[i])
        return word1