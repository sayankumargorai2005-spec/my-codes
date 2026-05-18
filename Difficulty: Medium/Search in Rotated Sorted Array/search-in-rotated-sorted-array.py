class Solution:
    def search(self, nums, key):
        # code here
        low=0
        high = len(nums)-1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==key:
                return mid
            elif nums[mid]>=nums[low]:
                if key>=nums[low] and key<=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if key>=nums[mid] and key<=nums[high]:
                    low = mid +1
                else:
                    high = mid-1
        return -1
        