class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        mx = max(candies)
        for candy in candies:
            res.append(candy + extraCandies >= mx)
        return res

        # First create an empty list
        # Then find the max element out of the candies list
        # Start the loop for candy
        # Then add the condition if (candy+extracandies) >= max
        # Apeend the following to empty list 
        # Return List