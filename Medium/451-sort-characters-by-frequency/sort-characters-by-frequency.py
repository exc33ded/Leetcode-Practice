class Solution:
    def frequencySort(self, s: str) -> str:
        hm = {}
        for char in s:
            if char not in hm:
                hm[char] = 1
            else:
                hm[char] += 1
        sorted_list = sorted(hm.items(), key=lambda char_cnt: -char_cnt[1])

        return "".join([char_cnt[0] * char_cnt[1] for char_cnt in sorted_list])