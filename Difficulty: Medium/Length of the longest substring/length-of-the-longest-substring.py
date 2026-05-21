#User function Template for python3

class Solution:
    def longestUniqueSubstring(self, s):
        maxlen = 0
        for i in range(len(s)):
            st = set()
            length = 0
            for j in range (i , len(s)):
                if s[j] in st:
                    break
                else:
                    st.add(s[j])
                    length+=1
            maxlen = max(maxlen,length)
        return maxlen