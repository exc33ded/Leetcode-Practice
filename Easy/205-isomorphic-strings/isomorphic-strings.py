class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t_mapping = {}
        t_to_s_mapping = {}

        for x, y in zip(s, t):
            if x in s_to_t_mapping:
                if s_to_t_mapping[x] != y:
                    return False
            else:
                s_to_t_mapping[x] = y
                
            if y in t_to_s_mapping:
                if t_to_s_mapping[y] != x:
                    return False
            else:
                t_to_s_mapping[y] = x

        return True
        