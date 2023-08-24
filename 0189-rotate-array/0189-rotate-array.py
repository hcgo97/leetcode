class Solution(object):
    def rotate(self, nums, k):
        
        if len(nums) > 1:
            
            # 이동시킬 횟수 구하기
            moveCount = k % len(nums)
        
            # 1. 이동시킬 범위 설정
            startIndex = len(nums) - moveCount
            endIndex = len(nums)

            # 2. 가장 끝에서부터 k 번째 만큼의 범위를 배열의 맨 앞으로 옮긴다
            nums[0:0] = nums[startIndex:endIndex]

            # 3. 범위 다시 설정
            startIndex = len(nums) - moveCount
            endIndex = len(nums)

            # 4. 옮긴 범위를 배열에서 삭제한다
            del nums[startIndex:endIndex]
        
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        