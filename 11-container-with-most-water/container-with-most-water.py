class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr_lo = 0
        ptr_hi = len(height) - 1
        area = 0

        while (ptr_lo <= ptr_hi):
            area = max(area, min(height[ptr_lo], height[ptr_hi]) * (ptr_hi - ptr_lo))
            
            if height[ptr_lo] <= height[ptr_hi]:
                ptr_lo += 1
            else:
                ptr_hi -= 1
    
        return area
        
        

        