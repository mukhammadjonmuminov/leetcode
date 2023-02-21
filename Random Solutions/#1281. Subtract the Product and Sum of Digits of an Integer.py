class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mlt = 1
        total = 0
        while n > 0:
            mlt *= n % 10
            total += n % 10
            n = n // 10
        return mlt - total
