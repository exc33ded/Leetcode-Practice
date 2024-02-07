class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        lst = [first]

        for element in encoded:
            xor = element ^ lst[-1]
            lst.append(xor)
        return lst