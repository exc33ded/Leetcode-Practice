import itertools

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hm = {
            2:'abc',
            3:'def',
            4:'ghi',
            5:'jkl',
            6:'mno',
            7:'pqrs',
            8:'tuv',
            9:'wxyz'
        }
        
        if not digits:
            return []
        else:
            chars = []
            for digit in digits:
                chars.append(hm[int(digit)])
            
            comb = []
            for c in itertools.product(*chars):
                comb.append("".join(c))
        return comb