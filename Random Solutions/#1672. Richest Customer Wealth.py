from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for i in range(len(accounts)):
            if sum(accounts[i]) > res:
                res = sum(accounts[i])
        return res