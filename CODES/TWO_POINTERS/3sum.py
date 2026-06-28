"""You are given an array of integers (both positive and negative). You need to find all unique triplets (three numbers) that add up exactly to 0.Example Array: [-1, 0, 1, 2, -1, -4]One winning triplet here is [-1, 0, 1] because $-1 + 0 + 1 = 0$."""

#BRUTE FORCE APPROACH:

def threeSum_brute(nums: list[int]) -> list[list[int]]:
    # Use a set to automatically filter out duplicate triplets
    unique_triplets = set()
    n = len(nums)
    
    # Loop 1: Fixes the first element (A)
    for i in range(n):
        # Loop 2: Fixes the second element (B)
        for j in range(i + 1, n):
            # Loop 3: Scans for the third element (C)
            for k in range(j + 1, n):
                
                # Check if the three distinct elements add up to zero
                if nums[i] + nums[j] + nums[k] == 0:
                    # Sort the triplet before adding to the set so it catches duplicates
                    # e.g., [-1, 0, 1] and [0, -1, 1] will both become (-1, 0, 1)
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    unique_triplets.add(triplet)
                    
    # Convert the set of tuples back into a list of lists for the required output
    return [list(t) for t in unique_triplets]

#TC: O(n^3)
#SC: O(n) for storing unique triplets in a set

#OPTIMIZED APPROACH:
def threeSum_optimized(nums: list[int]) -> list[list[int]]:
    nums.sort()  # Sort the array to use two-pointer technique
    result = []
    n = len(nums)

    for i in range(n):
        # Skip duplicate elements for the first number of the triplet
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                # Skip duplicates for the second number of the triplet
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                
                # Skip duplicates for the third number of the triplet
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result