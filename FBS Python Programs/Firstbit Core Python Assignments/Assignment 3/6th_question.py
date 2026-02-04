# Write a program to calculate profit or loss.

cost_price = float(input("Enter the Cost Price (CP): "))
selling_price = float(input("Enter the Selling Price (SP): "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    percentProfit = (profit/cost_price)*100
    print(f"Profit is {profit:.2f} and % profit is {percentProfit}%")

elif selling_price < cost_price:
    loss = cost_price - selling_price
    percentLoss = (loss/cost_price)*100
    print(f"Loss is {loss:.2f} and % loss is {percentLoss}%")

else:
    print("No Profit, No Loss.")
