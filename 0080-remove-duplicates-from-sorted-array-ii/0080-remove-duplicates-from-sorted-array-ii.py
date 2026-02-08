class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        
        # Pointer for placing the next valid element
        write_idx = 2
        
        # Start from index 2 since first two elements are always valid
        for i in range(2, len(nums)):
            # If current element is different from element at write_idx-2
            # then it's safe to include (max 2 occurrences)
            if nums[i] != nums[write_idx - 2]:
                nums[write_idx] = nums[i]
                write_idx += 1
        
        return write_idx