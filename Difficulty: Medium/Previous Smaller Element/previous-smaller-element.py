class Solution:
	def prevSmaller(self, arr):
		# code here
        result = [-1]*len(arr)
        stack=[]
        for i in range(len(arr)):
            while stack and stack[-1] >= arr[i]:
                stack.pop()
            if stack :
                result[i] = stack[-1]
            stack.append(arr[i])
        return result