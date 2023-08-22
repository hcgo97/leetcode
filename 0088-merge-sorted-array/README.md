<h2><a href="https://leetcode.com/problems/merge-sorted-array/">88. Merge Sorted Array</a></h2><h3>Easy</h3><hr><div><p>You are given two integer arrays <code>nums1</code> and <code>nums2</code>, sorted in <strong>non-decreasing order</strong>, and two integers <code>m</code> and <code>n</code>, representing the number of elements in <code>nums1</code> and <code>nums2</code> respectively.</p>

<p><strong>Merge</strong> <code>nums1</code> and <code>nums2</code> into a single array sorted in <strong>non-decreasing order</strong>.</p>

<p>The final sorted array should not be returned by the function, but instead be <em>stored inside the array </em><code>nums1</code>. To accommodate this, <code>nums1</code> has a length of <code>m + n</code>, where the first <code>m</code> elements denote the elements that should be merged, and the last <code>n</code> elements are set to <code>0</code> and should be ignored. <code>nums2</code> has a length of <code>n</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
<strong>Output:</strong> [1,2,2,3,5,6]
<strong>Explanation:</strong> The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [<u>1</u>,<u>2</u>,2,<u>3</u>,5,6] with the underlined elements coming from nums1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> nums1 = [1], m = 1, nums2 = [], n = 0
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The arrays we are merging are [1] and [].
The result of the merge is [1].
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> nums1 = [0], m = 0, nums2 = [1], n = 1
<strong>Output:</strong> [1]
<strong>Explanation:</strong> The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>nums1.length == m + n</code></li>
	<li><code>nums2.length == n</code></li>
	<li><code>0 &lt;= m, n &lt;= 200</code></li>
	<li><code>1 &lt;= m + n &lt;= 200</code></li>
	<li><code>-10<sup>9</sup> &lt;= nums1[i], nums2[j] &lt;= 10<sup>9</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up: </strong>Can you come up with an algorithm that runs in <code>O(m + n)</code> time?</p>
</div>

<br></br>
<hr>
<br></br>

# 2023.08.23

## 풀이 과정

1. 먼저 `nums1` 배열에 `nums2` 배열을 합친다.
```python
nums1 += nums2
```

2. 합쳐진 `nums1` 배열 정렬을 정렬한다.
```python
nums1.sort()
```

3. `nums1` 배열에서 0인 요소만 삭제한다.
- 처음엔 for-in 문을 사용하여 0인 요소를 삭제하려 했으나 삭제되지 않았다.
    ```python
    nums1 = [x for x in nums1 if x != 0]
    ```
- 이유는 함수 내부에서는 `nums1` 이 수정되었지만, 함수가 끝나면 `nums1` 의 수정 내역이 삭제되기 때문이다.
- 수정된 함수 내역을 반영하려면 `return nums1` 을 하여 반영해야하는데, 해당 문제는 return 타입이 따로 지정되어 있지 않기 때문에 `nums1` 의 수정 내역을 반영 할 수 없었다.
- 따라서 아래와 같이 while 문으로 처리하였다.
    ```python
    while 0 in nums1:
        nums1.remove(0)
    ```

## 최초 제출 코드
```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # 1. nums1 요소와 nums2 요소를 합침
        nums1 += nums2
        
        # 2. 정렬
        nums1.sort()
            
        # 3. 0인 요소만 삭제
        while 0 in nums1:
	    nums1.remove(0)
```
<br></br>

## 1차 수정 - 조건문 추가

1. `nums2` 요소가 존재하는 경우에만 `nums1` 요소와 합치면 되므로 조건문을 추가하였다.
```python
if n != 0:
    nums1 += nums2
```

2. `sort()` 함수를 사용해야 하는 경우는 `nums1` + `nums2` 한 결과 일때 밖에 없으므로 해당 조건문을 추가하였다.
    - `nums2` 요소만 존재하는 경우일때는 이미 정렬되어 있는 `nums2` 배열을 `nums1` 에 추가한 경우이므로 `sort()` 함수를 사용하지 않아도 된다.
```python
if m != 0 and n != 0:
    nums1.sort()
```

## 1차 수정 코드
```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # 1. nums2 요소가 있는 경우에만 nums1 요소와 nums2 요소를 합침
        if n != 0:
            nums1 += nums2

	    # 2. nums1 요소와 nums2 요소가 둘다 있는데 합친 경우라면 정렬
	    if m != 0:
	        nums1.sort()
            
        # 3. nums1 에서 0인 요소만 삭제
        while 0 in nums1:
            nums1.remove(0)
```
<br></br>

## 2차 수정 - 문제를 잘못 이해한 부분 수정

- 0의 값을 가지는 요소는 모두 삭제해야 하는 것으로 문제를 잘못 이해하고 있었다.
- 0인 요소는 무조건 삭제하는 것이 아니라, `**nums1` 마지막 요소부터 `nums2` 요소 개수 만큼의 0인 요소를 삭제 해야하기 때문에** 해당하는 조건문을 추가하고 잘못된 코드를 삭제하였다.
```python
if n > 0:
    del nums1[-n:]
```

## 최종 제출 코드
```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # 1. nums2 요소가 있는 경우에만
        if n > 0:
            # 2. nums1 마지막 요소부터 num2 요소 개수만큼 삭제
            del nums1[-n:]
            
            # 3. nums1 요소와 nums2 요소를 합침
            nums1 += nums2
            
            # 4. nums1 요소와 nums2 요소가 둘다 있는데 합친 경우라면 정렬
            if m > 0:
                nums1.sort()
```

## 시간 복잡도
### `O(1) + O(n) + O(n) + O(n log n)` = **`O(n log n)`**
- `nums1` 요소만 있는 경우
    - `O(1)`
- `nums2` 요소만 있는 경우
    - `O(n)`
- `nums1` 요소와 `nums2` 요소가 둘 다 있는 경우
    - `O(n log n)`
<br></br>

## 문제 풀이 기록
<img width="749" alt="image" src="https://github.com/hcgo97/leetcode/assets/72455719/7fab421d-c4ca-4413-8c8f-13824805a527">
<br></br>

## 다른 풀이 방법

### `O(n)` 시간 복잡도를 갖는 풀이 방법
- *링크: [https://leetcode.com/problems/merge-sorted-array/discuss/2360538/Easy-0-ms-100-(Fully-Explained)(Java-C%2B%2B-Python-JS-C-Python3)](https://leetcode.com/problems/merge-sorted-array/discuss/2360538/Easy-0-ms-100-(Fully-Explained)(Java-C%2B%2B-Python-JS-C-Python3))*
```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # Initialize nums1's index
        i = m - 1
        # Initialize nums2's index
        j = n - 1
        # Initialize a variable k to store the last index of the 1st array...
        k = m + n - 1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
```
1. `nums1` 의 마지막 요소(`m - 1`)를 가리키는 포인터 `i` 를 설정한다.
2. `nums2` 의 마지막 요소(`n - 1`)를 가리키는 포인터 `j` 를 설정한다.
3. `nums1`, `nums2` 의 요소들을 합쳤을 때의 마지막 요소(`m + n - 1`)를 가리키는 포인터 `k` 를 설정한다.
4. 포인터 `j`가 0보다 같거나 클 경우
    1. `nums1[i]` 요소와 `nums[j]` 요소를 비교 후, 더 큰 요소를 `nums1[k]` 에 대체한다.
    2. 포인터 `k` 와 대체한 요소의 포인터를 -1 만큼 옮긴다.
    3. 포인터 `j` 가 -1 이 될때까지 반복한다.
5. 포인터 `j` 가 0보다 작을 경우에는 `nums2` 의 요소가 존재하지 않는다는 것이므로 로직이 종료된다.
<br></br>

## 회고
학부 시절 이후로는 처음으로 알고리즘 문제를 풀어본건데 eazy 난이도임에도 불구하고 생각보다 어렵게 느껴져서 당황스러웠다.<br>
여러번의 수정 끝에 코드가 통과되었을때는 개발을 처음 시작했던 때와 같은 짜릿한 희열이 느껴졌다.<br>
앞으로도 꾸준히 문제를 풀어서 지금보단 더 수월하게 풀 수 있도록 노력해야겠다.<br>
