class Solution(object):
    def twoSum(self, numbers, target):

        # 1. left, right 포인터를 하나씩 만든다.

        # 2. 배열의 길이만큼 반복하는 for-in 문을 선언한다.

        # 3. left 는 numbers[0] (배열의 맨첫번째), right 는 numbers[len(index) - 1] (배열의 맨끝) 에서 시작한다.

        # 4. target 과 left, right 을 더한값을 비교한다.
        # 4-1. target 보다 크면(<) right 를 -1 해서 포인터 위치를 옮긴다.
        # 4-2. target 보다 작으면(>) left 를 +1 해서 포인터 위치를 옮긴다.
        # 4-3. target 과 같으면 left, right 를 +1 씩해서 return 한다.

        left = 0
        right = len(numbers) - 1

        for i in range(len(numbers) - 1):
            
            print(numbers[left] + numbers[right])

            if target == numbers[left] + numbers[right]:
                return [left + 1, right + 1]
            
            if target < numbers[left] + numbers[right]:
                right -= 1

            if target > numbers[left] + numbers[right]:
                left += 1




        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """