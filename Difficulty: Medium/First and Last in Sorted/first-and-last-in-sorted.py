class Solution:
    def find(self, arr, x):
        # code here
      return [arr.index(x), len(arr)-1-arr[::-1].index(x)] if x in arr else [-1,-1]