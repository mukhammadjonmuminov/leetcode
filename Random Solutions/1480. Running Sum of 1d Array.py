from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        res = []
        for item in nums:
            s += item
            res.append(s)
        return res