from math import floor

SALES_TAX = 1.07
DISCOUNT_PRICE = 0.7
prices = sorted([float(price) for price in input().split(',')], reverse=True)

total_cost = sum(prices)
sale_cost = prices[0] + DISCOUNT_PRICE * sum(prices[1:])

print(floor((total_cost - sale_cost) * SALES_TAX))
