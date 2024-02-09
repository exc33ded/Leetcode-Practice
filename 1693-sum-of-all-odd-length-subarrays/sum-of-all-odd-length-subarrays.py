class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)  # Length of the input array

        # Iterate over each element in the array
        for i in range(n):
            # Calculate the contribution of arr[i] to the sum
            # based on the number of subarrays it appears in
            res += ((i + 1) * (n - i) + 1) // 2 * arr[i]

        return res