class Solution(object):
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        
        nums.sort()
        left, right = 0, 1
        result = 0
        n = len(nums)
        
        while right < n:
            if left == right or nums[right] - nums[left] < k:
                right += 1
            elif nums[right] - nums[left] > k:
                left += 1
            else:
                result += 1
                left += 1
                right += 1
                # Skip duplicates for left
                while left < n and nums[left] == nums[left - 1]:
                    left += 1
                # Skip duplicates for right
                while right < n and nums[right] == nums[right - 1]:
                    right += 1
                    
            # Ensure left is always less than right
            if left == right:
                right += 1
        
        return result