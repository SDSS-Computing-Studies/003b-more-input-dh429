#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""

price1 = input("Enter the first price: ").strip()
price1 = float(price1)

price2 = input("Enter the second price: ").strip()
price2 = float(price2)

price3 = input("Enter the third price: ").strip()
price3 = float(price3)

price4 = input("Enter the fourth price: ").strip()
price4 = float(price4)

price5 = input("Enter the fifth price: ").strip()
price5 = float(price5)

subtotal = price1 + price2 + price3 + price4 + price5
subtotal = round(subtotal, 2)

taxes = subtotal * 0.12
taxes = round(taxes , 2)

total = taxes + subtotal
total = round(total, 2)

print(f"Your subtotal is ${subtotal} and your taxes total ${taxes} for a total of ${total}")

