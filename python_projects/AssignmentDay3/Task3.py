custName = "Mary Smith"
itemDesc = "Shirt"
message1 = custName
message2 = itemDesc
price = int(25);
tax = float(1.2);
quantity = int(2);
message3 = quantity
print(message1, "wants to purchase", message3, message2)
total = price * tax * quantity
print("Total cost with tax is:", total)
outOfStock = True
if quantity > 1:
    print(message1, "wants to purchase", message3, message2 + "(s)")
if outOfStock == True:
    print("item is unavailable")
else:
    print("Total cost with tax is:", total)
