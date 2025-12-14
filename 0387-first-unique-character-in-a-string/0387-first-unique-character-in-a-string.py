class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        char_count = Counter(s)
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        return -1