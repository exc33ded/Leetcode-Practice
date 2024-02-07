class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        map = {
            "type" : 0,
            "color" : 1,
            "name" : 2
        }
        counter = 0

        for item in items:
            idx = map[ruleKey]
            if item[idx] == ruleValue:
                counter += 1
        return counter