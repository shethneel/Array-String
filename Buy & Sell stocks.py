# -*- coding: utf-8 -*-
"""Experiments.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UFYFG4l-qZC6H1GhwLgroNnGp8P7B7xB

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4] <br>
Output: 5 <br>
Explanation: <br> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.<br>
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.<br>
Example 2:

Input:<br> prices = [7,6,4,3,1]<br>
Output: 0<br>
Explanation: In this case, no transactions are done and the max profit = 0.
"""

prices = [2,5,1,3]

# set profit to 0
profit = 0

# set buying price to first element of prices
buy = prices[0]

# This will become starting range of our list and we will update it as we will update our buy var.
# This will help us to reduce time complexity

x = 1

for sell in prices[1:]:

  # if selling price is bigger than the buying price, we will deduct it from buying price
  # also we will check what is bigger, current profit or sell - buy
  # profit var will update accordind to the received max value

  if sell > buy:
    profit = max(profit, sell-buy)

  # if selling price is smaller than buying price, then the selling price will be the new buying price
  # we will also update the x
  else:
    buy = sell
    x+=1

print (profit)