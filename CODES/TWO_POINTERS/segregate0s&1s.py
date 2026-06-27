"""Given an array arr[] consisting of only 0's and 1's. Modify the array in-place to segregate 0s onto the left side and 1s onto the right side of the array.

Examples :

Input: arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
Explanation:  After segregation, all the 0's are on the left and 1's are on the right. Modified array will be [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]."""

#BRUTE FORCE APPROACH:

def segregate0and1_brute(arr):
    # Step 1: Count the number of zeros
    zero_count = 0
    for num in arr:
        if num == 0:
            zero_count += 1
            
    # Step 2: Overwrite the array based on the count
    for i in range(len(arr)):
        if i < zero_count:
            arr[i] = 0
        else:
            arr[i] = 1

#TC: O(n)
#SC: O(1)

#OPTIMIZED APPROACH:

class Solution:
    def segregate0and1(self, arr):
        if not arr:
            return 0
        left=0
        for right in range(len(arr)):
            if arr[right]==0:
                arr[left],arr[right]=arr[right],arr[left]
                left+=1

#TC: O(n)
#SC: O(1)