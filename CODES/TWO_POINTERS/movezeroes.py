"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.Note: You must do this in-place without making a copy of the array.📥 ExamplesExample 1:Input: nums = [0, 1, 0, 3, 12]Output: [1, 3, 12, 0, 0]Example 2:Input: nums = [0]Output: [0]💡 Constraints$1 \le \text{nums.length} \le 10^4$$-2^{31} \le \text{nums}[i] \le 2^{31} - 1$
"""
#BRUTE FORCE APPROACH:

def move_zeroes_brute(nums: list[int]) -> None:
    non_zero_nums = []
    zeroes=[]
    for num in nums:
        if num != 0:
            non_zero_nums.append(num)
        else:
            zeroes.append(num)
    combined_result= non_zero_nums + zeroes
    for i in range(len(nums)):
        nums[i] = combined_result[i]

#TC: O(n)
#SC: O(n)

#OPTIMIZED APPROACH:

def move_zeroes_optimized(nums: list[int]) -> None:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1

#TC: O(n)
#SC: O(1)