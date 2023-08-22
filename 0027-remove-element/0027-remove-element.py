class Solution(object):
    def removeElement(self, nums, val):
        # nums 배열에서 val 요소 다 삭제하기
        while val in nums:
            nums.remove(val)

        return len(nums)
        
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        