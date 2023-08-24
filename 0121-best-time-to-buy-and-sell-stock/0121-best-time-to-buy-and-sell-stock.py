class Solution(object):
    def maxProfit(self, prices):
        
        # 1. prices 배열이 비어있다면 return 0
        if len(prices) == 0:
            return 0
    
        # 2. 이익 변수 초기화
        profit = 0
        
        # 3. 최소 가격 변수 초기화
        min_price = prices[0]

        
        for price in prices:
            
            # 4. 현재 가격이 최소 가격보다 낮으면 현재 가격을 최소 가격으로 설정
            if price < min_price:
                min_price = price
                
            else:
                # 5. 현재가격 - 최소가격 뺀값이 기존 이익보다 높으면 이익을 업데이트
                profit = max(price - min_price, profit)

        return profit


        """
        :type prices: List[int]
        :rtype: int
        """
        