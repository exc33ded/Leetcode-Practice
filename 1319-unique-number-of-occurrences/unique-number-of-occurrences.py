class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dummy = {}
        for num in set(arr):
            dummy[num] = arr.count(num)

        st = set()

        for val in dummy.values():
            if val in st:
                return False
            else:
                st.add(val)

        return True
        
