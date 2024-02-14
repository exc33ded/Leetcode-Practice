class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def lastOcc(nums, target):
            start = 0
            last = len(nums) - 1
            last_occ = -1
            while(start <= last):
                mid = start + (last - start)//2
                if (nums[mid] > target):
                    last = mid - 1
                elif (nums[mid] < target):
                    start = mid + 1
                else:
                    last_occ = mid
                    start = mid + 1
            return last_occ

        def firstOcc(nums, target):
            start = 0
            last = len(nums) - 1
            first_occ = -1
            while(start <= last):
                mid = start + (last - start)//2
                if (nums[mid] > target):
                    last = mid - 1
                elif (nums[mid] < target):
                    start = mid + 1
                else:
                    first_occ = mid
                    last = mid - 1
            return first_occ

        return [firstOcc(nums, target), lastOcc(nums, target)]

        