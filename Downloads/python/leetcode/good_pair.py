class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize a dictionary to count the frequency of each number
        num_counts = {}
        
        # Initialize a variable to keep track of the total count of good pairs
        total_count = 0
        
        # Iterate through the input list
        for num in nums:
            # If the number is not in the dictionary, add it with a count of 1
            if num not in num_counts:
                num_counts[num] = 1
            else:
                # If the number is already in the dictionary, increment its count
                num_counts[num] += 1
                
                # Add the current count to the total count (this counts the good pairs)
                total_count += num_counts[num] - 1
        
        return total_count

nums = [1, 2, 3, 1, 1, 3]
solution = Solution()
result = solution.numIdenticalPairs(nums)
print(result) 