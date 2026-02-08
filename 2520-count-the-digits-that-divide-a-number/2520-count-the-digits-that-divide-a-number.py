class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        original_num = num
        
        while num > 0:
            digit = num % 10
            if original_num % digit == 0:
                count += 1
            num = num // 10
        
        return count