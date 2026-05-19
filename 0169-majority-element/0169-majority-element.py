class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        can=None 
        count = 0
        for i in range(len(nums)):
            if count == 0:
                can=nums[i]
                count = 1 
            elif can == nums[i]:
                count +=1 
            else :
                count -=1
        return can
        