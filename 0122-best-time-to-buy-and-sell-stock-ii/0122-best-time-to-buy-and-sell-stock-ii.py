class Solution(object):
    def maxProfit(self, prices):
        
        # 1. prices 배열 요소가 2개 미만일 경우 바로 return 0
        if len(prices) < 2:
            return 0
        
        # 2. 이익 변수 초기화
        profit = 0
        
        for i in range(1, len(prices)):
            # 3. 현재 가격이 이전 가격 보다 높을때만 이익이 나므로 이익을 업데이트함
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
                
        return profit
                
        """
        :type prices: List[int]
        :rtype: int
        """
        