class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        exist={}
        result=[]
        for index,value in enumerate(nums):
            complement=target-nums[index]
            if complement in exist:                            
                return [exist[complement],index]
            else:
                exist[value]=index
            
        
        
