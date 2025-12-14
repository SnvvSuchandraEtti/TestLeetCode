class Solution {
    public int divide(int dividend, int divisor) {
        // Handle edge case
        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }
        
        // Convert to long to avoid overflow
        long dvd = Math.abs((long)dividend);
        long dvs = Math.abs((long)divisor);
        
        long result = 0;
        while (dvd >= dvs) {
            long temp = dvs;
            long count = 1;
            
            while (dvd >= (temp << 1)) {
                temp <<= 1;
                count <<= 1;
            }
            
            dvd -= temp;
            result += count;
        }
        
        // Apply sign
        if ((dividend < 0) ^ (divisor < 0)) {
            result = -result;
        }
        
        return (int)result;
    }
}