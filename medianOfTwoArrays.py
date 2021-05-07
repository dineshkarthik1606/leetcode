class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged=nums1+nums2
        merged.sort()
        mid=len(merged)//2        
        res=(merged[mid]+merged[~mid])/2
        return res
        
