class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+= 1
            else:
                dict[nums[i]]=1
        for key in dict:
            if dict[key]>len(nums)//2:
                return key
        