# -*- coding: utf-8 -*-
"""Zigzag Conversion.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UFYFG4l-qZC6H1GhwLgroNnGp8P7B7xB

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N : row 1

A P L S I I G : row 2

Y   I   R : row 3

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3

Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4

Output: "PINALSIGYAHRPI"

Explanation:

P     I    N : row 1

A   L S  I G : row 2

Y A   H R : row 3

P     I : row 4

Example 3:

Input: s = "A", numRows = 1

Output: "A"

Problem : https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150
"""

s = "PAYPALISHIRING"
numRows = 3

if numRows == 1:
  print ('1')

ans = ""

for r in range(numRows):
  increment = 2*(numRows-1)
  for i in range(r, len(s), increment):
    ans+=s[i]
    if r > 0 and r < numRows-1 and i + increment - 2*r < len(s):
      ans+=s[i + increment - 2*r]

print (ans)

"""The given solution implements the conversion of the input string into the zigzag pattern based on the number of rows specified. Let's break down the logic of the solution:

1. **Initialize Variables**:
    - Initialize the input string `s` and the number of rows `numRows`.
    - Check if `numRows` is equal to 1. If so, the output will be the input string itself, so the program prints it and exits.

2. **Outer Loop (Rows)**:
    - Iterate over each row `r` from 0 to `numRows - 1`.

3. **Inner Loop (Columns)**:
    - Calculate the `increment` value as `2 * (numRows - 1)`, which represents the number of characters in each column.
    - Iterate over each character in the input string `s`, starting from the current row `r` with a step size of `increment`.
    - Append the character at index `i` to the result string `ans`.
    - For rows other than the first and last rows, there are additional characters that need to be included. So, inside this loop, if the current row `r` is greater than 0 and less than `numRows - 1`, and there exists a character at index `i + increment - 2*r`, append this character to the result string `ans`.

4. **Output Result**:
    - After iterating through all rows and columns, the result string `ans` contains the zigzag pattern of the input string based on the number of rows.
    - Print the result string.

**Explanation**:
- The solution constructs the zigzag pattern row by row.
- For each row, it iterates through the input string, considering only the characters that belong to that row.
- It handles the special cases for rows other than the first and last rows where additional characters need to be included.
- Finally, it prints the resulting zigzag pattern.

Reference : https://youtu.be/Q2Tw6gcVEwc?si=vhUHwegraZJ-7ptP
"""