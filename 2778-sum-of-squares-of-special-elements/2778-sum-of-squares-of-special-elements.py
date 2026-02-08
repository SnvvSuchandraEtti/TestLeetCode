class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        result = 0
        
        for i in range(n):
            # Convert to 1-indexed
            if n % (i + 1) == 0:
                result += nums[i] * nums[i]
        
        return result