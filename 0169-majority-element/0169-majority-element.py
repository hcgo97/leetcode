class Solution(object):
    def majorityElement(self, nums):
        
        # 1. 배열 요소가 1개 밖에 없으면 바로 return
        if len(nums) == 1:
            return nums[0]
        
        # 2. 배열 정렬
        nums.sort()
        
        # 3. 정중앙에 위치한 index 구함
        index = len(nums) // 2
    
        # 4. 정중앙에 위치한 요소 return
        return nums[index]
        
        """
        :type nums: List[int]
        :rtype: int
        """
        