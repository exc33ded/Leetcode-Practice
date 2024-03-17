class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_cnt, one_cnt, two_cnt = 0,0,0
        for num in nums:
            if num == 0:
                zero_cnt += 1
            elif num == 1:
                one_cnt += 1
            else:
                two_cnt += 1

        z_arr = [0]*zero_cnt
        o_arr = [1]*one_cnt
        t_arr = [2]*two_cnt
        arr = []
        arr[:] = z_arr[:] + o_arr[:] + t_arr[:]
        
        for i in range(len(nums)):
            nums[i] = arr[i]
        return nums