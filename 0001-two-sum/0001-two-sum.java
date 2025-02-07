import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
            // Create a HashMap to store the value and its corresponding index
                    Map<Integer, Integer> map = new HashMap<>();
                            
                                    // Iterate through the array
                                            for (int i = 0; i < nums.length; i++) {
                                                        int complement = target - nums[i];
                                                                    
                                                                                // Check if the complement exists in the map
                                                                                            if (map.containsKey(complement)) {
                                                                                                            // If it exists, return the indices
                                                                                                                            return new int[] { map.get(complement), i };
                                                                                                                                        }
                                                                                                                                                    
                                                                                                                                                                // Otherwise, add the current element and its index to the map
                                                                                                                                                                            map.put(nums[i], i);
                                                                                                                                                                                    }
                                                                                                                                                                                            
                                                                                                                                                                                                    // If no solution is found, return an empty array (though the problem guarantees one solution)
                                                                                                                                                                                                            return new int[0];
                                                                                                                                                                                                                }
                                                                                                                                                                                                                }
                                                                                                                                                                                                                