class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        get = min(x, y//4)
        if get % 2 == 0:
            return "Bob"
        else:
            return "Alice"