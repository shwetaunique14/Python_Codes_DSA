"""Squares of a Sorted Array
Easy
Topics
premium lock icon
Companies
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
"""


#BRUTE FORCE APPROACH:

def sortedSquares_brute(nums: list[int]) -> list[int]:
    # Step 1: Square every element in place
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
        
    # Step 2: Sort the array from scratch
    nums.sort() 
    return nums

#TC: O(n log n) due to sorting
#SC: O(1) if we ignore the space used by the sorting algorithm, otherwise O(n) if the sorting algorithm uses additional space.  


#OPTIMAL TWO-POINTER (Filling Backward)
def sortedSquares_optimal(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n  # Allocate memory for output array
    
    left = 0
    right = n - 1
    write_index = n - 1  # Start filling from the largest slot (at the back)
    
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        
        # Compare squares at the extremes
        if left_square > right_square:
            result[write_index] = left_square
            left += 1  # Move left pointer inward
        else:
            result[write_index] = right_square
            right -= 1  # Move right pointer inward
            
        write_index -= 1  # Shift our target output slot to the left
        
    return result

#TC: O(n) - We traverse the array once
#SC: O(n) - We use an additional array to store the results