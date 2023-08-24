class Solution(object):
    def removeDuplicates(self, nums):
        
        # 1. nums 배열 요소가 2개 이하면 바로 return
        if len(nums) <= 2:
            return len(nums)
        
        # 2. 최대 두 번까지 중복이 가능하므로 2로 초기화
        index = 2
        
        for i in range(2, len(nums)):
            
            # 3. 중복이 허용되는 범위를 벗어나면 
            if nums[i] != nums[index - 2]:
                
                # 4. 중복이 허용되는 범위 내에 있는 nums 요소를 index 위치에 저장
                nums[index] = nums[i]
                
                # 5. 다음 중복 허용 범위로 index 위치를 옮김
                index += 1
        
        # 6. 중복 제거된 nums 요소 개수 return
        return index
        
        """
        :type nums: List[int]
        :rtype: int
        """
        