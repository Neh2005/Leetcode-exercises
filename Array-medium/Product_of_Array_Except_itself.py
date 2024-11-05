from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n
        
        # First pass to fill `answer` with left products
        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]
        
        # Second pass to incorporate right products in-place
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        
        return answer

""" Here the time complexity is O(n) and time complexity is O(1) because here constant amount of space has been created for the extraa rray created."""
