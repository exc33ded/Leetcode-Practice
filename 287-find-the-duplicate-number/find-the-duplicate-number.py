class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        st = set()
        for num in nums:
            if num not in st:
                st.add(num)
            else:
                return num
            