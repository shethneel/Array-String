# -*- coding: utf-8 -*-
"""Experiments.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UFYFG4l-qZC6H1GhwLgroNnGp8P7B7xB

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4] <br>
Output: true <br>
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4] <br>
Output: false <br>
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

nums = [2,3,1,1,4]

jump = 0

for i in range(len(nums)-1, -1, -1):
  if i + nums[i] >= jump:
    jump = i

print ('True') if jump == 0 else print ('false')

"""We are using greedy approach and traversing from the end and checking if addition of index and its value goes to the updated value of jump/that index value"""