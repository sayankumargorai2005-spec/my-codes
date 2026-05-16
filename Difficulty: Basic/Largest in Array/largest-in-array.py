class Solution:
    def largest(self, arr):
        # code here
        max_val = arr[0]
        for x in arr:
            if x>max_val:
                 max_val=x
        return max_val
        
