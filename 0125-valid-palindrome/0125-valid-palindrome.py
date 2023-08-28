import re

class Solution(object):
    def isPalindrome(self, s):
        
        # 1. 문자 띄워쓰기, 특수문자 없애기
        s = re.sub(r'[_\W]', '', s).lower()
        
        # 2. 문자 소문자로 변환
        #s = s.lower()
        
        # 3. string 변수 하나 더 만들고 뒤집기
        #sReverse = s[::-1]
        
        # 4. 3 이랑 4 랑 똑같은지 비교
        if s == s[::-1]:
            return True
        else:
            return False
        
        
        """
        :type s: str
        :rtype: bool
        """
        