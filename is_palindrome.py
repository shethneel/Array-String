# -*- coding: utf-8 -*-
"""Is Palindrome.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UFYFG4l-qZC6H1GhwLgroNnGp8P7B7xB

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"

Output: true

Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"

Output: false

Explanation: "raceacar" is not a palindrome.

Example 3:

Input: s = " "

Output: true

Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
"""

s = "A man, a plan, a canal: Panama"

s = ''.join(filter(lambda x: x.isalnum(), s))

s = s.upper()

rev = s[::-1]

if s == rev:
  print ('True')
else:
  print ('False')

"""The provided solution is a Python code snippet that determines whether a given string `s` is a palindrome according to the definition provided.

Here's a breakdown of the solution's logic:

1. `s = ''.join(filter(lambda x: x.isalnum(), s))`: This line removes all non-alphanumeric characters from the string `s` using the `filter` function with a lambda function that checks if each character `x` is alphanumeric (`x.isalnum()`). The `filter` function returns an iterator containing only the alphanumeric characters, which are then joined back together into a string. This step effectively removes spaces, punctuation, and other non-alphanumeric characters from the string.

2. `s = s.upper()`: This line converts all characters in the string `s` to uppercase. This step is done to make the comparison case-insensitive, as the problem statement specifies that after converting all uppercase letters into lowercase letters, the string should be checked for palindrome properties.

3. `rev = s[::-1]`: This line reverses the string `s` using slicing (`[::-1]`) and assigns the result to the variable `rev`.

4. `if s == rev:`: This line checks if the original string `s` is equal to its reverse `rev`. If they are equal, it means the original string is a palindrome.

5. If the condition `s == rev` is `True`, it prints `'True'`, indicating that the input string is a palindrome. Otherwise, it prints `'False'`, indicating that the input string is not a palindrome.

Let's apply this logic to the provided example:

```python
s = "A man, a plan, a canal: Panama"
```

1. After removing non-alphanumeric characters, `s` becomes `"AmanaplanacanalPanama"`.
2. After converting all characters to uppercase, `s` becomes `"AMANAPLANACANALPANAMA"`.
3. Reversing the string `s` gives `rev` as `"AMANAPLANACANALPANAMA"`.
4. Since `s` is equal to `rev`, the condition `s == rev` evaluates to `True`.
5. Therefore, the output will be `'True'`, indicating that the input string is a palindrome.

The solution effectively implements the logic required to determine whether a given string is a palindrome according to the provided definition.
"""