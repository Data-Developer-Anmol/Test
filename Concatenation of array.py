"""1929. Concatenation of Array
Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n.
Specifically, ans is the concatenation of two nums arrays. Return the array ans"""

class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        
        # Check the Contrains and raise error if needed
        if not (1 <= n <= 1000):
            raise ValueError("Length of nums must be between 1 and 1000.")
        if any(num < 1 or num > 1000 for num in nums):
            raise ValueError("Each element in nums must be between 1 and 1000.")
        
        # Concatiniating nums with itself to form the ans array
        ans = nums + nums
        return ans