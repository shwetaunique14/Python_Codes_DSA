"""Remove Duplicates from Sorted Array
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores)."""

#BRUTE FORCE APPROACH:

def remove_duplicates_brute(nums: list[int]) -> int:
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num) 
    for i in range(len(unique_nums)):
        nums[i] = unique_nums[i]    
        
    return len(unique_nums)

#TC: O(n^2)
#SC: O(n)

#OPTIMIZED APPROACH:

def remove_duplicates_optimized(nums: list[int]) -> int:
    if not nums:
        return 0

    left=0
    for right in range(1, len(nums)):
        if nums[right] != nums[left]:
            left += 1
            nums[left] = nums[right]

    return left + 1

#TC: O(n)
#SC: O(1)