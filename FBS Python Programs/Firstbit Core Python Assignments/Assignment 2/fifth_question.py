# WAP to calculate selling price of a book based on cost price and discount

cost_price = float(input("Enter cost price of the book: "))
discount_percentage = float(input("Enter the '%' discount: "))

discount = (cost_price*discount_percentage)/100

selling_price = cost_price - discount

print(f"The selling price of the book is Rs.{selling_price}")