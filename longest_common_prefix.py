# -*- coding: utf-8 -*-
"""Longest Common Prefix.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UFYFG4l-qZC6H1GhwLgroNnGp8P7B7xB

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]

Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]

Output: ""

Explanation: There is no common prefix among the input strings.
"""

strs = ["flower","flow","flight"]

s = sorted(strs)

s

first = s[0]

first

last = s[-1]

last

ans = ""

for i in range(min(len(first), len(last))):

  if first[i] != last[i]:
    print (ans)
    break
  else:
    ans = ans + first[i]

"""The solution provided aims to find the longest common prefix string among an array of strings. It does so by sorting the array of strings lexicographically, which enables finding the common prefix efficiently.

Here's the breakdown of the solution's logic:

1. **Sort the Array of Strings**:
   - The array of strings `strs` is sorted lexicographically using the `sorted()` function and assigned to the variable `s`. Sorting the array ensures that the first and last strings in the sorted array will provide the maximum common prefix.

2. **Retrieve the First and Last Strings**:
   - The first string (`first`) and the last string (`last`) from the sorted array `s` are extracted.

3. **Iterate Through Characters**:
   - The solution initializes an empty string `ans` to store the common prefix.
   - It then iterates through the characters of the `first` string (or `last` string, as both are sorted and share the common prefix).
   - The loop runs for the minimum length of `first` and `last` strings to avoid index out of range errors.

4. **Compare Characters**:
   - In each iteration, it compares the corresponding characters of `first` and `last` strings.
   - If the characters match, it appends the character to the `ans` string, indicating the common prefix continues.
   - If the characters do not match, it breaks out of the loop as the common prefix ends here.

5. **Return the Result**:
   - The resulting `ans` string contains the longest common prefix among the input strings.
   - If there's no common prefix, the `ans` string remains empty.

The solution leverages the property of lexicographical sorting to efficiently find the common prefix and then iterates through the characters to confirm the common prefix. This approach ensures the correctness of the result while handling edge cases such as an empty input array or an input array with only one string.
"""