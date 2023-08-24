class Solution(object):
    def majorityElement(self, nums):
        
        # 1. 배열 정렬
        nums.sort()
        
        # 2. 정중앙에 위치한 index 구함
        index = len(nums) // 2
    
        # 3. 정중앙에 위치한 요소 return
        return nums[index]
        
        """
        :type nums: List[int]
        :rtype: int
        """
        