# -*- coding: utf-8 -*-
"""Trapped Water.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UFYFG4l-qZC6H1GhwLgroNnGp8P7B7xB

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output: 6

Explanation:

The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]

Output: 9

Question link : https://leetcode.com/problems/trapping-rain-water/description/?envType=study-plan-v2&envId=top-interview-150
"""

class Solution:
    def trap(height):
        if not height:
            return 0

        l = 0
        r = len(height)-1

        l_max = height[l]
        r_max = height[r]

        result = 0

        while l<r:
            if l_max<r_max:
                l+=1
                l_max = max(l_max, height[l])
                result = result + l_max - height[l]
            else:
                r-=1
                r_max = max(r_max, height[r])
                result = result + r_max - height[r]

        return result

height = [0,1,0,2,1,0,1,3,2,1,2,1]

Solution.trap(height)

"""The provided solution uses a two-pointer approach to find the trapped water between bars in the elevation map. Here's an explanation of the solution's logic:

1. Initialize pointers `l` and `r` at the beginning and end of the elevation map.

   ```python
   l = 0
   r = len(height) - 1
   ```

2. Initialize variables `l_max` and `r_max` to represent the maximum height encountered from the left and right, respectively. Set them initially to the heights of the first and last bars.

   ```python
   l_max = height[l]
   r_max = height[r]
   ```

3. Initialize the `result` variable to zero. This variable will accumulate the trapped water.

   ```python
   result = 0
   ```

4. Use a while loop to iterate as long as the left pointer (`l`) is less than the right pointer (`r`).

   ```python
   while l < r:
   ```

5. Inside the loop, check if the height at the left pointer (`height[l]`) is less than the height at the right pointer (`height[r]`).

   ```python
   if l_max < r_max:
   ```

   a. Increment the left pointer (`l`) and update the `l_max` to be the maximum of its current value and the new height at the left pointer.

      ```python
      l += 1
      l_max = max(l_max, height[l])
      ```

   b. Update the `result` by adding the difference between `l_max` and the height at the new left pointer (`height[l]`). This represents the trapped water at this position.

      ```python
      result = result + l_max - height[l]
      ```

   6. If the height at the left pointer is not less than the height at the right pointer, then decrement the right pointer (`r`) and update the `r_max` similarly.

      ```python
      else:
          r -= 1
          r_max = max(r_max, height[r])
          result = result + r_max - height[r]
      ```

7. Continue this process until the left and right pointers meet.

8. The `result` variable will contain the total trapped water, and the function returns this value.

   ```python
   return result
   ```

In summary, the solution iterates through the elevation map, using two pointers from the left and right sides. It calculates the trapped water at each step based on the minimum height encountered so far from the left and right sides. The two-pointer approach ensures an efficient traversal through the elevation map to calculate the trapped water.

Solution explaination : https://youtu.be/ZI2z5pq0TqA?si=4RqkJf_nWfwsxPrT
"""