
class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()

        missing = 1

        for num in nums:
            if num == missing:
                missing += 1

        return missing
