class Solution(object):
    def removeDuplicates(self, nums):
        
        # 중복이 아닌 요소들을 담을 set 생성
        numSet = set()
        
        # 중복이 아닌 요소들의 위치를 지정할 변수 초기화
        index = 0

        for num in nums:
            
            # 1. 현재 요소가 set 에 없는 요소라면
            if num not in numSet:
                
                # 2. set 에 추가
                numSet.add(num)
                
                # 3. index 위치로 현재 요소 옮기기
                nums[index] = num
                
                # 4. index 위치 +1 만큼 옮김
                index += 1
        
        return index

        """
        :type nums: List[int]
        :rtype: int
        """
        