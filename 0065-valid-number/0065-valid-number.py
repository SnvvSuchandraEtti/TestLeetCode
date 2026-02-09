class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False
        
        seen_digit = False
        seen_dot = False
        seen_e = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char in ['+', '-']:
                # Sign can only be at start or right after e/E
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            elif char == '.':
                # Dot cannot appear after e or if already seen
                if seen_e or seen_dot:
                    return False
                seen_dot = True
            elif char in ['e', 'E']:
                # e cannot appear twice or without preceding digit
                if seen_e or not seen_digit:
                    return False
                seen_e = True
                seen_digit = False  # Must have digit after e
            else:
                return False
        
        return seen_digit