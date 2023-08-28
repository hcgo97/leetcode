import re

class Solution(object):
    def isPalindrome(self, s):
        
        # 1. 문자 특수문자 제거 및 소문자로 변환
        s = re.sub(r'[_\W]', '', s).lower()
        
        # 2. 원본 문자열과 뒤집힌 원본 문자열이 똑같은지 비교
        if s == s[::-1]:
            return True
        else:
            return False
        
        
        """
        :type s: str
        :rtype: bool
        """
        