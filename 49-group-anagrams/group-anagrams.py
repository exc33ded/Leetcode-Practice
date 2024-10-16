class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dummy = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            dummy[sorted_word].append(word)
        return list(dummy.values())