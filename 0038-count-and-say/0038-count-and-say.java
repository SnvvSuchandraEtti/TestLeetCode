class Solution {
    public String countAndSay(int n) {
        String result = "1";
        for (int i = 1; i < n; i++) {
            result = nextSequence(result);
        }
        return result;
    }
    
    private String nextSequence(String s) {
        StringBuilder sb = new StringBuilder();
        int i = 0;
        while (i < s.length()) {
            char current = s.charAt(i);
            int count = 1;
            while (i + 1 < s.length() && s.charAt(i + 1) == current) {
                count++;
                i++;
            }
            sb.append(count).append(current);
            i++;
        }
        return sb.toString();
    }
}