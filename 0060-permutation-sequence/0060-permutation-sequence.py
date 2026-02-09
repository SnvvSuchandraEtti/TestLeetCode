class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # Calculate factorials
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)
        
        # Create list of available numbers
        numbers = list(range(1, n + 1))
        
        # Convert k to 0-indexed
        k -= 1
        
        result = []
        for i in range(n):
            # Find which number should be at this position
            index = k // factorial[n - 1 - i]
            result.append(str(numbers[index]))
            numbers.pop(index)
            
            # Update k for next position
            k %= factorial[n - 1 - i]
        
        return ''.join(result)