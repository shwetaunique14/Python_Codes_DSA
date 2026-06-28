"""3Sum Closest
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2)."""

#OPTIMIZED APPROACH:

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        
        # Start by assuming the very first 3 numbers make our closest sum
        closest_sum = nums[0] + nums[1] + nums[2]
        
        for i in range(n - 2):
            # Your duplicate check (with i - 1 filled in!)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Notice the indentation: left and right are outside the 'if' block now
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # 1. Exact match jackpot! Return immediately.
                if current_sum == target:
                    return current_sum
                
                # 2. Check if the gap of current_sum is smaller than our best gap so far
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # 3. Move your pointers based on whether the sum is too small or too big
                if current_sum < target:
                    left += 1   # We need a larger number
                else:
                    right -= 1  # We need a smaller number
                    
        return closest_sum