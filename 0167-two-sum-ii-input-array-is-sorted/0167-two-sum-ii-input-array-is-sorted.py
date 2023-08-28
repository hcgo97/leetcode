class Solution(object):
    def twoSum(self, numbers, target):

        # 1. numbers 배열 요소가 2개밖에 없으면 index 1, 2 를 return
        if len(numbers) == 2:
            return [1, 2]
        
        # 2. 투 포인터 방법 사용하기 위해 left, right 변수 선언
        # left 는 numbers[0] (배열의 가장 첫번째), right 는 numbers[len(index) - 1] (배열의 가장 마지막) 에 위치하도록 초기화
        left = 0
        right = len(numbers) - 1
        
        # 3. 배열의 길이만큼 반복하는 for 문 선언
        for i in range(len(numbers) - 1):
            sumNumbers = numbers[left] + numbers[right]
            
            # 4. target 과 left, right 을 더한값을 비교한다.
            if target < sumNumbers:
                # 4-1. target 보다 크면(<) right 를 -1 해서 포인터 위치를 옮김
                right -= 1

            elif target > sumNumbers:
                # 4-2. target 보다 작으면(>) left 를 +1 해서 포인터 위치를 옮김
                left += 1
                
            else:
                # 4-3. target 과 같으면 left, right 를 +1 씩해서 return
                return [left + 1, right + 1]
            
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """