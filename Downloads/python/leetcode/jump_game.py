class Solution(object):
    def jump(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        jumps = 0  # number of jumps
        current_max = 0  # farthest index that can be reached with the current jump
        next_max = 0  # farthest index that can be reached with the next jump

        for i in range(n):
            next_max = max(next_max, i + nums[i])

            if i == current_max:
                jumps += 1
                current_max = next_max

                if current_max >= n - 1:
                    break
        return jumps