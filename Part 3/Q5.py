# Part 3
# Q5. Write a Python program to get the top three items in a shop.

# Sample data:
# {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4: 55
# item1: 45.5
# Item3: 41.3

items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# # Sort the items by value in descending order and get the top 3
top_3_items = dict(sorted(items.items(), key=lambda x: x[1], reverse=True)[:3])
print(top_3_items)

prices = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}
# Get the maximum, second maximum, and third maximum prices using the sorted function
max_price, second_max_price, third_max_price = sorted(prices.values(), reverse=True)[:3]
print(max_price, second_max_price, third_max_price)
# Find the items corresponding to the maximum, second maximum, and third maximum prices
top_three_items = {item: price for item, price in prices.items() if price in [max_price, second_max_price, third_max_price]}
print(top_three_items)