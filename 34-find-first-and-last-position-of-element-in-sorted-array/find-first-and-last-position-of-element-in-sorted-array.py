class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def floor(nums, target):
            start = 0
            end = len(nums) - 1
            idx = -1
            while(start <= end):
                mid = start + (end - start)//2
                if nums[mid] == target:
                    idx = mid
                    start = mid + 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return idx
           
        def ceil(nums, target):
            start = 0
            end = len(nums) - 1
            idx = -1
            while(start <= end):
                mid = start + (end - start)//2
                if nums[mid] == target:
                    idx = mid
                    end = mid - 1
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return idx

        return [ceil(nums, target), floor(nums, target)]