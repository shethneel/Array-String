# -*- coding: utf-8 -*-
"""Jump Game II.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UFYFG4l-qZC6H1GhwLgroNnGp8P7B7xB

You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n

Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]

Output: 2

Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: nums = [2,3,0,1,4]

Output: 2
"""

nums = [2, 3, 4, 1, 4]

jump = 0

left = right = 0

while right < len(nums)-1:
  rng = 0
  for i in range(left, right+1):
    rng = max(rng, i+nums[i])

  left = right + 1
  right = rng

  jump+=1

print(jump)

"""1. Initialize `jump` variable to 0, representing the minimum number of jumps required.

2. Set `left` and `right` pointers to 0 initially, defining the range of elements to consider.

3. While the `right` pointer is less than the last index of the array:
   - Initialize `rng` (range) variable to 0.
   - Iterate over the elements within the current range (`left` to `right` inclusive).
   - Update `rng` to be the maximum value of the current `rng` and the position `i` plus the jump value at that position.
   - Update `left` pointer to be one position after the current `right`.
   - Update `right` pointer to the furthest reachable point found in the inner loop.
   - Increment `jump` variable.

4. Print the final value of `jump`, representing the minimum number of jumps needed to reach the end.
"""