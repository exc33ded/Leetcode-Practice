class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        # Compute the total sum of the last k cards
        total = sum(cardPoints[-k:])
        maxSum = total
        # Slide the window from right to left
        for i in range(k):
            total = total - cardPoints[-k+i] + cardPoints[i]
            maxSum = max(maxSum, total)
        return maxSum
