class Solution(object):
    def canJump(self, nums):
                    
        # 1. 배열 요소가 1개면 return true
        if len(nums) == 1:
            return True

        # 2. 현재 위치에서 최대 이동 가능한 범위를 나타내는 변수 초기화
        move = nums[0]

        while move < len(nums):
            
            # 3. 현재 위치가 배열의 끝에 도달 가능하면 return true
            if move >= len(nums) - 1:
                return True

            # 4-1. 현재 위치에서 더 이동할 수 없는 상황일 때
            if nums[move] == 0:
                
                # 4-1-1. 이전 위치로 돌아가면서 확인
                for i in range(move - 1, -1, -1):
                    
                    # 4-1-1-1. 이전 위치에서 현재 위치로 도달 가능한지 확인
                    if i + nums[i] > move:
                        # 4-1-1-2. 진행 가능한 위치로 업데이트
                        move = i + nums[i]
                        break

                # 4-1-2. 더 이상 진행 불가능한 상황이면 return false
                else:
                    return False
            
            # 4-2. 현재 위치에서 이동할 수 있다면 다시 이동 가능한 범위만큼 이동시킴
            else:
                move += nums[move]
                
        # 5. 이동 가능한 범위가 배열 요소보다 크면 return true
        if move >= len(nums) - 1:
            return True
                
        # 6. 배열의 마지막까지 도달하지 못한 경우 return false
        return False
                    
                    
        """
        :type nums: List[int]
        :rtype: bool
        """
        