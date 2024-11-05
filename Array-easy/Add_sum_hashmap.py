class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum=0
        n=len(nums)
        hashmap={}

        for i in range(0,n):
            sum=target-nums[i]
            if sum in hashmap:
                return [hashmap[sum],i]
            hashmap[nums[i]]=i
