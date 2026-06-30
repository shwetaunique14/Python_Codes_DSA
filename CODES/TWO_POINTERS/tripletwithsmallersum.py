"""
Triplet With Smaller Sum
Solved
Medium
Topics
Companies
Given an array of n integers nums and a target, find the number of triplets i, j, k such that i < j < k and nums[i] + nums[j] + nums[k] < target.
Examples :

Input: sum = 2, arr[] = [-2, 0, 1, 3]
Output:  2
Explanation: Triplets with sum less than 2 are (-2, 0, 1) and (-2, 0, 3). """

#OPTIMIZED APPROACH:

class Solution:
    def triplet_with_smaller_sum(self, nums: list[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        count = 0
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum < target:
                    count += (right - left)  # All triplets with the current 'i' and 'left' are valid
                    left += 1
                else:
                    right -= 1
                    
        return count