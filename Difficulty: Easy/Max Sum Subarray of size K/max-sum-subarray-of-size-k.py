class Solution:
    def maxSubarraySum(self, arr, k):
        
        sum1= sum(arr[ : k])
        maxsum = sum1
        for i in range(k, len(arr)):
            sum1= sum1 + arr[i] - arr[i-k]
            maxsum= max(maxsum,sum1)
            
        return maxsum