class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # 1. nums2 요소가 있는 경우에만
        if n > 0:
            # 2. nums1 마지막 요소부터 num2 요소 개수만큼 삭제
            del nums1[-n:]
            
            # 3. nums1 요소와 nums2 요소를 합침
            nums1 += nums2
            
            # 4. nums1 요소와 nums2 요소가 둘다 있는데 합친 경우라면 정렬
            if m != 0:
                nums1.sort()

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """