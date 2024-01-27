# -*- coding: utf-8 -*-
"""Rotate Array.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y_DwxCl3cPEYaaDMdoqc2-DjhmNwXotD

Rotate the given array nums to the right side by k steps

Examples :

Input:

nums = [1,2,3,4,5,6,7], <br>
k = 3 <br>
Output:

[5,6,7,1,2,3,4]<br>

Explanation:<br>
rotate 1 steps to the right: [7,1,2,3,4,5,6]<br>
rotate 2 steps to the right: [6,7,1,2,3,4,5]<br>
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Input <br>

nums =[1,2] <br>
k = 2 <br>

Output <br>
[1,2]

Input <br>

nums = [1,2] <br>
k = 5 <br>

Output <br>
[2,1]
"""

nums = [1,4,2,-7,5]

k = 2

for i in range(len(nums)):
    if k > len(nums):
        k = k - len(nums)
nums[:] = nums[-k:] + nums[:-k]

nums

"""Intuition

Solve problem in easy manner

Approach

Adjustment for Large k:

Inside the loop, there's an if statement to check if k is greater than the length of the array.
If true, it means that rotating by k steps is equivalent to rotating by k % len(nums) steps.
The value of k is adjusted by subtracting the length of the array until it becomes less than or equal to the length of the array.

Rotation Operation:

The list nums is modified in-place to achieve the rotation.
nums[-k:] represents the last k elements of the array.
nums[:-k] represents all elements of the array except the last k elements.
The concatenation of these two slices effectively rotates the array to the right by k steps.
The result is assigned back to nums using slicing and assignment (nums[:]).

Complexity

Time complexity: O(n)

Space complexity: O(1)
"""