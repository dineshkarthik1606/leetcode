class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right={}
        left=0
        result=0
        n=len(s)
        for i in range(n):
            if s[i] in right:
                left=max(right[s[i]],left)
            result=max(result,i-left+1)
            right[s[i]]=i+1
            
        return result
            
