# -*- coding: utf-8 -*-
"""Merge_Sorted_Array.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y_DwxCl3cPEYaaDMdoqc2-DjhmNwXotD

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



<b>Example 1:</b>

Input:

nums1 = [1,2,3,0,0,0], <br>
m = 3, <br>
nums2 = [2,5,6], <br>
n = 3

Output: [1,2,2,3,5,6]

Explanation:

The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

<b>Example 2:</b>

Input:

nums1 = [1], <br>m = 1,<br> nums2 = [],<br> n = 0

Output: [1]

Explanation:

The arrays we are merging are [1] and [].
The result of the merge is [1].

<b>Example 3:</b>

Input:

nums1 = [0],<br> m = 0,<br> nums2 = [1],<br> n = 1

Output: [1]

Explanation:

The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
"""

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

class Solution(object):
    def merge(self, n1, m, n2, n):

        for j in range(n):
            n1[m + j] = n2[j]

            if len(n1) == m+n-1 and j>=0:
                n1.append(n2[j])
        n1.sort()

"""Intuition

There are multiple approaches to solve this problem such as bruteforce with multiple loops and adding 2 special cases

In my solution (Which is an updated solution of another person), I am using basic one loop and one special case to avoid index out of range error

Approach

Here, we are updating/adding values after the required elements of n1 provided by m

Why special case?

Let's say if there are 5 elements in n1 and 3 in n2, but we are supposed to add 6 elelemtns in n1, i.e. 4 of n1 and 2 of n2, then this basic method fails without special case

Ex :

n1 = [1,2,3,6,9] <br>
m = 4 <br>
n2 = [4,7,8] <br>
n = 2

In this case, we only have 5 elements but as per requirement, we are supposed to add 6 elements (4 of m and 2 of n)

Complexity

Time complexity:

The time complexity of the merge function is O(n*log n), where n represents the total number of elements being merged.

Space complexity:

The space complexity is O(n) due to the storage of the input arrays, and O(1) for auxiliary space.
"""