class Solution {
    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) return result;
        
        String[] mapping = {"0","1","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"};
        backtrack(digits, 0, new StringBuilder(), result, mapping);
        return result;
    }
    
    private void backtrack(String digits, int idx, StringBuilder sb, List<String> result, String[] mapping) {
        if (idx == digits.length()) {
            result.add(sb.toString());
            return;
        }
        
        String letters = mapping[digits.charAt(idx) - '0'];
        for (char c : letters.toCharArray()) {
            sb.append(c);
            backtrack(digits, idx + 1, sb, result, mapping);
            sb.deleteCharAt(sb.length() - 1);
        }
    }
}