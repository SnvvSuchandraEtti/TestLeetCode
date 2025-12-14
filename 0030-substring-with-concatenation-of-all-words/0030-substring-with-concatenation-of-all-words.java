class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        if (s == null || s.length() == 0 || words == null || words.length == 0) {
            return result;
        }
        
        int wordLen = words[0].length();
        int wordCount = words.length;
        int totalLen = wordLen * wordCount;
        
        // Create a map of word frequencies
        Map<String, Integer> wordMap = new HashMap<>();
        for (String word : words) {
            wordMap.put(word, wordMap.getOrDefault(word, 0) + 1);
        }
        
        // Check each possible starting position
        for (int i = 0; i <= s.length() - totalLen; i++) {
            // Create a map for words in current window
            Map<String, Integer> windowMap = new HashMap<>();
            
            // Extract words from the current window
            for (int j = 0; j < wordCount; j++) {
                String word = s.substring(i + j * wordLen, i + (j + 1) * wordLen);
                windowMap.put(word, windowMap.getOrDefault(word, 0) + 1);
            }
            
            // Check if window matches
            if (windowMap.equals(wordMap)) {
                result.add(i);
            }
        }
        
        return result;
    }
}